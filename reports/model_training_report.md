# Model Training Report

## Algorithm
XGBoost Regressor

## Baseline Performance

MAE: 8.84
RMSE: 11.60

## XGBoost Performance

MAE: 6.09
RMSE: 7.91

## Improvement

31.79% reduction in RMSE compared to baseline.

## Important Features

1. rolling_mean_7
2. lag_7
3. rolling_mean_30
4. is_weekend
5. day_of_week

## Conclusion

The model successfully captures demand trends,
seasonality and weekly purchasing patterns.