import json
import os
import sys

def verify_json_file(file_path):
    """
    Verify if a JSON file is valid.
    Returns a tuple: (is_valid, message)
    """
    # Check if file exists
    if not os.path.exists(file_path):
        return False, f"Error: File '{file_path}' does not exist"

    # Check if file is empty
    if os.path.getsize(file_path) == 0:
        return False, f"Error: File '{file_path}' is empty"

    try:
        # Attempt to read and parse the JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        
        # Check if the JSON is empty ({} or [])
        if json_data == {} or json_data == []:
            return True, "Warning: JSON file is valid but empty"
        
        # Basic structure check
        if not isinstance(json_data, (dict, list)):
            return False, "Error: JSON root must be an object or array"
        
        return True, "JSON file is valid"

    except json.JSONDecodeError as e:
        return False, f"Error: Invalid JSON syntax - {str(e)}"
    except UnicodeDecodeError:
        return False, "Error: File is not valid UTF-8 encoded"
    except Exception as e:
        return False, f"Error: Unexpected error - {str(e)}"

def main():
    # Check if file path is provided as command-line argument
    if len(sys.argv) != 2:
        print("Usage: python verify_json_file.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    is_valid, message = verify_json_file(file_path)
    print(message)
    
    # If valid and not empty, print the content
    if is_valid and "empty" not in message.lower():
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)
                print("\nJSON Content:")
                print(json.dumps(json_data, indent=2))
        except Exception as e:
            print(f"Error printing content: {str(e)}")

if __name__ == "__main__":
    main()