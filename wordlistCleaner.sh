#!/bin/bash

# Check if an argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <input_file>"
    exit 1
fi

# Input file
input_file="$1"

# Check if the input file exists
if [ ! -f "$input_file" ]; then
    echo "Error: Input file not found."
    exit 1
fi

# Convert uppercase letters to lowercase
awk '{print tolower($0)}' "$input_file" > "$input_file.tmp"

# Sort and remove duplicates from the input file
sort -u "$input_file.tmp" -o "$input_file"

# Remove temporary file
rm "$input_file.tmp"

echo "File sorted, duplicates removed, and uppercase letters converted to lowercase: $input_file"
