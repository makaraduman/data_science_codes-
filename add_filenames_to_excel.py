import os
import pandas as pd

folder_path = "path/to/folder"

# Create a list to store the file names
file_names = []
for filename in os.listdir(folder_path):
    file_names.append(filename)

# Create a pandas dataframe with the file names
df = pd.DataFrame({'File Name': file_names})

# Write the dataframe to an Excel file
df.to_excel("file_names.xlsx", index=False)
