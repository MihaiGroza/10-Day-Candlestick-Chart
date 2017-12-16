import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
import quandl
from tkinter import *
style.use("ggplot")

class AutoPlot:
    def __init__(self):
        master = Tk()
        Label(master, text="Stock Ticker").grid(row=0)
        Label(master, text="Range Start").grid(row=1)
        Label(master, text="Range End").grid(row=2)
        
        self.e1 = Entry(master)
        self.e2 = Entry(master)
        self.e3 = Entry(master)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        
        Button(master, text='Quit', command=master.destroy).grid(row=3, column=0, sticky=W, pady=4)
        Button(master, text='Show', command=self.make_plot).grid(row=3, column=1, sticky=W, pady=4)
        
        mainloop()



    def make_plot(self):
        #Extracting data
        df = quandl.get("WIKI/{ticker}".format(ticker=self.e1.get()),
                        trim_start = self.e2.get(), trim_end = self.e3.get())
        
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
        plt.tight_layout()
        
AutoPlot()