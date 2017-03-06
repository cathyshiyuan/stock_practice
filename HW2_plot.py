#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:52:46 2017

@author: Cathy
"""

#from openpyxl import load_workbook
#from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import matplotlib.ticker as mticker
from matplotlib import style
#from matplotlib.finance import candlestick_ohlc
#import matplotlib.dates as mdates
#from datetime import datetime
style.use('ggplot')

def stock_plot(stock_name):
    path = '/Users/Cathy 1/Desktop/Semester2/ECA5337FE/HW2/Folder_SLFiles/A0161690E_HW2.xlsm'
    
    wb = pd.read_excel(path, sheetname = None)
    aapl = wb[stock_name]
    
    start = 100
    plt.title('Stock Analysis')
    ax1 = plt.subplot2grid((2,1),(0,0))
    ax2 = plt.subplot2grid((2,1),(1,0))
    
    #==============================================================================
    # def bytespdate2num(fmt,encoding='utf-8'):
    #     strconverter = mdates.strpdate2num(fmt)
    #     return strconverter
    #==============================================================================
    
    x = aapl['Date'][start:]
    x = np.array(x)
    
    
    #date = map(lambda x: mdates.strpdate2num(str(datetime.strftime(x, '%d %m %Y %H %M %S'))),x)
    y = aapl['EMA(5)'][start:]
    y1 = aapl['EMA(26)'][start:]
    volume = aapl['Volume'][start:]
    ax1.set_ylabel('Price/Volume',size = '10')
    ax1.plot(x, y, label = 'EMA(5)')
    ax1.plot(x, y1, label = 'EMA(26)',color='g')
    ax1v = ax1.twinx()
    ax1v.fill_between(x, 0, volume, facecolor = '#adc8fa',alpha = 0.5)
    ax1v.axes.yaxis.set_ticklabels([])
    ax1v.grid(False)
    ax1v.set_ylim(0,1.5*volume.max())
    ax1.axes.xaxis.set_ticklabels([])
    
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.fill_between(x, y, y1, where = (y>y1),color='g',alpha=0.3,interpolate=True)
    ax1.fill_between(x, y, y1, where = (y<y1),color='r',alpha=0.3,interpolate=True)
    close_p = aapl['Close'][start:]
    BB = aapl['BB(20)'][start:]
    SMA = aapl['SMA'][start:]
    BB_up = BB + SMA
    BB_down = SMA - BB
    
    ax2.set_ylabel('Price',size= '10')
    ax2.plot(x, BB_up,color='#8cabec',label='BB')
    ax2.plot(x, BB_down,color='#8cabec')
    ax2.plot(x, close_p, color ="#303b46")
    for label in ax2.xaxis.get_ticklabels():
        label.set_rotation(45)
    #ax2.fill_between(x,BB_up,close_p,where = (close_p > BB_up),color='g',alpha=0.3)
    #ax2.fill_between(x,BB_down,close_p,where = (close_p < BB_down),color='r',alpha=0.3)
    ax2.fill_between(x,BB_up,BB_down,color='#8cabec',alpha=0.2)
    plt.title(stock_name,color='#526d7a',size = '12')
    ax1.legend()
    ax2.legend()
    plt.show()
    
stock_plot('Google')