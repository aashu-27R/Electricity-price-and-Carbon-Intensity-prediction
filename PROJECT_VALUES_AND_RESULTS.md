# Electricity Price Prediction Project: Recovered Values and Results

## Data Paths (Local)

- New York electricity prices: `/Users/aashrithasankineni/Downloads/newyork_electricity_prices`
- New York carbon footprint: `/Users/aashrithasankineni/Downloads/newyork_carbon_footprint`
- Texas electricity prices: `/Users/aashrithasankineni/Downloads/texas_electricity_prices`
- Texas carbon footprint: `/Users/aashrithasankineni/Downloads/texas_carbon_footprint`
- California electricity prices: `/Users/aashrithasankineni/Downloads/california_electricity_prices`
- California carbon footprint: `/Users/aashrithasankineni/Downloads/california_carbon_footprint`

## Common Preprocessing Choices

- CSV reading often uses `skiprows=3`
- `on_bad_lines='skip'` used in some loaders
- Time resampling to hourly (`'h'` / `'H'`)
- Stationarity checks with ADF (`adfuller`)
- ACF/PACF plots with `lags=48`
- Typical forecast horizon: `8760` hours (1 year)

## Key Target Columns

- New York price target: `J - New York City LMP`
- New York comparison columns: `D - North LMP`, `J - New York City LMP`, `K - Long Island LMP`
- Texas price target (single-region version): `Bus average LMP`
- Texas regional columns (mean-based version): `Bus average LMP`, `Houston LMP`, `Hub average LMP`, `North LMP`, `Panhandle LMP`, `South LMP`, `West LMP`
- California price target: `PALOVRDE_ASR-APND LMP`
- Carbon target (all states): `Carbon Intensity gCO₂eq/kWh (direct)`

## Forecast Dates Used

- 2024 forecast window:
  - Start: `2024-01-01 00:00:00`
  - End: `2024-12-31 23:00:00`
- 2025 forecast window:
  - Start: `2025-01-01 00:00:00`
  - End: `2025-12-31 23:00:00`

## Model Configs (Recovered)

### New York Electricity Price

- ARIMA variant:
  - `order=(1, 1, 1)`
- SARIMA variant(s):
  - `order=(1, 1, 1)`
  - `seasonal_order=(1, 1, 1, 24)`
  - `maxiter=1000` in some fits

### Texas Electricity Price

- SARIMA (scaled):
  - `order=(1, 0, 1)`
  - `seasonal_order=(0, 1, 1, 24)`
  - `MinMaxScaler()` applied
  - Outlier clipping at 1st and 99th percentiles
  - `maxiter=1000`

### California Electricity Price

- ARIMA variant:
  - `order=(1, 1, 1)`
- SARIMA variants:
  - `order=(1, 1, 1)`, `seasonal_order=(1, 1, 1, 24)`
  - Another notebook section also uses `order=(2, 1, 1)`, `seasonal_order=(1, 1, 1, 24)`

## Saved Forecast / Model Files Seen

- New York:
  - `.../newyork_electricity_prices/forecast_2024.csv`
  - `.../newyork_electricity_prices/sarima_model_2020_2023.pkl`
  - `.../newyork_electricity_prices/sarima_model_2022_2024.pkl`
- Texas:
  - `.../texas_electricity_prices/forecast_2024_hourly.csv`
  - `.../texas_electricity_prices/forecast_2025_hourly.csv`
- California:
  - `.../california_electricity_prices/forecast_2024.csv`
  - `.../california_electricity_prices/sarima_model_2021_2023.pkl`
  - `.../california_electricity_prices/sarima_model_2022_2024.pkl`

## Saved Metrics (Notebook Outputs)

### New York (2024 evaluation)

- Metrics:
  - MAE: `102.23`
  - MSE: `12505.12`
  - RMSE: `111.83`
- Metric evaluation uses:
  - Forecast file: `.../newyork_electricity_prices/forecast_2024.csv`
  - Actuals: 2024 Q1-Q4 NYISO files
  - Target: `J - New York City LMP` resampled hourly
- Forecast source model (matching `forecast_2024.csv`):
  - SARIMA trained on New York data from 2020Q1 to 2023Q3
  - `order=(1,1,1)`, `seasonal_order=(1,1,1,24)`

### Texas (2024 evaluation, two saved runs)

- Run 1:
  - MAE: `17.91586818670322`
  - MSE: `5737.632822328188`
  - R²: `-0.024563070857462677`
- Run 2:
  - MAE: `17.928313248977414`
  - MSE: `5735.754098074486`
  - R²: `-0.02422758903939015`
- Metric evaluation uses:
  - Forecast file: `.../texas_electricity_prices/forecast_2024_hourly.csv`
  - Actuals: 2024 Q1-Q4 ERCOT files
  - Actual target = hourly mean of regional LMP columns
- Forecast source models (same output file name, likely overwritten between runs):
  - Variant A target: `Bus average LMP`
  - Variant B target: mean of `Bus/Houston/Hub/North/Panhandle/South/West`
  - Both use SARIMA `order=(1,0,1)`, `seasonal_order=(0,1,1,24)` with scaling/clipping

### California (2024 evaluation)

- Metrics:
  - MAE: `79.53030518951084`
  - MSE: `8866.060697795423`
  - RMSE: `94.15976156403235`
- Metric evaluation uses:
  - Forecast file: `.../california_electricity_prices/forecast_2024.csv`
  - Actuals: 2024 Q1-Q4 CAISO interface files
  - Target: `PALOVRDE_ASR-APND LMP`
- Forecast source model (matching `forecast_2024.csv`):
  - SARIMA trained on California data from 2021Q1 to 2023Q3
  - `order=(1,1,1)`, `seasonal_order=(1,1,1,24)`

## Notes

- Some notebooks duplicate experiments and reuse the same forecast output filenames, so later runs may overwrite earlier results.
- `myfinalproject.ipynb` and `CALSIS.IPYNB` did not contain saved metric output text in the notebook outputs scanned.
