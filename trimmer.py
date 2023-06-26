import re

def trim_md_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Define the regular expression pattern to match table rows
    pattern = r'\|(.+?)\|(.+?)\|(.+?)\|'

    # Use regex to find and replace each row, trimming whitespace within columns
    trimmed_content = re.sub(pattern, lambda m: f'| {m.group(1).strip()} | {m.group(2).strip()} | {m.group(3).strip()} |', content)

    with open(file_path, 'w') as file:
        file.write(trimmed_content)

# Usage example
md_file_path = './ReadMe.md'
trim_md_file(md_file_path)