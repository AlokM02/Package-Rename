# Package-Rename

The steps to rename the package contents are as below. 

1. Extract the package using ABAPGit to a single ZIP file. Ensure to extract as ‘Full’.
2. Unzip the package to the local folder, copy [rename.py](https://github.com/AlokM02/Package-Rename/blob/main/rename.py) to the src folder, and use it. This script will crawl all subfolders and rename the file and its content.
3. Copy [walk.py](https://github.com/AlokM02/Package-Rename/blob/main/walk.py) to the src folder and use it. This script will identify objects which exceed the maximum length set by the ABAP language. 
4. Now copy the generated ‘search_results.xlsx’ to ‘match_data.xlsx’
5. Copy [match.py](https://github.com/AlokM02/Package-Rename/blob/main/match.py) to the src folder and use it.
6. Create two empty columns in ‘match_data.xlsx’ and manually populate them with the shortened names.
7. Open the ‘search_results.xlsx’, copy all lines with SQL database views for the CDS, and copy it to the match_data to include it in the final list. Since the SQL database views will not have its object, we do not need to rename its file separately hence we only need to update the name in the DDL file. 
8. After manual shortening is complete, create two excel files as below. 
    1. The First excel file should have Match and Shortened Match columns.
    2. The second excel file should have the File name and Shortened File name columns. 
9. Copy [replace_string.py](https://github.com/AlokM02/Package-Rename/blob/main/replace_string.py)   to the src folder and use it. It will replace the names in the current folder and all its subfolders.
10. Copy [name_filename.py](https://github.com/AlokM02/Package-Rename/blob/main/name_filename.py)  to the src folder and use it. It will rename the file names in the current folder and all its subfolders.
11. Now remove all python scripts from the src folder and add all the contents to a zip file which can be used to import in the ABAPgit. 
12. Import the zip file 
13. Pull the content 
14. Fix any issues if required.
