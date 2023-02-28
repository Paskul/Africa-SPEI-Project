import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
import geoplot 
import pyreadr
from shapely.geometry import Point, Polygon

africaShape = gpd.read_file('C:/Users/pasca/Desktop/Research/Step2/afr_g2014_2013_0.shp')

#fig,ax = plt.subplots(figsize = (15,15))
#map = africaShape.plot(ax = ax)
#plt.show()

data = pyreadr.read_r('C:/Users/pasca/Desktop/Research/Step2/Pascal_data.rds') # also works for RData
df = data[None]

df['time'] = pd.to_datetime(df['time'])
df.set_index('time', inplace=True)
df = df['1948':'1960']
print(df)

#df_groups = df.groupby(['lat', 'lon'])['spei'].mean()
df_groups = df.groupby([df['lat'], df['lon']])['spei'].mean().reset_index()
df_groups.columns = ['lon', 'lat', 'spei_mean']

print('------------------------- SPLIT -------------------------')

#plt.scatter(x=df_groups['lon'], y=df_groups['lat'])]
#plt.contour([df_groups['lon'], df_groups['lat']], z=df_groups['spei_mean'])
print('lon', len(df_groups['lon']))
print('lat', len(df_groups['lat']))
print('spei_mean', len(df_groups['spei_mean']))

#X, Y = np.meshgrid(df_groups['lon'], df_groups['lat'])

#Z = np.reshape(df_groups['spei_mean'], (len(set(df_groups['lon'])), len(set(df_groups['lat']))))


#plt.contour(x=df_groups['lon'], y=df_groups['lat'], z=df_groups['spei_mean'])

#fig,ax = plt.subplots(figsize = (60,60))
#map = africaShape.contour(x=df_groups['lon'], y=df_groups['lat'], z=df_groups['spei_mean'])

#-------------------



# Extract x, y, and z data from dataframe
x = df_groups['lon']
y = df_groups['lat']
z = df_groups['spei_mean']

# Create a meshgrid of x and y values
X, Y = np.meshgrid(np.sort(x.unique()), np.sort(y.unique()))

# Reshape z values to match meshgrid dimensions
Z = np.reshape(z, (len(np.unique(y)), len(np.unique(x))))

# Create contour line plot
plt.contour(X, Y, Z)

# Add labels and title
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Contour Line Plot of SPEI Mean')

# Display the plot
plt.show()