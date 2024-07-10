import xml.etree.ElementTree as ET
import pandas as pd

# Load the XML file
file_path = '/SAEcon/data/Data.xml'
tree = ET.parse(file_path)
root = tree.getroot()

# Initialize an empty list to store the data
data = []

# Print the root element and its children to understand the structure
print("Root element:", root.tag)
for child in root:
    print("Child element:", child.tag, child.attrib)

# Iterate through each record in the XML
for record in root.findall('.//record'):  # Using .// to ensure it finds records at any depth
    record_data = {}
    print("Record:", ET.tostring(record, encoding='unicode'))  # Debugging statement to print the entire record
    for field in record:
        field_name = field.get('name')
        field_value = field.text
        print(f"Field name: {field_name}, Field value: {field_value}")  # Debugging statement
        if field_name:
            record_data[field_name] = field_value
    data.append(record_data)

# Check if any data was extracted
if not data:
    print("No data extracted from XML.")
else:
    # Convert the list of dictionaries to a Pandas DataFrame
    df = pd.DataFrame(data)

    # Debug: Print the first few rows and column names
    print("DataFrame head:\n", df.head())
    print("DataFrame columns:\n", df.columns)

    # Ensure the 'Year' column exists and filter the data
    if 'Year' in df.columns:
        # Convert the 'Year' column to numeric
        df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
        
        # Filter out rows where the year is prior to 1985
        df_filtered = df[df['Year'] >= 1985]
        
        # Filter out rows where 'Value' is None
        df_filtered = df_filtered.dropna(subset=['Value'])

        # Check if any data is left after filtering
        if df_filtered.empty:
            print("No data available after filtering for Year >= 1985 and non-null 'Value'.")
        else:
            # Save the filtered data to a new CSV file
            output_path = '/SAEcon/data/filtered_data.csv'
            df_filtered.to_csv(output_path, index=False)
            print(f"Filtered data has been saved to {output_path}")

        # Print the final filtered DataFrame for verification
        print("Filtered DataFrame head:\n", df_filtered.head())
    else:
        print("Error: 'Year' column not found in the data.")
