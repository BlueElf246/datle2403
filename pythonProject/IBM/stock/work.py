import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
apple=yf.Ticker('AAPL')
def run1():
    #get the information about info of stock
    apple_info=apple.info
    country_of_stock=apple_info['country']
    long_business_summary=apple_info['longBusinessSummary']

def run2():
    apple_share_price_data=apple.history(period='max')
    #reset index co nghia la index cua 1 row bat ki la so 1,2,3...
    #chu khong phai la Date
    apple_share_price_data.reset_index(inplace=True)
    apple_share_price_data.plot(x='Date',y='Open')
def run3():
    #extrating_shared_price
    div=apple.dividends
    div.plot()
    plt.show()
    print(div)
def run4():
    amd=yf.Ticker('AMD')
    amd_info=amd.info
    print(amd_info['country'])
    print(amd_info['sector'])
    amd_history=amd.history(period='max')
    print(amd_history.head(0))
run4()
