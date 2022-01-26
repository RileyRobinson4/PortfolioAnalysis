import lookup_portfolio
from lookup_portfolio import GetPositions
import re
import json
import csv
from io import StringIO
#import pandas_datareader as pdr
#pdr.get_data_fred('GS10')

#from bankroll.interface import *
#from decimal import Decimal
#from ib_insync import IB, util
#import logging
##
#import pyfolio
#
#util.startLoop()
#
#accounts = AccountAggregator.fromSettings(AccountAggregator.allSettings(loadConfig()), lenient=False)
#print (accounts.positions())
#frame = positions_to_dataframe(accounts.positions())
#positions, frame, historical_data = positions_to_history(marketDataProvider(accounts), accounts.positions(), frame)
#portfolio = positions_to_portfolio(frame, historical_data, 'America/New_York')
#returns = positions_to_returns(marketDataProvider(accounts), positions, 'America/New_York')
## To ignore pyfolio deprecated function warnings
#import warnings
#warnings.filterwarnings('ignore')
#
#import pyfolio as pf
#pf.create_returns_tear_sheet(returns, benchmark_rets=None)
#
#portfolio = lookup_portfolio.lookup_portfolio()

#import csv
#with open('portfolioData/Portfolio_Positions_Jan-22-2022.csv', newline='') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#    for row in spamreader:
#        print(', '.join(row))

csvPorfolio = 'portfolioData/Portfolio_Positions_Jan-26-2022.csv'

positions = GetPositions(csvPorfolio)

p = {k: v for k, v in sorted(positions.items(), key=lambda item: item[1])}

print('Printing Positons')
for key, value in p.items():
    print(key, value)
