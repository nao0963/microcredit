import pandas as pd
import os

def process_gdp_data(input_path, output_path):
    """
    Processes the raw GDP data from the World Bank.

    Args:
        input_path (str): The path to the raw CSV file.
        output_path (str): The path to save the processed CSV file.
    """
    df = pd.read_csv(input_path, skiprows=4)

    df = df.drop(columns=['Indicator Name', 'Indicator Code', 'Country Code'])

    df_melted = df.melt(id_vars=['Country Name'], var_name='Year', value_name='GDP_per_capita_PPP')

    df_melted.dropna(subset=['GDP_per_capita_PPP'], inplace=True)

    df_melted['Year'] = pd.to_numeric(df_melted['Year'], errors='coerce')
    df_melted.dropna(subset=['Year'], inplace=True)
    df_melted['Year'] = df_melted['Year'].astype(int)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_melted.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")

if __name__ == '__main__':
    raw_data_path = 'data/raw/gdp_per_capita_ppp.csv'
    processed_data_path = 'data/processed/gdp_per_capita_ppp_processed.csv'
    process_gdp_data(raw_data_path, processed_data_path) 