import os
import re
import argparse

# Define the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--root_dir', default='.', help='Root directory to search for TODO comments')
parser.add_argument('--todo_regex', default=r'^\s*#\s*TODO\s*(.*)$', help='Regular expression to match TODO comments')
args = parser.parse_args()

# Loop through all files in the root directory and its subdirectories
for dirpath, dirnames, filenames in os.walk(args.root_dir):
    for filename in filenames:
        # Only process Python files
        if filename.endswith('.py'):
            # Read the file contents
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'r') as f:
                contents = f.read()
            # Search for TODO comments
            matches = re.findall(args.todo_regex, contents, re.MULTILINE)
            # Print the TODO comments
            for match in matches:
                print(match)
