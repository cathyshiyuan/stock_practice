#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 19:14:24 2017

@author: Cathy
"""

import pandas as pd
import os
import time

import matplotlib.pyplot as plt
import pandas.io.data
from pandas_datareader import data
from bs4 import BeautifulSoup
import urllib



plt.style.use('ggplot')

path = "/Users/Cathy/Desktop/python/SgStock"


def Key_Stats(gather = "P/E"):
    df = pd.DataFrame(columns = ['Ticker','P/E'])
    file = os.listdir(path)
    for each_file in file[1:]:
        
        full_file_path = path + '/' + each_file
        
        ticker = each_file.split('.htm')[0]
        url = 'https://sg.finance.yahoo.com/q/ks?s='+ ticker
        url_all = url.append()
        source = open(full_file_path,'r').read()
        
        pe = source.split('"trailingPE":')[1].split(',"regularMarketVolume"')[0].split('"fmt":"')[1].split('"}')[0]
        df=df.append({'Ticker':ticker,'P/E':pe},ignore_index=True)
    #print df
    df.sort_values('P/E',ascending=False,inplace=True)
    #print df
    #

    df.to_csv('PEratio')

for r in url_all:
    r =urllib.urlopen(url).read()
    soup = BeautifulSoup(r)
    

#url = 'https://sg.finance.yahoo.com/q/ks?s='+ ticker


        #print pe
    
    
   
    #print os.walk(statspath)
    #stock_list = [x[0] for x in os.walk(statspath)]
    #print(stock_list)            
    #df = pd.DataFrame(columns = ['Ticker','P/E'])
