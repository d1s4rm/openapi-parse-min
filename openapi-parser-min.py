import json
import argparse
import os

def parse_openapi_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    parsed_data = []
    for path_key, path_info in data.get('paths', {}).items():
        method = next(iter(path_info))
        description = path_info[method].get('description')
        host = description.split(' ')[1]
        parsed_data.append({
            'Host': host,
            'Path': path_key,
            'Method': method
        })

    return parsed_data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', help='Input file path')
    args = parser.parse_args()

    file_path = args.file_path

    file_name = os.path.splitext(os.path.basename(file_path))[0]
    output_file_path = f"{file_name}.txt"

    parsed_data = parse_openapi_file(file_path)

    with open(output_file_path, 'w') as output_file:
        for entry in parsed_data:
            output_file.write(f"Host = {entry['Host']}\nPath = {entry['Path']}\nMethod = {entry['Method']}\n\n")

            # Also print to console
            print(f"Host = {entry['Host']}\nPath = {entry['Path']}\nMethod = {entry['Method']}\n")

    print(f"Output saved to {output_file_path}")

if __name__ == "__main__":
    main()