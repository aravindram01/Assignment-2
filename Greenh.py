# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 23:56:28 2023

@author: aravind
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# Read in the CSV file and convert to a DataFrame
df = pd.read_csv('Green.csv', index_col=0)

# Calculate skewness and kurtosis for each column
skewness = df.apply(lambda x: skew(x))
kurtosis = df.apply(lambda x: kurtosis(x))

# Plot the results
fig, ax = plt.subplots(figsize=(8, 6))

ax.bar(skewness.index, skewness.values, label='Skewness')
ax.bar(kurtosis.index, kurtosis.values, label='Kurtosis')

ax.set_xlabel('Country')
ax.set_ylabel('Value')
ax.set_title('Skewness and Kurtosis of Greenhouse Gas Data')
ax.legend()

plt.show()
