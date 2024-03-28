import ifcopenshell
import os
import pandas as pd

# Directory containing IFC files
ifc_directory = "Ifc Models\Ifc Models/"

# List to store information from all IFC files
all_elements = []

# Loop through each IFC file in the directory
for filename in os.listdir(ifc_directory):
    if filename.endswith(".ifc"):
        # Load IFC file
        ifc_file_path = os.path.join(ifc_directory, filename)
        ifc_file = ifcopenshell.open(ifc_file_path)

        # Extract building elements from IFC file
        elements = ifc_file.by_type("IfcBuildingElement")
        for element in elements:
            # Process each building element and extract relevant information
            # For example, you can extract properties like element type, dimensions, etc.
            element_info = {
                "Filename": filename,
                "ElementID": element.id(),
                "ElementType": element.is_a(),
                # Add more properties as needed
            }
            # Extract all properties of the element
            properties = {}
            for attr_name in element.get_info().keys():
                # Check if the attribute exists for the entity
                if hasattr(element, attr_name):
                    attr_value = getattr(element, attr_name)
                    # Check if the attribute is a nested entity
                    if hasattr(attr_value, 'is_a'):
                        properties[attr_name] = attr_value.is_a()
                    # Check if the attribute is a list of nested entities
                    elif isinstance(attr_value, list) and all(hasattr(item, 'is_a') for item in attr_value):
                        properties[attr_name] = [item.is_a() for item in attr_value]
                    else:
                        properties[attr_name] = attr_value
            element_info.update(properties)
            all_elements.append(element_info)

# Convert list of dictionaries to DataFrame
models_df = pd.DataFrame(all_elements)
models_df.to_csv("models_dataset.csv", index=False)
# Display first few rows of the DataFrame
print(models_df.info())
