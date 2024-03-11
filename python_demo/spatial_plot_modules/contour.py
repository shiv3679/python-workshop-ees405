# This code provides you with a simple idea of how to do a contour plot of a climate variable of interest.

#import the required libraries
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Load the dataset
file = '../../datasets/air.2m.mon.mean.nc'
data = xr.open_dataset(file)

# Average out the time and level dimensions
data_mean = data.air.mean(dim=['time', 'level'])

# Setup the plot with Cartopy
fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

# Contour plot
contour_plot = ax.contourf(data_mean.lon, data_mean.lat, data_mean, levels=15, cmap='coolwarm', transform=ccrs.PlateCarree())

# Adding map features for better visualization
ax.add_feature(cfeature.LAND, edgecolor='black')
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.OCEAN)
# ax.add_feature(cfeature.BORDERS, linestyle=':')
# ax.add_feature(cfeature.LAKES, alpha=0.5)
# ax.add_feature(cfeature.RIVERS)

# Adding state and province borders for more detail
states_provinces = cfeature.NaturalEarthFeature(
    category='cultural',
    name='admin_1_states_provinces_lines',
    scale='50m',
    facecolor='none')
# ax.add_feature(states_provinces, edgecolor='gray')

# Colorbar
cbar = fig.colorbar(contour_plot, shrink=0.5, label='Average Air Temperature (°K)')
cbar.minorticks_on()

# Adding gridlines and labels
gl = ax.gridlines(draw_labels=True, color='gray', alpha=0.5, linestyle='--')
gl.top_labels = False
gl.right_labels = False

plt.title('Contour Plot of Average Air Temperature')
plt.show()
