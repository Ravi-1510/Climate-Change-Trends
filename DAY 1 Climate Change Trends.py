import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv(r"C:\Users\ravid\OneDrive\Desktop\INDOLIKE INTERNSHIP\DAY 1\GlobalLandTemperaturesByCity.csv\GlobalLandTemperaturesByCity.csv")

# Print the dataset to verify
print(data)  # print all the data
print("*" * 100)
print(data.head())  # print top 5
print("*" * 100)
print(data.tail())  # print bottom 5
print("*" * 100)
print(data.info())  # Check data types, non-null values
print("*" * 100)
print(data.isnull().sum())  # Check for missing values
print("*" * 100)
data.dropna(inplace=True)  # Drop rows with missing values
print(data.duplicated().sum())  # Check for duplicates
print("*" * 100)

# Identify numerical and categorical columns
numerical_cols = data.select_dtypes(include='number').columns.tolist()
categorical_cols = data.select_dtypes(include='object').columns.tolist()
print(f"Categorical columns: {categorical_cols}")
print(f"Numerical columns: {numerical_cols}")

# Convert 'dt' column to datetime format
data['dt'] = pd.to_datetime(data['dt'])

# Plot the Average Temperature over time
data.plot(x='dt', y='AverageTemperature')
plt.title('Average Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Average Temperature')
plt.show()

# Scatter plot of Average Temperature Uncertainty over time
plt.figure(figsize=(15, 6))
plt.scatter(data['dt'], data['AverageTemperatureUncertainty'])
plt.title('Temperature Uncertainty Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature Uncertainty')
plt.show()

# Set 'dt' as the index for time-series analysis
data = data.set_index('dt')
print(data.head())

# Create a new DataFrame with the 'AverageTemperature' column and take a sample
df = data['AverageTemperature'].to_frame()
df = df.sample(frac=0.5, random_state=42)
print(df.head())

# Line plot of 'AverageTemperature' over time
plt.figure(figsize=(15, 6))
sns.lineplot(data=data, x=data.index, y='AverageTemperature')
plt.title('Average Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Average Temperature')
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x='Country', y='AverageTemperature', data=data)
plt.xticks(rotation=90)
plt.title('Temperature Distribution by Country')
plt.tight_layout()