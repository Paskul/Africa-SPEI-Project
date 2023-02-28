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
df_groups.columns = ['lat', 'lon', 'spei_mean']

print('------------------------- SPLIT -------------------------')

print(df_groups)