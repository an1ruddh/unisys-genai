import pandas as pd

# Load label data from Excel files
labels_folder_path = "labels\labels/"
excel_files = ["Duplex_a.xlsx", "rac_basic.xlsx", "rst_advanced.xlsx", "rst_basic.xlsx", "tech_school.xlsx"]

dfs_labels = []
for file in excel_files:
    df = pd.read_excel(labels_folder_path + file)
    
    dfs_labels.append(df)


# Concatenate DataFrames
labels_data = pd.concat(dfs_labels, ignore_index=True,keys=None)
labels_data['Filename'] = labels_data['Filename'].fillna(labels_data['Filenam'])
labels_data.drop(columns=['Filenam'], inplace=True)
labels_data.to_csv("lables_dataset.csv", index=False)
# Display first few rows of label data
print(labels_data.info())
