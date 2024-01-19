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



