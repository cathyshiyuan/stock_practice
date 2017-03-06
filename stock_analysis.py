#/usr/bin/python
"""
Author:Cathy
Stock Analysis
"""

import pandas as pd
#import pandas.io.data
import numpy as np
#from pandas_datareader import data
import pandas_datareader
import os
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import datetime
#import time
#from pandas_datareader.famafrench import get_available_datasets
#import pandas_datareader.data as web


################ You can change any date you want###############
start = datetime.date(2016,12,20)
end = datetime.date.today()
################################################################


#STI = pd.DataFrame.from_csv('/Users/Cathy/Desktop/python/YAHOO-INDEX_STI.csv')
#stock_data = pd.read_excel('/Users/Cathy 1/Desktop/python/stock_datasets.xlsx')
path = "/Users/Cathy 1/Desktop/python/SgStock"
file = os.listdir(path)
stock_name_list = []

for each_file in file[1:]:
    #print each_file
    stock_name = each_file.split('.htm')[0]
    #print stock_name
    stock_name_list.append(stock_name)
    
print  stock_name_list

all_stock = []
all_stock_change = {}
stock_per_change = []
price_change = {}

#STI = STI.ix[:'2016-01-04']['Adjusted Close']
start_unix = int(start.strftime('%s'))
end_unix = int(end.strftime('%s'))



### Percantage change in closing price everyday for each stocks ####
########## Database can be renew daily #############################

def p_change():
    
    yesterday_price = stock_price['Adj Close'].ix[0]
    #print yesterday_price
    #yesterday_sti_price = STI.ix[-1]
   
    stock_per_change = []
    for t in range(start_unix,end_unix+1,86400):
        
        time = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d')
        #print time
        try:
            
            today_price = stock_price['Adj Close'].ix[time]
            
            stock_p_change = 100*(today_price - yesterday_price)/yesterday_price
            
            #stock_p_change
            
            stock_per_change.append(stock_p_change)
            yesterday_price = today_price
     
    #print today_price
       
            
        except Exception as e:
            print e
            #pass
    #print len(stock_per_change)
    price_change = {i:stock_per_change}        
    return price_change

####################### Can download the stock price daily ##########################        
    
        
for i in stock_name_list:
    try:
        stock_price = pandas_datareader.data.DataReader(i,"yahoo",start,end)
        #s = stock_price.index.astype(np.int64)
        #today_price = stock_price['Adj Close'].ix['2016-01-01']
        #print today_price
        stock_i_change = p_change()
        #print stock_i_change
        #time.sleep(15)
        all_stock_change.update(stock_i_change)
        all_stock.append(stock_price)
    except:
        pass
        
#print all_stock_change
result = pd.concat(all_stock,axis=1,keys=stock_name_list)

result.to_excel('stock_history.xlsx')

################### To see the overall performance of each stocks #####################

def classify():
    stock_performance = {}
    stock_performance1 = {}
    for item in all_stock_change:
        #print item
        certain_stock_change = all_stock_change[item]
        #print certain_stock_change[273]
        count = 0
        for p in range(0,len(certain_stock_change)+1):
            try:
                if certain_stock_change[p]>0:
                    count +=1
            except:
               
                pass
           
        performance = 100.0*count/len(certain_stock_change)
        stock_performance = {item:performance}   #out put of each stock
        stock_performance1.update(stock_performance)  #pack all stocks in dic
    #print stock_performance1
    return stock_performance1
            
#classify()

################## In the order of performance ####################

sss = pd.DataFrame.from_dict(classify(),'index')
#print sss.sort_values(0,ascending=False)


################### N-day Moving Average ##################################

def EMA(n_days, ticker):
    ave_price = 0
    datasets = result[ticker]['Adj Close'].dropna()
    id = datasets.index
    id = id[n_days-1:]
    
    for n in range(n_days):
        ave_price += datasets[n]

    ave_price = ave_price/n_days
    
    beta = 2.0/(n_days+1)
     
    #print beta
    EMAtl = ave_price
    #Pt = datasets[n_days-1]
    #print id
    index = np.array(id)
    EMA =pd.DataFrame(columns = index) 
    i = 0
    
    try:
        while n_days <= len(datasets) :

            Pt = datasets[n_days-1]
            
            #print Pt
            EMAt = beta*Pt + (1-beta)*EMAtl
            #print EMAt
            
            EMA[index[i]]= [EMAt]
            #print EMA
            n_days += 1
            i += 1
            
            EMAtl = EMAt
            #print beta
    #EMA1 = DataFrame(EMA,id)
    #print ema_list       
    except Exception as e:
        #print e
        pass
    #print EMA.transpose()
    return EMA.transpose()
#print EMA(5,'D05.SI')

