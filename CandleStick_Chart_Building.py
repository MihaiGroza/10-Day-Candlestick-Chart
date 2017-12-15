import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
import quandl

style.use("ggplot")

#Extracting data
df = quandl.get("WIKI/KO", trim_start = "2000-12-12", trim_end = "2014-12-30")

#Resampling the data set at a 10 day frequency
df_ohlc = df["Adj. Close"].resample("10D").ohlc()
df_volume = df["Volume"].resample("10D").sum()

df_ohlc.reset_index(inplace=True)

#Converting Date to mdate format
df_ohlc["Date"]= df_ohlc["Date"].map(mdates.date2num)

#print(df_ohlc.head())

#Plotting
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1),(5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup="g")
ax2.fill_between(df_volume.index.map(mdates.date2num),df_volume.values, 0)
plt.show()