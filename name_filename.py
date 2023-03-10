import os
import pandas as pd

# Load the dataset into a pandas dataframe
df = pd.read_excel('your_dataset_file_name.xlsx')

# Iterate through all the files in the current directory and its subdirectories
for root, dirs, files in os.walk("."):
    for filename in files:
        # Check if the file name contains any of the strings from the 'File Name' column in the dataset, ignoring case
        for file_str in df['File Name']:
            if file_str.lower() in filename.lower():
                # Replace the matched part of the file name with the corresponding string from the 'Shortened File Name' column
                new_filename = filename.lower().replace(file_str.lower(), df[df['File Name'].str.lower()==file_str.lower()]['Shortened File Name'].values[0])
                # Restore the original case of the filename
                new_filename = filename[:filename.lower().find(file_str.lower())] + new_filename + filename[filename.lower().find(file_str.lower())+len(file_str):]
                # Rename the file
                os.rename(os.path.join(root, filename), os.path.join(root, new_filename))
                print(f"Renamed {filename} to {new_filename}")
