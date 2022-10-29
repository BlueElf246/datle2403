import pandas.io.sql as pds
import sqlite3 as sq3
con=sq3.Connection('baseball.db')
df=pds.read_sql('select * from allstarfull',con)
print(df)