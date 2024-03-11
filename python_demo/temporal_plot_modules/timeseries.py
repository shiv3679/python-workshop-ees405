# This is a sample code to plot a timeseries of a particular climate variable.

# import the libraries 
import matplotlib.pyplot as plt  # for plotting
import xarray as xr # for loading the netcdf files
from sklearn.linear_model import LinearRegression # for linear regression analysis
from sklearn.metrics import mean_squared_error # for mean squared error calculation
import numpy as np # for array like operations

# Open the dataset
file = '../../datasets/air.2m.mon.mean.nc'
data = xr.open_dataset(file)
data_timeseries = data.air.mean(dim=['lat', 'lon']).squeeze()

# Yearly resampling
data_yearly = data_timeseries.resample(time='Y').mean()

# Plotting
plt.figure(figsize=(14, 6))

# Plot monthly data
plt.plot(data_timeseries.time, data_timeseries, label='Monthly Mean Air Temperature', color='lightgray')

# Plot yearly data
plt.plot(data_yearly.time, data_yearly, label='Yearly Mean Air Temperature', color='blue', linewidth=2, marker='o')

# Convert datetime to numerical format for regression
X = data_yearly.time.dt.year.values.reshape(-1, 1)  # Extract year and reshape for sklearn
y = data_yearly.values.reshape(-1, 1)

# Linear regression
linreg = LinearRegression().fit(X, y)
y_pred = linreg.predict(X)
rmse = np.sqrt(mean_squared_error(y, y_pred))

# Plot the trendline
plt.plot(data_yearly.time, y_pred, label=f'Trendline (RMSE={rmse:.2f})', color='red', linestyle='--')

# Calculate and print the slope
slope = linreg.coef_[0][0]  # Slope of the linear regression
print(f"Slope: {slope:.4f} °K/year")  # Change in temperature per year

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Air Temperature (°K)')
plt.title('Air Temperature Time Series Analysis')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

# Show plot
plt.show()
