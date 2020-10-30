# Load Libraries

import pandas as pd
import scipy.stats
import matplotlib.pyplot as plt
import numpy as np
import random as random


#Load in data to a pandas data frame
raw_data = pd.read_csv('/Users/brianbeeler/Downloads/exo_data.csv')


# Create a histogram of showing the frequncy of amount of suns in a solar system
raw_data.hist(column="sy_snum")

# Create a historam showing the frequency of different numbers of planets in solar systems
raw_data.hist(column='sy_pnum')

#Show a sctter of the number of suns and the number of planets
raw_data.plot.scatter(x='sy_snum', y='sy_pnum')

# Compare the lengs of the data tables
x_shape = raw_data.sy_snum.shape
y_shape = raw_data.sy_pnum.shape

# Jitter creation for the raw data plot
x_jitter = scipy.stats.norm().rvs(x_shape)/ 10
y_jitter = scipy.stats.norm().rvs(y_shape) / 10 

# Plot the data 
fig, ax = plt.subplots(figsize=(10,10))
ax.scatter(raw_data.sy_snum + x_jitter, raw_data.sy_pnum + y_jitter, alpha=0.1, s=1)