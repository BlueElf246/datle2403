import pandas as pd
import numpy as np
other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df=pd.read_csv('auto.csv',header=None)
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns=headers
df1=df.replace('?',np.NaN)
# drop NaN value in 'price' column
df=df1.dropna(subset=['price'],axis=0)
# print(df)
# print(df.columns)
#df.to_csv('automobile.csv',index=False)
# print(df.dtypes)
df.describe()
print(df.info())
