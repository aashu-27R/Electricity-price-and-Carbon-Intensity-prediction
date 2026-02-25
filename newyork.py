import pandas as pd
import os

# Define the folder path for New York electricity prices
newyork_price_folder = '/Users/aashrithasankineni/Downloads/newyork_electricity_prices'

# Initialize a list to hold each file's data
newyork_price_dfs = []

# Load each CSV file in the newyork_electricity_prices folder
if os.path.exists(newyork_price_folder):
    for filename in os.listdir(newyork_price_folder):
        if filename.endswith('.csv'):
            file_path = os.path.join(newyork_price_folder, filename)
            newyork_price_dfs.append(pd.read_csv(file_path, delimiter=',', on_bad_lines='skip'))
            print(f"Loaded data from {filename}")
else:
    print(f"Folder not found: {newyork_price_folder}")

# Concatenate all dataframes if any files were loaded
if newyork_price_dfs:
    newyork_price_df = pd.concat(newyork_price_dfs, ignore_index=True)
    print("Combined New York Electricity Prices Data:\n", newyork_price_df.head())
else:
    print("No New York electricity prices data loaded.")
