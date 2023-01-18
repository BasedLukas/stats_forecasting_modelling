import requests
import csv
import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from statsmodels.tsa.seasonal import STL
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt




sns.set_style("darkgrid")
plt.rc("figure", figsize=(16, 12))
plt.rc("font", size=13)

df = pd.read_csv("new_england_tavg.csv")
df["date"] = pd.to_datetime(df["date"], infer_datetime_format=True)
df.set_index("date", inplace=True)

data = df
#summarize the data bu creating a new df with the monthl average
monthly_avg = data.resample('M').mean()
#set frquency of index to M
monthly_avg.index.freq = 'M'
#convert values to Fahrenheit
monthly_avg["measurement"] = monthly_avg["measurement"] * 9/5 + 32

from prophet import Prophet
df["ds"] = df.index
df["y"] = df["measurement"]
df = df[["ds", "y"]]
m = Prophet()
m.fit(df)
future = m.make_future_dataframe(periods=365)
forecast = m.predict(future)
fig1 = m.plot(forecast)
fig2 = m.plot_components(forecast)
plt.show()
m.
