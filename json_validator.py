#!/usr/bin/env python3

import json
import os
import sys
import argparse
from pathlib import Path

def is_valid_json(file_path):
    """Check if a file contains valid JSON."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
        return True
    except (json.JSONDecodeError, UnicodeDecodeError, FileNotFoundError):
        return False

def validate_single_file(file_path):
    """Validate a single JSON file."""
    if not file_path.endswith('.json'):
        print(f"Error: '{file_path}' is not a .json file")
        return False
    if is_valid_json(file_path):
        print(f"'{file_path}' is a valid JSON file")
        return True
    else:
        print(f"'{file_path}' is NOT a valid JSON file")
        return False

def validate_directory(dir_path):
    """Validate all .json files in a directory."""
    dir_path = Path(dir_path)
    if not dir_path.is_dir():
        print(f"Error: '{dir_path}' is not a directory")
        return

    json_files = list(dir_path.glob('*.json'))
    if not json_files:
        print(f"No .json files found in '{dir_path}'")
        return

    valid_count = 0
    invalid_files = []

    for file_path in json_files:
        if is_valid_json(file_path):
            valid_count += 1
        else:
            invalid_files.append(str(file_path))

    total_files = len(json_files)
    print(f"\nValidation Summary for '{dir_path}':")
    print(f"Total JSON files checked: {total_files}")
    print(f"Valid JSON files: {valid_count}")
    print(f"Invalid JSON files: {len(invalid_files)}")
    
    if invalid_files:
        print("\nInvalid JSON files:")
        for file in invalid_files:
            print(f"- {file}")
    else:
        print("All JSON files are valid!")

def main():
    parser = argparse.ArgumentParser(description="Validate JSON file(s)")
    parser.add_argument("path", help="Path to a JSON file or directory")
    args = parser.parse_args()

    path = Path(args.path)
    
    if path.is_file():
        validate_single_file(str(path))
    elif path.is_dir():
        validate_directory(str(path))
    else:
        print(f"Error: '{path}' is neither a file nor a directory")
        sys.exit(1)

if __name__ == "__main__":
    main()