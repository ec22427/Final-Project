import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_clean_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Clean the data (handle missing values, convert data types)
    df['sales'] = pd.to_numeric(df['sales'].str.replace(',', ''), errors='coerce')

    return df

def display_basic_info(dataframe):
    # Display basic information about the dataset
    print(dataframe.info())
    print(dataframe.head())  # Display the first few rows of the DataFrame
    print(dataframe['sales'].unique())  # Check unique values in the 'sales' column
    print(dataframe['peak_chart'].unique())  # Check unique values in the 'peak_chart' column

def visualise_peak_chart(dataframe):
    # Visualise distribution of peak chart positions
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Artist', y='peak_chart', data=dataframe, palette='husl')
    plt.title('Distribution of Peak Chart Positions by Artist')
    plt.xlabel('Artist')
    plt.ylabel('Peak Chart Position')
    plt.xticks(rotation=90)
    plt.show()

def calculate_and_visualise_total_sales(dataframe):
    # Filter only 'JPN' and 'KOR' countries
    dataframe = dataframe[dataframe['country'].isin(['JPN', 'KOR'])]

    # Calculate total sales for each artist
    total_sales = dataframe.groupby(['Artist', 'country'])['sales'].sum().reset_index()

    # Set up separate plots for each graph
    fig, axes = plt.subplots(3, 1, figsize=(15, 18))

    # Visualise distribution of peak chart positions
    sns.boxplot(x='Artist', y='peak_chart', data=dataframe, ax=axes[0], palette='husl')
    axes[0].set_title('Distribution of Peak Chart Positions by Artist')
    axes[0].set_xlabel('Artist')
    axes[0].set_ylabel('Peak Chart Position')
    axes[0].tick_params(axis='x', rotation=90)

    # Box plot for total sales comparison
    sns.boxplot(x='Artist', y='sales', data=total_sales, hue='country', ax=axes[1], palette='magma', showfliers=False)
    axes[1].set_title('Sales Comparison (Box Plot)')
    axes[1].set_xlabel('Artist')
    axes[1].set_ylabel('Total Sales')
    axes[1].legend(title='Country')
    axes[1].tick_params(axis='x', rotation=90)

    # Bar plot for total sales for each group
    total_sales_general = dataframe.groupby('Artist')['sales'].sum().reset_index()
    sns.barplot(x='Artist', y='sales', data=total_sales_general, ax=axes[2], palette='viridis')
    axes[2].set_title('Total Sales for Each Group')
    axes[2].set_xlabel('Artist')
    axes[2].set_ylabel('Total Sales')
    axes[2].tick_params(axis='x', rotation=90)

    # Adjust layout
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Specify the file path
    file_path = "Kpop 4th gen Sales - Sheet1.csv"

    # Load and clean the data
    df = load_and_clean_data(file_path)

    # Display basic information about the dataset
    display_basic_info(df)

    # Visualise distribution of peak chart positions
    visualise_peak_chart(df)

    # Calculate and visualise total sales
    calculate_and_visualise_total_sales(df)
