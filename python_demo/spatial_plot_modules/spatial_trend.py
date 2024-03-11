# This code provides you with a simple idea of how to do plot a spatial trend analysis and plot the significance of the trend. 

#import the required libraries
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
from scipy import stats
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Load the dataset
file = '../../datasets/air.2m.mon.mean.nc'
data = xr.open_dataset(file)

# For simplicity, we'll work with the air temperature data and squeeze the level dimension if it exists
data_squeezed = data.air.squeeze()

# Assuming time is in a recognizable datetime format; otherwise, convert to numeric
time_numeric = np.arange(len(data_squeezed.time))

# Initialize arrays to hold slope and p-value information
slope = xr.full_like(data_squeezed.isel(time=0), fill_value=0)
p_value = xr.full_like(data_squeezed.isel(time=0), fill_value=1)

# Loop through each pixel to perform linear regression
for lat_idx in range(len(data_squeezed.lat)):
    for lon_idx in range(len(data_squeezed.lon)):
        y = data_squeezed.isel(lat=lat_idx, lon=lon_idx)
        regression_result = stats.linregress(time_numeric, y)
        slope[lat_idx, lon_idx] = regression_result.slope
        p_value[lat_idx, lon_idx] = regression_result.pvalue

# Determine significance based on a threshold (e.g., p < 0.05)
significant = p_value < 0.05

# Plotting
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_global()

# Plot the trend (slope) as background
trend_plot = ax.contourf(data_squeezed.lon, data_squeezed.lat, slope, levels=20, cmap='coolwarm', transform=ccrs.PlateCarree())
cbar = fig.colorbar(trend_plot, shrink=0.5, label='Trend (change per unit time)')
cbar.minorticks_on()

# Highlight significant trends
lon, lat = np.meshgrid(data_squeezed.lon, data_squeezed.lat)
ax.scatter(lon[significant], lat[significant], color='black', s=1, transform=ccrs.PlateCarree())

# Adding map features
ax.add_feature(cfeature.LAND, edgecolor='black')
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')

plt.title('Trend Significance in Air Temperature')
plt.show()
