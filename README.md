# Electricity Price and Carbon Intensity Prediction

## Overview

This project forecasts electricity prices and analyzes carbon intensity trends for three U.S. power markets:

- New York (NYISO)
- Texas (ERCOT)
- California (CAISO)

The work is implemented in Jupyter notebooks using ARIMA/SARIMA time-series models with hourly resampling of ISO market data and grid carbon-intensity datasets.

## Project Scope

- Multi-state electricity price forecasting (New York, Texas, California)
- Carbon-intensity forecasting and trend analysis
- Historical time-series preprocessing across multiple quarterly CSV files
- Model evaluation using MAE, MSE, RMSE, and R²

## Methods Used

- `Python`, `Pandas`, `NumPy`
- `statsmodels` (`ARIMA`, `SARIMAX`)
- `scikit-learn` metrics (`MAE`, `MSE`, `R²`)
- Time-series preprocessing:
  - timestamp parsing and alignment
  - hourly resampling
  - interpolation / missing-value handling
  - outlier clipping (Texas experiments)
  - normalization with `MinMaxScaler` (Texas experiments)

## Key Modeling Configurations (Recovered)

- New York SARIMA (price forecasting):
  - `order=(1,1,1)`
  - `seasonal_order=(1,1,1,24)`

- Texas SARIMA (price forecasting):
  - `order=(1,0,1)`
  - `seasonal_order=(0,1,1,24)`
  - hourly data scaling + outlier clipping

- California SARIMA (price forecasting):
  - `order=(1,1,1)`
  - `seasonal_order=(1,1,1,24)`

## Saved Evaluation Results (Notebook Outputs)

### New York (2024 evaluation)

- MAE: `102.23`
- MSE: `12505.12`
- RMSE: `111.83`

### Texas (2024 evaluation, two saved runs)

- Run 1: MAE `17.9159`, MSE `5737.6328`, R² `-0.02456`
- Run 2: MAE `17.9283`, MSE `5735.7541`, R² `-0.02423`

### California (2024 evaluation)

- MAE: `79.5303`
- MSE: `8866.0607`
- RMSE: `94.1598`

## Repository Files

- `newyork.ipynb` - New York forecasting and analysis
- `texas.ipynb` - Texas forecasting and analysis
- `California.ipynb` - California forecasting and analysis
- `myfinalproject.ipynb` - combined/final project notebook work
- `CALSIS.IPYNB` - California SARIMA experiment notebook
- `newyork.py` - New York data loading script
- `PROJECT_VALUES_AND_RESULTS.md` - recovered paths, parameters, and metrics summary

## Notes

- Some notebooks reuse the same forecast output filenames, so later runs may overwrite earlier forecast CSVs.
- Local paths in notebooks point to datasets under the author's `Downloads` directory; update these paths before running on another machine.
