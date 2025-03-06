# Climate-Change-Trends
Overview
This project analyzes global land temperature trends over time using a dataset containing global temperature data for cities around the world. The goal of this analysis is to visualize temperature changes, identify trends, and understand the temperature uncertainty across different countries.

Dataset
The dataset used in this analysis is the GlobalLandTemperaturesByCity.csv file. The dataset contains global land temperature data for different cities, with columns such as:

dt: Date of the temperature record
AverageTemperature: The average temperature for that city on the given date
AverageTemperatureUncertainty: The uncertainty associated with the temperature record
City: The city where the temperature was recorded
Country: The country of the city
Requirements
Libraries
The following Python libraries are used in this project:

numpy: For numerical operations
pandas: For data manipulation and analysis
matplotlib: For data visualization
seaborn: For advanced data visualization
Installation
Make sure you have Python installed (preferably Python 3.x). You can install the required libraries using pip:

bash
Copy
pip install numpy pandas matplotlib seaborn
Dataset
The dataset can be downloaded from the following location:

Global Land Temperatures by City Dataset: Kaggle Dataset
Ensure that the dataset is placed in the correct location on your system. Update the file path in the code accordingly.

Project Structure
The project consists of a single Python script for analysis and visualization:

GlobalLandTemperaturesByCity.csv: The dataset file.
ClimateChangeTrends.py: The Python script that performs data analysis and visualization.
Steps to Run the Code
Download the dataset: Download the GlobalLandTemperaturesByCity.csv dataset and place it in a local directory on your system.

Run the Python script: Run the Python script to load the dataset, perform data analysis, and generate plots.

The following steps are performed in the script:

Loading the Dataset: The dataset is loaded using pd.read_csv().
Data Preprocessing:
Dropping rows with missing values.
Checking for duplicates.
Identifying numerical and categorical columns.
Converting the dt column (date) to a datetime format.
Data Visualization:
Plotting the average temperature over time.
Scatter plot for temperature uncertainty.
Creating line plots and box plots for better insights into the data.
Visualizations:

Average Temperature Plot: A line plot showing how the average temperature has changed over time.
Temperature Uncertainty Plot: A scatter plot of temperature uncertainty over time.
Boxplot: A box plot showing the temperature distribution across different countries.
