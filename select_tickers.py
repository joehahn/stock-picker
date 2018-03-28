#!/usr/bin/env python

#select_tickers.py
#
#by Joe Hahn
#jmh.datasciences@gmail.com
#16 March 2018
#
#this selects the desired tickers that will modeled

#to execute:
#    ./select_tickers.py

#set input parameters...this selects the 509 most-dollar-traded tickers of 2017, out of 3131 tickers
#dollar_volume_fraction = 0.05               #this selects 3 of 3131 tickers
dollar_volume_fraction = 0.8               #this selects 509 of 3131 tickers
start_date = '2017-01-01'
end_date = '2018-01-01'
path = 'data/private/eoddata/NYSE_2017.zip'
debug = True

#read NYSE data
from stock_picker_source.helper_fns import *
market = read_market_data(path, start_date=start_date, end_date=end_date, drop_holidays=True)
if (debug):
    print market.head()
    print market.tail()
    print 'start_date = ', start_date
    print 'end_date = ', end_date
    print 'market.date.min() = ', market.date.min()
    print 'market.date.max() = ', market.date.max()
    print 'market.shape = ', market.shape

#select tickers having highest dollar-volumes
print 'dollar_volume_fraction = ', dollar_volume_fraction
dpd_cs, tickers, market_top = get_top_tickers(market, dollar_volume_fraction)
N_all_tickers = len(market.ticker.unique())
N_tickers = len(tickers)
if (debug):
    print 'tickers = ', tickers
    print 'N_all_tickers = ', N_all_tickers
    print 'N_tickers = ', N_tickers
    print 'market_top.shape = ', market_top.shape

#plotting imports
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale=1.5)

#plot dpd_cs versus ticker
yp = dpd_cs/1.0e9
xp = range(len(yp))
fig, ax = plt.subplots(figsize=(16, 6))
p = ax.plot(xp, yp, linestyle='-')
N = len(tickers)
p = ax.plot(xp[N], yp[N], marker='o', markersize=12)
p = ax.set_title('2017 NYSE daily dollar-volume')
p = ax.set_xlabel('ticker')
p = ax.set_ylabel('dollar-volume    (G$/day)')
plt.savefig('figs/selected_tickers_volume.png')

#save tickers
import pickle
file = 'data/selected_tickers.pkl'
with open(file, 'wb') as f:
    pickle.dump(tickers, f)
