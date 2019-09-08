import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates
import mpl_finance as mpl
from tkinter import *
from yahoo_fin.stock_info import get_data
import pandas as pd
import plotly.graph_objects as go


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
        df = get_data("{ticker}".format(ticker=self.e1.get()),
                        start_date = self.e2.get(), end_date = self.e3.get())
        

        df.index = pd.to_datetime(df.index)

        fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])

        fig.show()

     
AutoPlot()
