import re
import webbrowser
import readline
import tempfile
import subprocess
import sys

# Predefined classes with their corresponding single letter hotkeys
classes = {
    'b': 'bc breaking',
    'd': 'deprecations',
    'n': 'new features',
    'i': 'improvements',
    'u': 'bug fixes',
    'p': 'performance',
    'd': 'documentation',
    'e': 'developers',
    'N': 'not user facing',
    'T': 'Untopiced (not relevant to inductor)'
    # Add new classes here, e.g., 'n': 'New Class'
}

def rlinput(prompt, prefill=''):
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   try:
      return input(prompt)  # or raw_input in Python 2
   finally:
      readline.set_startup_hook()

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
        choice = input("> ").lower()
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

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Process commits')
    parser.add_argument('input_file', nargs='?', help='Input file containing the list of commits')
    parser.add_argument('output_file', nargs='?', help='Output file name')
    parser.add_argument('-e', '--editor', default='vim', help='Editor to use for rewriting commit messages')
    args = parser.parse_args()
    if not args.input_file:
        args.input_file = input("Enter a file name containing the list of commits: ")
    if not args.output_file:
        args.output_file = input("Enter an output file name: ")
    try:
        with open(args.input_file, 'r') as f:
            commits = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("File not found.")
        return
    data = {class_name: [] for class_name in classes.values()}
    for line in commits:
        processed_line, issue_numbers = process_line(line)
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
        data[class_name].append(final_line)
        save_to_file(args.output_file, data)
if __name__ == "__main__":
    main()
