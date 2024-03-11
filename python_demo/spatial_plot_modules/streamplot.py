import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Load the wind datasets
uwnd = xr.open_dataset('../../datasets/uwnd.mon.mean.jja.nc')
vwnd = xr.open_dataset('../../datasets/uwnd.mon.mean.jja.nc')

# Compute the mean over time
uwnd_mean = uwnd.uwnd.mean(dim='time')
vwnd_mean = vwnd.vwnd.mean(dim='time')

# Select the data at 850 hPa
uwnd_850 = uwnd_mean.sel(level=850)
vwnd_850 = vwnd_mean.sel(level=850)


uwnd_850['lon'] = ((uwnd_850['lon'] + 180) % 360) - 180
vwnd_850['lon'] = ((vwnd_850['lon'] + 180) % 360) - 180
uwnd_850 = uwnd_850.sortby('lon')  # Ensure data is sorted after adjustment
vwnd_850 = vwnd_850.sortby('lon')

# Compute wind speed
wind_speed = np.sqrt(uwnd_850**2 + vwnd_850**2)

# Setup the plot
fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_global()  # Ensure full global coverage

# Plot wind speed background
speed_plot = ax.contourf(uwnd_850.lon, uwnd_850.lat, wind_speed, levels=20, cmap='coolwarm', transform=ccrs.PlateCarree())
cbar = fig.colorbar(speed_plot, shrink=0.5, label='Wind Speed (m/s)')
cbar.minorticks_on()

# Streamplot for direction and magnitude
stream = ax.streamplot(uwnd_850.lon, uwnd_850.lat, uwnd_850.values, vwnd_850.values, density=2, color='black', linewidth=0.5, arrowsize=1.5, transform=ccrs.PlateCarree())

# Map features
ax.add_feature(cfeature.LAND, edgecolor='black')
ax.add_feature(cfeature.COASTLINE)
# ax.add_feature(cfeature.BORDERS, linestyle=':')
# ax.add_feature(cfeature.LAKES, alpha=0.5)
# ax.add_feature(cfeature.RIVERS)

plt.title('Global Wind Direction and Magnitude at 850 hPa')
plt.show()
