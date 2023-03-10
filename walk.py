import os
import re
from pathlib import Path
import pandas as pd

# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

def search_files(substring, min_word_length):
    # Compile regex pattern outside the loop
    pattern = re.compile(fr'\w*{re.escape(substring)}\w*', flags=re.IGNORECASE | re.ASCII)

    # Initialize results as a list of lists
    results = []

    # Get the absolute path to the Excel file
    excel_file_path = os.path.join(script_dir, 'search_results.xlsx')

    # Check if the Excel file exists
    if os.path.exists(excel_file_path):
        # If it exists, read in the existing data and append to it
        with pd.ExcelFile(excel_file_path) as reader:
            existing_data = reader.parse()
        start_row = len(existing_data)
        df = existing_data.append(pd.DataFrame(columns=['Match', 'Length', 'File Name', 'Line Number', 'Folder']))
    else:
        # If it doesn't exist, create a new DataFrame to hold the results
        start_row = 0
        df = pd.DataFrame(columns=['Match', 'Length', 'File Name', 'Line Number', 'Folder'])

    for file_path in Path('.').rglob('*.*'):
        if file_path.name != 'rename.py':
            try:
                content = file_path.read_text(encoding='utf-8')
            except UnicodeDecodeError:
                try:
                    content = file_path.read_text(encoding='Windows-1252')
                except UnicodeDecodeError:
                    try:
                        content = file_path.read_text(encoding='ISO-8859-8')
                    except UnicodeDecodeError:
                        continue  # skip the file if none of the encodings can decode it
            for line_num, line in enumerate(content.splitlines()):
                for match in pattern.finditer(line):
                    full_word = match.group()
                    word_length = len(full_word)
                    if word_length > min_word_length:
                        # Append results as a list
                        results.append([full_word, word_length, file_path.name, line_num + 1, str(file_path.parent)])

    # Append the results to the DataFrame
    for row_num, row in enumerate(results):
        for col_num, value in enumerate(row):
            df.loc[start_row + row_num, df.columns[col_num]] = value

    # Write to the Excel file
    df.to_excel(excel_file_path, index=False)

# Call the search_files function for each substring
search_files("/GRAV/I_", 30)
search_files("/GRAV/C_", 30)
search_files("/GRAV/VI_", 16)
search_files("/GRAV/VC_", 16)
search_files("/GRAV/DC_", 16)
search_files("/GRAV/DA_", 16)
search_files("/GRAV/CL_", 30)
search_files("/GRAV/CX_", 30)
search_files("/GRAV/CF_", 30)
search_files(".srvdsrv", 30)
search_files("/GRAV/ST_", 30)
