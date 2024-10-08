import re
import webbrowser
import readline
import tempfile
import subprocess
import sys
import os
# Predefined classes with their corresponding single letter hotkeys
classes = {
    'b': 'bc breaking',
    'd': 'deprecations',
    'n': 'new features',
    'i': 'improvements',
    'u': 'bug fixes',
    'p': 'performance',
    'D': 'documentation',
    'e': 'developers',
    'N': 'not user facing',
    'T': 'Untopiced (not relevant to inductor)'
    # Add new classes here, e.g., 'n': 'New Class'
}

def remove_square(line):
    # Remove anything at the start that is contained within square brackets
    return re.sub(r'\[.*?\]\s*', '', line)

def process_line(line):
    # Find the issue numbers
    issue_numbers = re.findall(r'\(#(\d+)\)', line)
    # Remove the issue numbers from the line
    line = re.sub(r'\(#\d+\)', '', line)
    return line.strip(), issue_numbers

def get_class():
    print("Select a class:")
    for hotkey, class_name in classes.items():
        print(f"{hotkey}: {class_name}")
    while True:
        choice = input("> ")
        if choice in classes:
            return classes[choice]
        else:
            print("Invalid choice. Please try again.")

def rewrite_line(line, editor='vim'):
    with tempfile.NamedTemporaryFile(mode='w') as tmp_file:
        tmp_file.write(line)
        tmp_file.flush()
        subprocess.run([editor, tmp_file.name])
        with open(tmp_file.name, 'r') as f:
            return f.read().strip()

def save_to_file(file_name, data):
    with open(file_name, 'w') as f:
        for class_name, lines in data.items():
            f.write(f"# {class_name}\n")
            for line in lines:
                f.write(f" - {line}\n")

def load_from_file(file_name):
    data = {}
    current_class = None
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith('#'):
                current_class = line[2:]
                data[current_class] = []
            elif line.startswith('-'):
                data[current_class].append(line[2:])
    return data

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Process commits')
    parser.add_argument('input_file', nargs='?', help='Input file containing the list of commits')
    parser.add_argument('output_file', nargs='?', help='Output file name')
    parser.add_argument('-e', '--editor', default='vim', help='Editor to use for rewriting commit messages')
    parser.add_argument('-s', '--skip', help='Whether or not to skip ', action=argparse.BooleanOptionalAction)
    args = parser.parse_args()
    if not args.input_file:
        args.input_file = input("Enter a file name containing the list of commits: ")
    if not args.output_file:
        args.output_file = input("Enter an output file name: ")
    resume = False
    if os.path.exists(args.output_file):
        response = input(f"Output file '{args.output_file}' already exists. Do you want to resume from it? (y/n): ")
        if response.lower() == 'y':
            resume = True
    if resume:
        try:
            data = load_from_file(args.output_file)
        except Exception as e:
            print(f"Error loading from file: {e}")
            return
    else:
        data = {class_name: [] for class_name in classes.values()}
    try:
        with open(args.input_file, 'r') as f:
            commits = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("File not found.")
        return
    existing_issue_numbers = set()
    for lines in data.values():
        for line in lines:
            issue_numbers = re.findall(r'\[#(\d+)\]', line)
            existing_issue_numbers.update(issue_numbers)
    for line in commits:
        processed_line, issue_numbers = process_line(line)
        if any(issue_number in existing_issue_numbers for issue_number in issue_numbers):
            if args.skip:
                continue
            response = input(f"Issue number(s) {', '.join(issue_numbers)} already exist in the output file. Do you want to skip this line? (y/n): ")
            if response.lower() == 'y':
                continue
        # Open the issue number link in the system default browser
        for issue_number in issue_numbers:
            url = f"https://github.com/pytorch/pytorch/pull/{issue_number}"
            webbrowser.open(url)
        # Ask the user to categorize it into one of several predefined classes
        class_name = get_class()
        # remove the squares
        processed_line = remove_square(processed_line)
        # Rewrite the line if desired
        rewritten_line = rewrite_line(processed_line, editor=args.editor)
        # Format the link to the issues
        links = ' '.join(f"([#{issue_number}](https://github.com/pytorch/pytorch/pull/{issue_number}))" for issue_number in issue_numbers)
        final_line = f"{rewritten_line} {links}"
        # Save the file state to the output file every iteration
        if class_name not in data:
            data[class_name] = []
        data[class_name].append(final_line)
        save_to_file(args.output_file, data)

if __name__ == "__main__":
    main()
