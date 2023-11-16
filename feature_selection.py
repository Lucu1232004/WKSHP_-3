from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestRegressor
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score 

df_unido = pd.read_csv("WKSHP_03\df_unido.csv")

X = df_unido[['GDP per capita', 'Life expectancy', 'Freedom']]
y = df_unido['Happiness Score']

joblib_file = "modelo_regresion.pkl"
loaded_regressor = joblib.load(joblib_file)

model = RandomForestRegressor()
model.fit(X, y)

sfm = SelectFromModel(model, threshold=0.1)
sfm.fit(X, y)


y_pred_before = loaded_regressor.predict(X)
mse_before = mean_squared_error(y, y_pred_before)
r2_before = r2_score(y, y_pred_before)


y_pred_after = loaded_regressor.predict(X)
mse_after = mean_squared_error(y, y_pred_after)
r2_after = r2_score(y, y_pred_after)

print("Rendimiento antes de la selección de características:")
print(f"Mean Squared Error: {mse_before}")
print(f"R-squared: {r2_before}")

print("\nRendimiento después de la selección de características:")
print(f"Mean Squared Error: {mse_after}")
print(f"R-squared: {r2_after}")
