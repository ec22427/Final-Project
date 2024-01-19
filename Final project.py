import pandas as pd

# Load the dataset
df = pd.read_csv("Kpop 4th gen Sales - Sheet1.csv")

# Clean the data (handle missing values, convert data types)
df['sales'] = pd.to_numeric(df['sales'].str.replace(',', ''), errors='coerce')

# Display basic information about the dataset
print(df.info())

