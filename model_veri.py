import pandas as pd

# Load the data from JSON file
data = pd.read_json('evler_analizi_model.json')

# Data Preprocessing
# Convert string values to numerical values and handle missing data
data['Net Metrekare'] = data['Net Metrekare'].str.extract('(\d+)').astype(float)
data['price'] = data['price'].str.replace(',', '').astype(float)

# Save the preprocessed data to a CSV file
data.to_csv('preprocessed_evler.csv', index=False)
