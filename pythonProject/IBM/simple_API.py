# from pycoingecko import CoinGeckoAPI
# import pandas as pd
# cg=CoinGeckoAPI()
# bit_coin=cg.get_coin_market_chart_by_id(id='bitcoin',vs_currency='usd',days=30)
# bit_coin_data=bit_coin['prices']
# seq.txt=pd.DataFrame(bit_coin_data,columns=['TimeStamp','Prices'])
# seq.txt['Date']=pd.to_datetime(seq.txt['TimeStamp'],unit='ms')
# print(seq.txt.head())
# candle_stick=seq.txt.groupby(seq.txt.Date.dt.date).agg({'Prices':['min','max','first','last']})