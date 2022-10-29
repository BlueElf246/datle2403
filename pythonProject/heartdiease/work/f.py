import pandas as pd
df=pd.read_csv('nop_test.csv')
df=df.iloc[:,1:]
print(df)