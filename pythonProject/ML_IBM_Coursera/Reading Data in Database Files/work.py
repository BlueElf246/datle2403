import sqlite3 as sq3
import pandas.io.sql as pds
import pandas as pd
path='classic_rock.db'
con=sq3.Connection(path)
query="""Select * from rock_songs"""
query1="""Select Artist, Release_Year, count(*) as num_song, avg(PlayCount)  from rock_songs group by Artist, Release_Year
"""
query2="""select * from rock_songs where Artist='3 Doors Down'"""
def query_1(text):
    observation = pds.read_sql(text, con)
    print(observation)
def query_2(text):
    observation = pds.read_sql(text, con, parse_dates=['Release_Year'],chunksize=5)
    for index, observation in enumerate(observation):
        if index <5:
            print(observation)
query_2(query)