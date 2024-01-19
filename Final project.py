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
    plt.show()

def calculate_and_visualise_total_sales(dataframe):
    # Calculate total sales for each artist
    total_sales = dataframe.groupby('Artist')['sales'].sum().reset_index()

    # Visualise sales comparison
    plt.figure(figsize=(15, 6))
    sns.barplot(x='Artist', y='sales', data=total_sales, palette='magma')
    plt.title('Total Sales Comparison by Artist')
    plt.xlabel('Artist')
    plt.ylabel('Total Sales')
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
