import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
import geoplot as gplt
import geoplot.crs as gcrs
import pyreadr
from shapely.geometry import Point, Polygon

africaShape = gpd.read_file('C:/Users/pasca/Desktop/Research/Step2/afr_g2014_2013_0.shp')

#fig,ax = plt.subplots(figsize = (15,15))
#map = africaShape.plot(ax = ax)
#plt.show()

data = pyreadr.read_r('C:/Users/pasca/Desktop/Research/Step2/Pascal_data.rds') # also works for RData
data = data[None]

#data['time'] = pd.to_datetime(data['time'])
#data.set_index('time', inplace=True)
#data = data['1948':'1960']

#print('----BEFORE')
#for col_name in data.columns: 
    #print(col_name)
#data.columns = ['lon', 'lat', 'spei_mean']
data = data.drop(columns=['shape_id', 'ADM0_CODE', 'ADM0_NAME', 'CONTINENT', 'ISO3',
       'ISO2', 'UNI', 'UNDP', 'FAOSTAT', 'GAUL', 'RIC_ISO3', 'REC_ISO3', 'AFR',
       'CEMAC', 'CILSS', 'CRA', 'ECOWAS', 'IGAD', 'IOC', 'SADC', 'CICOS',
       'ICPAC', 'BDMS', 'MOI'])
#print('----AFTER')
#for col_name in data.columns: 
    #print(col_name)
#print(data.head())

'''
data = pyreadr.read_r('C:/Users/pasca/Desktop/Research/Step2/Pascal_data.rds') # also works for RData
df = data[None]

df['time'] = pd.to_datetime(df['time'])
df.set_index('time', inplace=True)
df = df['1948':'1960']
print(df)
'''


# create a new DataFrame with unique lat and lon values
#unique_data = data[['lat', 'lon']].drop_duplicates().reset_index(drop=True)
unique_data = data[['lat', 'lon']].drop_duplicates()


# loop over the unique lat and lon values and calculate the average spei value for each point
for index, row in unique_data.iterrows():
    lon = row['lon']
    lat = row['lat']
    spei_average = data.loc[(data['lon'] == lon) & (data['lat'] == lat), 'spei'].mean()
    unique_data.at[index, 'spei'] = spei_average

print(unique_data)

#crs="EPSG:4326"
#crs = {'init':'espc:4326'}
geometry = [Point(xy) for xy in zip(unique_data['lon'], unique_data['lat'])]
geo_df = gpd.GeoDataFrame(unique_data, crs = "EPSG:4326", geometry = geometry)

# create figure and axes, assign to subplot
fig, ax = plt.subplots(figsize=(15,15))
# add .shp mapfile to axes
africaShape.plot(ax=ax, alpha=0.4,color='grey')
# add geodataframe to axes
# assign ‘price’ variable to represent coordinates on graph
# add legend
# make datapoints transparent using alpha
# assign size of points using markersize
geo_df.plot(column='spei',ax=ax,alpha=0.5, legend=True,markersize=10)
# add title to graph
plt.title('Average SPEI Africa', fontsize=15,fontweight='bold')
# set latitiude and longitude boundaries for map display
plt.xlim(-20,55)
plt.ylim(-40,40)
# show map
plt.show()

#http://www.loicdutrieux.net/pyLandsat/modisPreProcess.html