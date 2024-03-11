# This code provides you with a simple idea of how to do plot a spatial trend analysis and plot the significance of the trend. This code particularly uses the power of GPU and parallel processing to speed up the analysis.

#import the required libraries
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
from scipy.stats import linregress
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def linregress_func(y, x):
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    return np.array([slope, p_value])

def apply_linregress(data_array):
    time_index = np.arange(len(data_array.time))
    data_array_chunked = data_array.chunk({"time": -1})

    results = xr.apply_ufunc(
        linregress_func,
        data_array_chunked,
        input_core_dims=[["time"]],
        output_core_dims=[["output_dim"]],
        vectorize=True,
        dask="parallelized",
        output_dtypes=[float],
        output_sizes={"output_dim": 2},
        kwargs={"x": time_index}
    )

    slope = results.isel(output_dim=0)
    p_value = results.isel(output_dim=1)
    
    return slope, p_value

# Load dataset
file = '../../datasets/air.2m.mon.mean.nc'
data = xr.open_dataset(file, chunks={'time': -1})  # Ensure dataset is chunked for Dask

# Squeeze the level dimension and select the air temperature variable
data_squeezed = data.air.squeeze()

# Apply linear regression to compute slope and p-value
slope, p_value = apply_linregress(data_squeezed)

# Compute significance
significant = p_value < 0.05

# Plotting
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_global()

# Plot trend (slope) as background
slope_plot = ax.contourf(data_squeezed.lon, data_squeezed.lat, slope, levels=20, cmap='coolwarm', transform=ccrs.PlateCarree())
cbar = fig.colorbar(slope_plot, shrink=0.5, label='Trend (change per unit time)')
cbar.minorticks_on()

# Highlight significant trends
lon, lat = np.meshgrid(data_squeezed.lon, data_squeezed.lat)
ax.scatter(lon[significant], lat[significant], color='black', s=1, transform=ccrs.PlateCarree())

# Add map features
ax.add_feature(cfeature.LAND, edgecolor='black')
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')

plt.title('Trend Significance in Air Temperature')
plt.show()
