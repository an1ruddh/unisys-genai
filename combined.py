import pandas as pd
# Merge the two DataFrames based on the "Filename" column"

models_df = pd.read_csv("elements_dataset.csv")
elements_df = pd.read_csv("models_dataset.csv")
combined_df = pd.merge(models_df, elements_df, on="Filename", how="outer")
# Ensure 'Filename' column is consistent across DataFrames
labels_data= pd.read_csv("lables_dataset.csv")

# Merge the combined DataFrame with the labels DataFrame based on 'Filename'
combined_with_labels_df = pd.merge(combined_df, labels_data, on='Filename', how='left')

# Display first few rows of the merged DataFrame


# Display the first few rows of the combined DataFrame

#print(models_df.info())
#print(elements_df.info())
# Save the combined DataFrame to a new CSV file
combined_df.to_csv("combined_dataset.csv", index=False)  # Replace "combined_dataset.csv" with the desired filename
