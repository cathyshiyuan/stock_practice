#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 19:15:42 2017

@author: Cathy
"""
import pandas as pd
from pandas_datareader.famafrench import get_available_datasets
import pandas_datareader.data as web
#print get_available_datasets()
path = '/Users/Cathy 1/Desktop/python/stock_datasets.xlsx'
file = pd.read_excel(path)

######################   read data in --updated ############################
ds_m_y = web.DataReader('F-F_Research_Data_Factors', 'famafrench')

#print ds.keys()

ds_w = web.DataReader('F-F_Research_Data_Factors_weekly', 'famafrench')
#print ds1
ds_d = web.DataReader('F-F_Research_Data_Factors_daily', 'famafrench')
#print ds_d.keys()
ds_5_m_y = web.DataReader('F-F_Research_Data_5_Factors_2x3', 'famafrench')
ds_5_d = web.DataReader('F-F_Research_Data_5_Factors_2x3_daily', 'famafrench')
#print ds_5
############################################################################

#  month: period = 0 ,  year: period = 1, default = 0

def factor_data(ds, period, factor): 
    
    factor_data = ds[period][factor]
    return factor_data
#print factor_data(ds_m_y, 0, 'SMB') 
   
def beta(ticker):
    beta = file[ticker]['Beta']  
    return beta

#print beta('A17U.SI')














