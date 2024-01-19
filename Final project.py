import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def load_and_clean_data(df):
    # Convert the 'sales' column to numeric, as it seems to contain some commas
    df['sales'] = pd.to_numeric(df['sales'].str.replace(',', ''), errors='coerce')
    return df

def plot_peak_chart_bar(df):
    # Group by artist and aggregate total sales and peak chart position
    artist_stats = df.groupby('Artist').agg({'sales': 'sum', 'peak_chart': 'mean'}).reset_index()

    # Create a bar graph in magenta
    plt.figure(figsize=(14, 6))
    sns.barplot(x='Artist', y='peak_chart', data=artist_stats, color='magenta')
    plt.title('Bar Graph of Average Peak Chart Position by Artist')
    plt.xlabel('Artist')
    plt.ylabel('Average Peak Chart Position')
    plt.xticks(rotation=90)
    plt.show()

def plot_sales_by_country_bar(df):
    # Group by artist and sum the sales in Japan and Korea separately
    sales_by_country = df.groupby(['Artist', 'country'])['sales'].sum().unstack().reset_index()

    # Create a bar graph
    plt.figure(figsize=(14, 6))
    sns.barplot(x='Artist', y='KOR', data=sales_by_country, color='violet', label='Korea')
    sns.barplot(x='Artist', y='JPN', data=sales_by_country, color='cyan', label='Japan')
    plt.title('Sales in Korea and Japan by Artist')
    plt.xlabel('Artist')
    plt.ylabel('Total Sales')
    plt.legend()
    plt.xticks(rotation=90)
    plt.show()

def plot_total_sales_with_fit_line(df):
    # Group by artist and sum the sales
    total_sales_by_artist = df.groupby('Artist')['sales'].sum().reset_index()

    # Create a scatter plot with a line of best fit
    plt.figure(figsize=(14, 6))
    sns.regplot(x=total_sales_by_artist.index, y='sales', data=total_sales_by_artist, ci=None, line_kws={"color": "red"})
    plt.title('Total Sales with Line of Best Fit by Artist')
    plt.xlabel('Artist Index')  # Change the x-axis label as per your preference
    plt.ylabel('Total Sales (in thousands)')

    # Format y-axis ticks to show values in thousands
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: '{:.0f}K'.format(x/1000)))

    plt.show()

# Load and clean the data
df = pd.read_csv('Kpop 4th gen Sales - Sheet1.csv')  
df = load_and_clean_data(df)

# Call each method to plot the graphs
plot_peak_chart_bar(df)
plot_sales_by_country_bar(df)
plot_total_sales_with_fit_line(df)
