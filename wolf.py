import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt 
import yahoofinance
from pylab import *
import numpy as np
import scipy.signal as sc
import datetime as dt


#define user input 

user_input = input('Enter Stock Symbol:     ')

stock = yf.Ticker(user_input)

recco = stock.recommendations

allison = [stock, stock.history(period ='5d'), recco]

#new = print(allison)

stock.history(period='1mo') 

eureka = pd.DataFrame(stock.history(period='5d'))


frame = (eureka.columns.values)

leff =list(frame) 

print(leff [0:5])

N = 5


xlab = 'Intraday Date'
ylab = 'Price'
title = (stock)

#axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)




first_n_column = eureka.iloc[:, :N]

print(first_n_column) 

print(recco)


plt.plot(eureka['Close'])

plt.show()
plt.clf()
