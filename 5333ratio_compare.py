#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 13:44:10 2017

@author: Cathy
"""

import pandas as pd
#import os
#import matplotlib.pyplot as plt
#plt.style.use('ggplot')
#from pandas_datareader import data



path = '/Users/Cathy 1/Desktop/python/stock_datasets.xlsx'
file = pd.read_excel(path)
#print file.head()
#print list(file)

#==============================================================================
# path2 = "/Users/Cathy 1/Desktop/python/SgStock"
# file = os.listdir(path2)
# stock_name_list = []
# def get_ticker():
#     for each_file in file[1:]:
#         #print each_file
#         stock_name = each_file.split('.htm')[0]
#         #print stock_name
#         stock_name_list.append(stock_name)
#         return stock_name_list
#==============================================================================


def sort_key(tuple):
    return tuple[1]

def get_ratio(ratio_name):
    ratio_tuple = ()
    ratio_list = []
    for key in list(file):
        stock_ratio = file[key][ratio_name]
        ratio_tuple = (key, stock_ratio)
        ratio_list.append(ratio_tuple)
    return ratio_list



    
sorted_market_cap = sorted(get_ratio('Market Cap'), key = sort_key)
sorted_pe = sorted(get_ratio('Trailling P/E'), key = sort_key)
sorted_pb = sorted(get_ratio('P/B'), key = sort_key)

#print sorted_market_cap
#print sorted_pe

def score(ratio_list):
    score_dic ={}
    i = 1
    for tuple in ratio_list:
        score_dic[tuple[0]] = i
        i += 1
    return score_dic

scored_maket_cap = score(sorted_market_cap)
scored_pe = score(sorted_pe)
scored_pb = score(sorted_pb)

def score_addup(dic1, dic2):
    score_dic = {}
    for key in dic1:
        try:
            score_dic[key] = dic1[key] + dic2[key]
        except Exception as e:
            print key, str(e)
    return score_dic
    
#score_addup(scored_maket_cap, scored_pe)

#print scored_maket_cap
score_addup = score_addup(score_addup(scored_maket_cap, scored_pe),scored_pb)

sorted_score_addup = sorted(score_addup.items(), key = sort_key)


print 'This is the overall score of %s, the smaller the better' %('P/B, P/E, Market Cap')
for score_tuple in sorted_score_addup:
    
    print score_tuple[0], score_tuple[1]



    
#for ticker in stock_name_list:
    
    
            
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
