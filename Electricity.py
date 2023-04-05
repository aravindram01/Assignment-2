# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:16:30 2023

@author: aravind
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read in the CSV file and convert to a DataFrame
df = pd.read_csv('Elect1.csv', index_col=0)
print(df)

#Transpose Data
df_t = pd.DataFrame.transpose(df)
print(df_t)

# use .describe() method to generate summary statistics
summary = df.describe()

# print summary statistics
print(summary)


#Line Plot - Function Starts from here
def plot_power_consumptions_per_capita(data_file: str) -> None:
    """
    Plots Energy power consumption per capita using a line plot.

    data_file (str): Name or path of the CSV file containing the data

    Displays the line plot
    """
# Create a figure with one subplot
fig, ax = plt.subplots(figsize=(15, 5))

# Loop through each country and create a line plot for Energy Consumption
# select data for the 5 countries
for country in df.index:
    data = df.loc[country][2:]
    ax.plot(data.index, data, label=country)
    
# Add labels and a title to the plot
ax.set_xlabel('Year')
ax.set_ylabel('kWh Per Capita')
ax.set_title('Electric Power Consumption')

# Add a legend to the plot
ax.legend()
#Line Plot - Function Ends here

# Display the plot
plt.show()