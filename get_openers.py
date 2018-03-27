#!/usr/bin/env python

#get_openers.py
#
#by Joe Hahn
#jmh.datasciences@gmail.com
#66 March 2018
#
#this gets opening values and volumes for all tickers, and this result
#is later used to fill values for those tickers that start trading after 2013

#to execute:
#    ./get_openers.py

#set input parameters
debug = True

#read NYSE data
from stock_picker_source.helper_fns import *
path = 'data/private/eoddata/NYSE_*.zip'
market = read_market_data(path, drop_holidays=True)
if (debug):
    print market.head()
    print market.tail()
    print 'market.date.min() = ', market.date.min()
    print 'market.date.max() = ', market.date.max()
    print 'market.shape = ', market.shape

#get each ticker's earliest record
openers = market.groupby('ticker').first().sort_values('date', ascending=False).reset_index()
if (debug):
    print openers.head()
    print openers.tail()

#save tickers
import pickle
file = 'data/openers.pkl'
with open(file, 'wb') as f:
    pickle.dump(openers, f)
