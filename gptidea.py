import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
import geoplot 
import pyreadr
from shapely.geometry import Point, Polygon

data = pyreadr.read_r('C:/Users/pasca/Desktop/Research/Step2/Pascal_data.rds') # also works for RData
data = data[None]

# Group the data by lon and lat, and calculate the mean spei_mean for each group
#                 grouped_data = data.groupby(['lon', 'lat']).mean().reset_index()

# Extract x, y, and z data from the grouped dataframe
x = data['lon']
y = data['lat']
z = data['spei']

# Determine number of unique x and y values
n_x = len(np.unique(x))
n_y = len(np.unique(y))

# Ensure that x and y have the same length
if n_x != n_y:
    raise ValueError('x and y arrays must have the same length')

# Determine grid size
grid_size = n_x, n_y

# Create meshgrid of x and y values
X, Y = np.meshgrid(np.unique(x), np.unique(y))

# Create empty grid for z values
Z = np.empty(grid_size)

# Fill in z values at corresponding x and y coordinates
for i, xi in enumerate(np.unique(x)):
    for j, yj in enumerate(np.unique(y)):
        Z[j, i] = np.mean(z[(x == xi) & (y == yj)]) # use np.mean() to get the average value of z

# Create contour line plot
plt.contour(X, Y, Z)

# Add labels and title
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Contour Line Plot of SPEI Mean')

# Display the plot
plt.show()