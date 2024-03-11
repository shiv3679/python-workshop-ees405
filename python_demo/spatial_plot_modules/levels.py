## This code file gives you a very simple idea of how to do a spatial plot of a climate variable of interest.

# import the libraries 
import numpy as np # for array like operations
import xarray as xr # for loading the netcdf files
import matplotlib.pyplot as plt # for plotting
import cartopy.crs as ccrs # for adding projections    
import cartopy.feature as cfeature # for adding features to the maps
import cartopy as cp 

# load the data 
data_3d = xr.open_dataset('../../datasets/air.mon.ltm.nc')
print(data_3d)

# reducing the dimensionality of the data
data_3d_mean = data_3d.air.mean(dim=['lat','lon','time']).squeeze()

# plot the levels data 
plt.plot(data_3d_mean, data_3d_mean.level, marker='o', linestyle='--', color='red')
plt.ylim(max(data_3d_mean.level), min(data_3d_mean.level)) # y-limits revered to make it look similar to literature plots
plt.xlabel('Air Temperature (°K)')
plt.ylabel('Pressure (hPa)')
plt.grid(True)
plt.xticks(rotation=45)
plt.title('Vertical Thermal Structure over globe')
plt.show()