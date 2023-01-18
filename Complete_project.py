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
"""pandas.to_datetime(arg, errors='raise', dayfirst=False, yearfirst=False, utc=None, format=None, exact=True, 
unit=None, infer_datetime_format=False, origin='unix', cache=True)"""
# we need to convert the first column of the df to a date object
df["date"] = pd.to_datetime(df["date"])
# set the date column as the index
df.set_index("date", inplace=True)
#in order to rmove negative values, each value is added to the absolute value of the minimum value in the column

# plt.figure(figsize=[15, 7.5]) # Set dimensions for figure
# plt.plot(df.index, df["measurement"])
#
# plt.title("Average Temperature in New England")
# plt.xlabel('Date')
# plt.xticks(rotation=90)
# plt.grid(True)
# plt.show()
# plot_pacf(df["measurement"], lags=365)
# plt.show()
# ad_fuller_result = adfuller(df["measurement"])
# print(f'ADF Statistic: {ad_fuller_result[0]}')
# print(f'p-value: {ad_fuller_result[1]}')
data = df
#set frquency of index to daily
data.index.freq = 'D'
myorder = (1,1,1)
myseasonal_order = (1,1,1,365)
# add frequency parameter to SARIMAX
model = SARIMAX(data, order=myorder, seasonal_order=myseasonal_order, freq="D")
results = model.fit()
print(results.summary())
