import pandas as pd
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
import geoplot 
import pyreadr
from shapely.geometry import Point, Polygon

africaShape = gpd.read_file('C:/Users/pasca/Desktop/Research/Step2/afr_g2014_2013_0.shp')

#africa = world.query('continent == "Africa"')

fig,ax = plt.subplots(figsize = (15,15))
map = africaShape.plot(ax = ax)
plt.show()

data = pyreadr.read_r('C:/Users/pasca/Desktop/Research/Step2/Pascal_data.rds') # also works for RData
df = data[None] # extract the pandas data frame
print(df.info())
df['time'] = pd.to_datetime(df['time'])
df.set_index('time', inplace=True)
df_1948_1960 = df['1948':'1960']
print(df_1948_1960.head())
print(df_1948_1960.info())
#df_groups = df.groupby(['lat', 'lon'])
#print(df_1948_1960.head(10))
print('df_1948_1960 break --------')
#df_groups_1948_1960 = df_1948_1960.groupby(['lat', 'lon']).mean()
#df_groups_1948_1960 = df_1948_1960.groupby(['lat', 'lon'], as_index=True)['spei'].mean()
df_groups_1948_1960 = df_1948_1960.groupby(['lat','lon'])['spei'].mean()
print(df_groups_1948_1960.info())
#doesnt work I don't think

print(df_groups_1948_1960.head())
print('df_1948_1960 groups break --------')

    #print(df)
#geometry = [Point(xy) for xy in zip(df_groups_1948_1960['lon'], df_groups_1948_1960['lat'])]
#geometry = [Point(xy) for xy in zip(df['lon'], df['lat'])]
    #maybe look at crs if doesnt work
#geo_df = gpd.GeoDataFrame(df_groups_1948_1960, geometry = geometry)
#geo_df = gpd.GeoDataFrame(df, geometry = geometry)
    #print(geo_df)
#print('geo_df break ----------')
#print(geo_df.head(10))
#print(geo_df.head(10))

#ax = geoplot.kdeplot(
    #df_groups_1948_1960, clip=africaShape,
    #shade=True, cmap='Reds',
    #projection=geoplot.crs.AlbersEqualArea())

#geoplot.polyplot(africaShape, ax=ax, zorder=1)
#fig.show()





#TO-DO need to get geoplot working somehow, then plot everything based on heatmap
#https://geopandas.org/en/stable/gallery/plotting_with_geoplot.html
#is probs a good link to do so
#surface maps, heatmaps
#https://towardsdatascience.com/geopandas-101-plot-any-data-with-a-latitude-and-longitude-on-a-map-98e01944b972

#sort lon-lat
#look up summarize points in df with same lon-lat