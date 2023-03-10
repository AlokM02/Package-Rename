import os
import pandas as pd
import re

# Get the current directory
dir_path = os.getcwd()

# Load the excel file
df = pd.read_excel('strings_to_replace.xlsx', header=0)

# Get the search and replace strings
search_strs = df['Search String'].tolist()
replace_strs = df['Replace String'].tolist()

# Create a dictionary to store the replacement counts for each search string
replace_counts = {search_str: 0 for search_str in search_strs}

# Loop through all files in the directory and its subdirectories
for subdir, dirs, files in os.walk(dir_path):
    for file in files:
        # Check if the file extension is not .py
        if not (file.endswith('.py') or file.endswith('.xlsx')):
            # Get the full file path
            file_path = os.path.join(subdir, file)

            # Open the file and read its contents
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_contents = f.read()
                    original_encoding = 'utf-8'
            except UnicodeDecodeError:
                try:
                    with open(file_path, 'r', encoding='Windows-1252') as f:
                        file_contents = f.read()
                        original_encoding = 'Windows-1252'
                except UnicodeDecodeError:
                    with open(file_path, 'r', encoding='ISO-8859-1') as f:
                        file_contents = f.read()
                        original_encoding = 'ISO-8859-1'

            # Loop through each search string and replace it with its corresponding replace string
            for i in range(len(search_strs)):
                # Escape any special characters in the search string
                search_pattern = re.compile(re.escape(search_strs[i]), flags=re.IGNORECASE | re.ASCII)

                # Replace the search string with the replace string
                num_replacements = len(re.findall(search_pattern, file_contents))
                replace_counts[search_strs[i]] += num_replacements
                file_contents = search_pattern.sub(replace_strs[i], file_contents)

            # Write the updated contents back to the file
            with open(file_path, 'w', encoding=original_encoding) as f:
                f.write(file_contents)

# Print the replacement counts for each search string
for search_str, replace_count in replace_counts.items():
    print(f'Replaced "{search_str}" with "{replace_strs[search_strs.index(search_str)]}" {replace_count} times.')
