import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_gdp_plot(input_path, output_path):
    """
    Generates a line plot comparing GDP per capita over time for different countries.

    Args:
        input_path (str): The path to the processed CSV file.
        output_path (str): The path to save the generated plot.
    """
    df = pd.read_csv(input_path)

    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 8))

    for country in df['Country Name'].unique():
        country_df = df[df['Country Name'] == country]
        ax.plot(country_df['Year'], country_df['GDP_per_capita_PPP'], label=country)

    ax.set_title('GDP Per Capita (PPP) Comparison', fontsize=16)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('GDP Per Capita (constant 2021 international $)', fontsize=12)
    ax.legend()
    ax.grid(True)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    print(f"Plot saved to {output_path}")

if __name__ == '__main__':
    processed_data_path = 'data/processed/gdp_per_capita_ppp_processed.csv'
    plot_path = 'reports/figures/gdp_per_capita_comparison.png'
    generate_gdp_plot(processed_data_path, plot_path) 