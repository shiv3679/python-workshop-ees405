# Python Modules for Climate Data Analysis

This repository contains a collection of Python modules designed to facilitate the analysis and visualization of climate data. These modules are specifically tailored for working with spatial and temporal datasets, providing tools for plotting, trend analysis, and data manipulation within the domain of climate science.

## Getting Started 
- **Pre-requisites**: Before you begin, ensure you have Python 3.x installed on your system. You will also need to install several dependencies. You can install it via `pip` as well as `conda`. The preferred way is to install via `conda` as it takes care of the dependencies involved. 

```bash
conda install xarray dask matplotlib cartopy scipy numpy
```

```bash
pip install xarray dask matplotlib cartopy scipy numpy
```

You can also install via `requirements.txt` file 

```bash
pip install -r requirements.txt
```

- **Installation**: Clone the repository to your local machine.

```bash
git clone https://github.com/yourusername/python-workshop-ees405.git
cd python-workshop-ees405
```

## Interactive Notebook

We have provided a Jupyter notebook along with this repository that you can use to follow along with our modules. It's a great way to learn and also experiment by trying out various codes.

To access the interactive version of the notebook, click on the binder badge below:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/shiv3679/python-workshop-ees405/main?urlpath=https%3A%2F%2Fgithub.com%2Fshiv3679%2Fpython-workshop-ees405%2Fblob%2Fmain%2Fpython_workshop.ipynb)

This will launch the notebook in a Binder environment, allowing you to execute and modify the code without needing to install anything on your local machine.



## Modules Overview
The repository is organized into two main categories: `spatial_plot_modules` and `temporal_plot_modules`, each containing Python scripts tailored for specific types of climate data analysis.

### Spatial Plot Modules
- `spatial.py`: Base module for generating spatial plots.
- `contour.py`: Generates contour plots for spatial data.
- `contour_lines.py`: Focuses on adding contour lines to spatial plots for enhanced detail.
- `levels.py`: Helps in defining custom levels for contour plots.
- `quiver.py`: Creates quiver plots to visualize vector fields like wind patterns.
- `streamplot.py`: Similar to quiver but produces streamlines for vector field visualization.
- `spatial_trend.py`: Analyzes and visualizes trends in spatial data.
- `spatial_trend_gpu.py`: A GPU-accelerated version of spatial_trend.py for faster processing of large datasets.
### Temporal Plot Modules
- `timeseries.py`: Designed for creating time-series plots to analyze trends over time.

## Usage
Each module is designed to be run as a standalone script. Here is an example of how to run the `timeseries.py` module:

```bash 
python3 temporal_plot_modules/timeseries.py
```
# Contributing
We welcome contributions to improve the modules or documentation. Please feel free to fork the repository, make your changes, and submit a pull request.

# License
This project is licensed under the MIT License. See [LICENSE](https://github.com/shiv3679/python-workshop-ees405/LICENSE)

# Acknowledgments
Thanks to all the contributors who have helped in developing these modules.
