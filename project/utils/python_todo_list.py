
import os
import re
import argparse

def find_todo_comments(root_dir='.', todo_regex=r'^\s*#\s*TODO\s*(.*)$'):
    # Loop through all files in the root directory and its subdirectories
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            # Only process Python files
            if filename.endswith('.py'):
                # Read the file contents
                filepath = os.path.join(dirpath, filename)
                with open(filepath, 'r') as f:
                    contents = f.read()
                # Search for TODO comments
                matches = re.findall(todo_regex, contents, re.MULTILINE)
                # Print the TODO comments
                for match in matches:
                    print(match)

if __name__ == '__main__':
    # Define the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--root_dir', default='.', help='Root directory to search for TODO comments')
    parser.add_argument('--todo_regex', default=r'^\s*#\s*TODO\s*(.*)$', help='Regular expression to match TODO comments')
    args = parser.parse_args()

    find_todo_comments(args.root_dir, args.todo_regex)
