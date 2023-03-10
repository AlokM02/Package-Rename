import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel('match_data.xlsx')

# Create a new column called "Enriched File Name" and copy the contents of "File Name" into it
df["Enriched File Name"] = df["File Name"]

# Replace all instances of "#" with "/" in the "Enriched File Name" column
df["Enriched File Name"] = df["Enriched File Name"].str.replace("#", "/")

# Check if the "Match" string is in the "Enriched File Name" string (ignoring case)
df["Match?"] = df.apply(lambda row: row["Match"].lower() in row["Enriched File Name"].lower(), axis=1)

# Filter the DataFrame to show only the rows where "Match?" is True
output_df = df[df["Match?"]]

# Drop the "Match?" column since we no longer need it
output_df = output_df.drop("Match?", axis=1)

# Filter the remaining rows to show only those where "Enriched File Name" ends with ".xml" or ".abap"
output_df = output_df[output_df["Enriched File Name"].str.endswith((".asddls", ".abap", ".srvdsrv", ".tabl.xml"))]

# Keep only the data in the "File Name" column which is before the first "."
output_df["File Name"] = output_df["File Name"].str.split(".", expand=True)[0]

# Drop any duplicate rows based on the "Match" column
output_df.drop_duplicates(subset=["Match"], keep="first", inplace=True)

# Overwrite the original Excel file with the updated DataFrame
output_df.to_excel('match_data.xlsx', index=False)

print("Excel file updated!")
