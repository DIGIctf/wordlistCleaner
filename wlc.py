#!/usr/bin/env python3
import sys
import unicodedata
import os
import shutil

def clean_text(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.readlines()
    cleaned_text = [unicodedata.normalize('NFKD', line).encode('ascii', 'ignore').decode('ascii') for line in text]
    return cleaned_text

def convert_to_lowercase(text):
    return [line.lower() for line in text]
    
def convert_to_uppercase(text):
    return [line.upper() for line in text]

def capitalize_first_letter(text):
    return [' '.join(word.capitalize() for word in line.split()) for line in text]

def replace_spaces_with_underscores(text):
    return [line.replace(' ', '_') for line in text]

def replace_underscores(text):
    return [line.replace('_', '') for line in text]

def remove_blank_lines(text):
    return [line for line in text if line.strip()]

def remove_duplicates(text):
    return list(set(text))

def main(input_file):
    # Clear the contents of tmp_cleaned_output.txt
    with open('tmp_cleaned_output.txt', 'w', encoding='utf-8'):
        pass



    # Clean the text
    cleaned_text = clean_text(input_file)

    # Convert to lowercase and append to the output file
    with open('tmp_cleaned_output.txt', 'a', encoding='utf-8') as f:
        f.write('\n'.join(convert_to_lowercase(cleaned_text)))
        f.write('\n\n')  # Add two newlines after each function output
     
    # Convert to uppercase and append to the output file
    with open('tmp_cleaned_output.txt', 'a', encoding='utf-8') as f:
        f.write('\n'.join(convert_to_uppercase(cleaned_text)))
        f.write('\n\n')  # Add two newlines after each function output      
        
    # Capitalize the first letter of each word and append to the output file
    with open('tmp_cleaned_output.txt', 'a', encoding='utf-8') as f:
        f.write('\n'.join(capitalize_first_letter(cleaned_text)))
        f.write('\n\n')

    # Replace spaces with underscores and append to the output file
    with open('tmp_cleaned_output.txt', 'a', encoding='utf-8') as f:
        f.write('\n'.join(replace_spaces_with_underscores(cleaned_text)))
        f.write('\n\n')

    # Replace underscores and append to the output file
    with open('tmp_cleaned_output.txt', 'a', encoding='utf-8') as f:
        f.write('\n'.join(replace_underscores(cleaned_text)))
        f.write('\n\n')

    # Read from tmp_cleaned_output.txt, remove spaces and underscores, and save to tmp_cleaned_output_part2.txt
    with open('tmp_cleaned_output.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Remove spaces and underscores from each line
    lines = [line.replace(' ', '').replace('_', '') for line in lines]

    # Write the modified text to tmp_cleaned_output_part2.txt
    with open('tmp_cleaned_output_part2.txt', 'w', encoding='utf-8') as f:
        f.write(''.join(lines))

    # Append the content from tmp_cleaned_output_part2.txt to tmp_cleaned_output.txt
    with open('tmp_cleaned_output_part2.txt', 'r', encoding='utf-8') as f_part2:
        part2_lines = f_part2.readlines()

    with open('tmp_cleaned_output.txt', 'a', encoding='utf-8') as f_output:
        f_output.write('\n\n')
        f_output.writelines(part2_lines)
        f_output.write('\n\n')
        
    # Read the contents of the input file and append to tmp_cleaned_output.txt
    with open(input_file, 'r', encoding='utf-8') as f:
        input_lines = f.read()  # Read the whole content of the file as a single string

    # Append the input lines to tmp_cleaned_output.txt with a newline character
    with open('tmp_cleaned_output.txt', 'a', encoding='utf-8') as f:
        f.write('\n\n' + input_lines + '\n')
  
        

    # Remove blank lines from the output file
    with open('tmp_cleaned_output.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    lines = remove_blank_lines(lines)
    with open('tmp_cleaned_output.txt', 'w', encoding='utf-8') as f:
        f.write(''.join(lines))

    # Remove duplicates from the output file
    with open('tmp_cleaned_output.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    lines = remove_duplicates(lines)
    with open('tmp_cleaned_output.txt', 'w', encoding='utf-8') as f:
        f.write(''.join(lines))

    # Remove tmp_cleaned_output_part2.txt
    if os.path.exists('tmp_cleaned_output_part2.txt'):
        os.remove('tmp_cleaned_output_part2.txt')
        

    # Copy tmp_cleaned_output.txt to wordlist_cleaned_00001.txt
    output_file_name = 'wordlist_cleaned_00001.txt'
    file_count = 1
    while os.path.exists(output_file_name):
        file_count += 1
        output_file_name = f'wordlist_cleaned_{file_count:05d}.txt'

    shutil.copyfile('tmp_cleaned_output.txt', output_file_name)
    
    # Remove tmp_cleaned_output.txt
    if os.path.exists('tmp_cleaned_output.txt'):
        os.remove('tmp_cleaned_output.txt')
    
    
    # Print the name of the output file
    print("Wordlist cleaned: ", output_file_name)
    #used for testing to output the results from the file
    #with open(output_file_name, 'r', encoding='utf-8') as f:
    #    print("Contents of the output file:")
    #    print(f.read())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 wordlistCleaner.py <wordlist_file.txt>")
        sys.exit(1)
    input_file = sys.argv[1]
    main(input_file)
