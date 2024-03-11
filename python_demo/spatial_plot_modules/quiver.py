# This code provides you with a simple idea of how to do a quiver plot of a climate variable of interest (particularly wind speed data).

#import the required libraries
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Load the wind datasets
uwnd = xr.open_dataset('../../datasets/uwnd.mon.mean.jja.nc')
vwnd = xr.open_dataset('../../datasets/vwnd.mon.mean.jja.nc')

# Compute the mean over time
uwnd_mean = uwnd.uwnd.mean(dim='time')
vwnd_mean = vwnd.vwnd.mean(dim='time')

# Select the data at 850 hPa
uwnd_850 = uwnd_mean.sel(level=850)
vwnd_850 = vwnd_mean.sel(level=850)


# Compute wind speed for background
wind_speed = np.sqrt(uwnd_850**2 + vwnd_850**2)

# Setup the plot with Cartopy
fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

# Plot wind speed as background
speed_plot = ax.contourf(uwnd_850.lon, uwnd_850.lat, wind_speed, levels=20, cmap='coolwarm', transform=ccrs.PlateCarree())
cbar = fig.colorbar(speed_plot, shrink=0.5, label='Wind Speed (m/s)')
cbar.minorticks_on()

# Quiver plot for wind direction and magnitude
# Note: Quiver plots can be dense; thinning data can help visualization
lon = uwnd_850.lon.values
lat = uwnd_850.lat.values
u = uwnd_850.values
v = vwnd_850.values

# Thinning data for clearer quiver plot
thin = 3  # Change thinning factor as needed for your dataset's resolution
q = ax.quiver(lon[::thin], lat[::thin], u[::thin, ::thin], v[::thin, ::thin], transform=ccrs.PlateCarree(), scale=300)

# Adding map features for better visualization
ax.add_feature(cfeature.LAND, edgecolor='black')
ax.add_feature(cfeature.COASTLINE)
# ax.add_feature(cfeature.BORDERS, linestyle=':')
# ax.add_feature(cfeature.LAKES, alpha=0.5)
# ax.add_feature(cfeature.RIVERS)

plt.title('Wind Direction and Magnitude at 850 hPa')
plt.show()
