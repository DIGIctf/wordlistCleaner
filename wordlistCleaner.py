import sys
import subprocess

def clean_wordlist(input_file):
    try:
        # Read the wordlist file
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Define the output filename
        output_file = 'list-clean.txt'

        # Remove spaces from each line and write to a temporary file
        temp_lines = [line.strip().replace(' ', '') for line in lines]
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write('\n'.join(temp_lines))

        # Run iconv command to replace accent characters
        subprocess.run(['iconv', '-f', 'utf-8', '-t', 'ascii//TRANSLIT', output_file, '-o', output_file])
        
        # Call the bash script to sort and remove duplicates
        subprocess.run(['./wordlistCleaner.sh', output_file])


        print("Wordlist cleaned successfully! Output file:", output_file)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <list_file>")
    else:
        input_file = sys.argv[1]
        clean_wordlist(input_file)
