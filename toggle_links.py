# replaces link formats in markdown/text
import re

def markdown_links_to_text(inp_string):
    return re.sub(r'\(\[#(\d+)\]\(.*\)\)', r'(#\1)', inp_string)

def text_links_to_markdown(inp_string):
    return re.sub(r'\(#(\d+)\)', r'\(\[#\1\]\(https://github.com/pytorch/pytorch/pull/\1\)\)', inp_string)

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Convert links')
    parser.add_argument('input_file', nargs='?', help='Input file containing the list of commits')
    parser.add_argument('output_file', nargs='?', help='Output file that is written to')
    parser.add_argument('convert_to', help='Either text or md')
    args = parser.parse_args()
    with open(args.input_file, 'r') as f:
        fstring = f.read()
        with open(args.output_file, 'w') as out:
            if args.convert_to == 'text':
                out.write(markdown_links_to_text(fstring))
            elif args.convert_to == 'md':
                out.write(text_links_to_markdown(fstring))
            else:
                raise Exception(f"bad convert_to input {args.convert_to}")







if __name__ == "__main__":
    main()
