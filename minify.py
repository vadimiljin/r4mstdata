#!/usr/bin/env python3
import os
import json

def minify_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, separators=(',', ':'))
        print(f"Minified: {file_path}")
    except Exception as e:
        print(f"Skipping {file_path}: {e}")

def main():
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if filename.endswith('.json'):
                file_path = os.path.join(root, filename)
                minify_json_file(file_path)

if __name__ == '__main__':
    main()
