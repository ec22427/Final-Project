import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Kpop 4th gen Sales - Sheet1.csv")

# Clean the data (handle missing values, convert data types)
df['sales'] = pd.to_numeric(df['sales'].str.replace(',', ''), errors='coerce')

# Display basic information about the dataset
print(df.info())

print(df.head())  # Display the first few rows of the DataFrame
print(df['sales'].unique())  # Check unique values in the 'sales' column
print(df['peak_chart'].unique())  # Check unique values in the 'peak_chart' column

# Visualize distribution of peak chart positions
plt.figure(figsize=(12, 6))
sns.boxplot(x='Artist', y='peak_chart', data=df , palette='husl')
plt.title('Distribution of Peak Chart Positions by Artist')
plt.xlabel('Artist')
plt.ylabel('Peak Chart Position')
plt.show()

# Calculate total sales for each artist
total_sales = df.groupby('Artist')['sales'].sum().reset_index()

# Visualize sales comparison
plt.figure(figsize=(15, 6))
sns.barplot(x='Artist', y='sales', data=total_sales, palette='magma')
plt.title('Total Sales Comparison by Artist')
plt.xlabel('Artist')
plt.ylabel('Total Sales')
plt.show()