######################## MACD ############################
"""
def MACD(ticker, S, L):
    MACDt = (EMA(S, ticker)- EMA(L, ticker)).dropna()
    print MACDt
    beta = 2.0/(9+1) # use 9 to calculate signal by default
    
    total = 0
    date = 9 # use 9 to calculate signal by default
    id = MACDt.index#[date-1:]
    #print id
    
    i = 0
    index = np.array(id)
   # print len(index)
   # print len(MACDt)
    MACD_signal = pd.DataFrame(columns = index)
    
    for num in range(0,9):
        total = total + MACDt.ix[num]
    MACDtl = total / 9
    try:
        while date <= len(MACDt):
            Pt = MACDt.ix[date-1]
            
            signal = beta * Pt + (1 - beta) * MACDtl
            MACD_signal[index[i]] = [signal]
            MACDtl = signal
            i += 1
            date += 1
    except Exception as e:
        
        pass
        #print date, str(e)
    return (MACD_signal.transpose(), MACDt)
    #print MACD.transpose()
    #print MACDt
    #print MACDt.ix[len(MACDt)-MACD('D05.SI',12,26)
#print MACD('D05.SI',12,26)[0]-MACD('D05.SI',12,26)[1]
"""
########################  FAMA FRANCH #############################





######################## MOMENTUM ###############################
def momentum(n_days, ticker):
    price_sets = result[ticker]['Adj Close'].dropna()
    #print price_sets[:5]
    
    index = price_sets.index
    index = index[n_days:]
    #print len(index)
    #print len(price_sets)-n_days
    momentum = pd.DataFrame(columns = index)
    
    for i in range(0, len(price_sets)-n_days):
        
        Mt = price_sets[i+n_days]-price_sets[i]
        momentum[index[i]] = [Mt]
    return momentum.transpose()
        
#print momentum(10,'D05.SI')
                        


####################### Buy or Sell? ##############################

def sign(short, lon , ticker):
    
    #print 'According to EMA'
   
    sign =  (EMA(short, ticker).ix[-1]-EMA(lon, ticker).ix[-1])/EMA(lon, ticker).ix[-1]
    
    if (sign > 0.01).bool():
        print 'EMA suggest: Buy '+ ' ' +ticker
    else:
        print 'EMA suggest: Sell'+ ' ' +ticker
'''
def MACD_sign(ticker):
    
    #print 'According to MACD'
    #signal-MACD
    sign = (MACD(ticker, 12, 26)[0]-MACD(ticker, 12, 26)[1]).dropna() 
    #print sign.ix[-1]
    #print float(sign.ix[0])>0
    if float(sign.ix[-1]) < 0 and float(sign.ix[-2]) > 0:
        print 'MACD suggest: Buy '+ ' ' +ticker
    else:
        print 'MACD suggest: Sell '+ ' ' +ticker
#MACD_sign('D05.SI')

'''
#==============================================================================
# def give_sign():
#         
#     for ticker in stock_name_list:
#         sign(5, 20, ticker)
#         MACD_sign(ticker)
# #give_sign()
#         
# 
#==============================================================================


######################## EMA PLOT ###########################
import matplotlib.ticker as mticker
def ema_plot(ticker, days):
    ema2 = EMA(2,ticker)[-days:]
    ema5 = EMA(5,ticker)[-days:]
    ema10 = EMA(10,ticker)[-days:]
    ema20 = EMA(20,ticker)[-days:]
    ax1 = plt.subplot2grid((1,1),(0,0))
    
    for item in (ema2,ema5,ema10,ema20):
        ax1.plot(item, label = 'EMA')
    for lable in ax1.xaxis.get_ticklabels():
        lable.set_rotation(45)
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    
    ax1.legend(['2d','5d', '10d', '20d'], loc='upper left')
    plt.title(ticker)
    plt.show() 
    
for ticker in stock_name_list:
    try:
        ema_plot(ticker, 20)
    except:
        pass
    #MACD_sign(ticker)
    #sign(5, 20 , ticker)

#############################################################

#==============================================================================
# today_performance = classify()
# 
# for stock in today_performance:
# 	if today_performance[stock] >= 50:
# 		sign(5, 10 , stock)
# 
# 			
#  
#==============================================================================
#print 'Currently Holding:'  

#==============================================================================
# sign(5,10,'F34.SI')
# sign(5,10,'D05.SI')
# sign(5,10,'S58.SI')
# sign(5,10,'C09.SI')
# sign(5,10,'Z74.SI')
# sign(5,10,'CC3.SI')
# sign(5,10,'C6L.SI')
# 
# sign(2,5,'F34.SI')
# sign(2,5,'D05.SI')
# sign(2,5,'S58.SI')
# sign(2,5,'C09.SI')
# sign(2,5,'Z74.SI')
# #sign(2,5,'CC3.SI')
# sign(2,5,'C6L.SI')
#==============================================================================

#==============================================================================
# 
# ema_plot('U11.SI',10)
# ema_plot('BN4.SI',10)
# ema_plot('S63.SI',10)
# ema_plot('C31.SI',10)
# ema_plot('S59.SI',10)
# ema_plot('MC0.SI',10)
# ema_plot('O39.SI',10)
# ema_plot('C09.SI',10)
# ema_plot('U96.SI',10)
# ema_plot('U14.SI',10)
# ema_plot('C6L.SI',10)
# ema_plot('Z74.SI',10)
# ema_plot('S68.SI',10)
# ema_plot('D05.SI',10)
# ema_plot('S51.SI',10)
# ema_plot('CC3.SI',10)
# ema_plot('F34.SI',10)
# ema_plot('S58.SI',10)
# 
# 
#==============================================================================

