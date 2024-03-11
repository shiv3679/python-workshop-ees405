## This code file gives you a very simple idea of how to do a spatial plot of a climate variable of interest.

# import the libraries 
import numpy as np # for array like operations
import xarray as xr # for loading the netcdf files
import matplotlib.pyplot as plt # for plotting
import cartopy.crs as ccrs # for adding projections    
import cartopy.feature as cfeature # for adding features to the maps
import cartopy as cp 

# import the data file

file = '../../datasets/air.2m.mon.mean.nc'
data = xr.open_dataset(file) ## open the data using xr.open_dataset()
print(data)

data_mean = data.air.mean(dim='time').squeeze()

#read the lat and lons
lat = data.air.lat
lon = data.air.lon


fig = plt.figure(figsize=(15,15)) # you can change the size of the figure here

ax = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree(central_longitude=0.0, globe=None)) # you can change the projection here
mp = ax.imshow(data_mean,extent=(lon.min(),lon.max(),lat.min(),lat.max()),cmap='coolwarm') # you can change the colormap here

states_provinces = cfeature.NaturalEarthFeature(
        category='cultural',
        name='admin_1_states_provinces_lines',
        scale='10m',
        facecolor='none')
# ax.add_feature(cfeature.BORDERS,edgecolor='blue')
# ax.add_feature(states_provinces, edgecolor='blue')

ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.OCEAN)


cbar = fig.colorbar(mp,shrink=0.5,label='A climate variable name')
cbar.minorticks_on()

#adding the long lat grids and enabling the tick labels
gl = ax.gridlines(draw_labels=True,alpha=0.1)
gl.top_labels = False
gl.right_labels = False
plt.title('Some spatial data plot')
plt.show()