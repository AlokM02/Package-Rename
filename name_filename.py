import os
import pandas as pd

# read in the mapping of file names to shortened file names
df = pd.read_excel('file_rename.xlsx')

# loop through all files in current directory and its subdirectories
for root, dirs, files in os.walk('.'):
    for filename in files:
        # check if the filename contains any substring from the 'File Name' column
        for file_name in df['File Name']:
            if file_name.lower() in filename.lower():
                # replace the matching substring with the 'Shortened File Name' value
                shortened_name = df.loc[df['File Name'] == file_name, 'Shortened File Name'].values[0]
                new_filename = filename.lower().replace(file_name.lower(), shortened_name)
                # rename the file with the new filename
                os.rename(os.path.join(root, filename), os.path.join(root, new_filename))
                print(f"Renamed {os.path.join(root, filename)} to {new_filename}")
                break
