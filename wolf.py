import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt 
from pylab import *
import numpy as np
import scipy.signal as sc
import datetime as dt


#define user input 
user_input = input('Enter Stock Symbol:     ')
#define stock variable as user input
stock = yf.Ticker(user_input)

#reccomendations defined
recco = stock.recommendations

#majorholders of stock 
major = stock.major_holders

allison = [stock, stock.history(period ='5d'), recco]

#set stock period, differs from dataframe time series
stock.history(period='1mo') 

#defining variable for dataframe using 5day
eureka = pd.DataFrame(stock.history(period='5d'))

#institutional holders 
insti = stock.institutional_holders

#frame
frame = (eureka.columns.values)

leff =list(frame) 
print(leff [0:5])

#define column selection
N = 5

#chart labels
xlab = 'Intraday Date'
ylab = 'Price'
title = (stock)

#axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)

#define printout 
first_n_column = eureka.iloc[:, :N]

#print commands 
print(first_n_column) 
print(recco)
print(insti) 

#plot chart 
plt.plot(eureka['Close'])

plt.show()

#clean
plt.clf()
