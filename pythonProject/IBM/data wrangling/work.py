import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib import pyplot
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
# read_csv and replace columns name by headers
df=pd.read_csv('auto.csv',names=headers)
# replace '?' by Nan
df.replace('?',np.NaN,inplace=True)
# return the T/F df
missing_data = df.isnull()
print(df.columns)
#missing_data.columns.values.tolist(): list of name of columns
def count_Nan():
    # missing_data[col].value_counts(): counts how many T/F
    missing_data = df.isnull()
    for col in missing_data.columns.values.tolist():
        print(col)
        print(missing_data[col].value_counts())

def replace_Nan_value():
    #check type of column
    #print(df['normalized-losses'].dtypes)
    #change column type
    avg=df['normalized-losses'].astype('float').mean(axis=0)
    df['normalized-losses'].replace(np.NaN, avg, inplace=True)
    avg_bore=df['bore'].astype('float').mean(axis=0)
    df['bore'].replace(np.NaN,avg_bore,inplace=True)
    avg_stroke=df['stroke'].astype('float').mean(axis=0)
    df['stroke'].replace(np.NaN, avg_stroke, inplace= True)
    avg_horse=df['horsepower'].astype('float').mean(axis=0)
    df['horsepower'].replace(np.NaN, avg_horse, inplace=True)
    avg_peakrpm = df['peak-rpm'].astype('float').mean(axis=0)
    df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)
    #print(df['num-of-doors'].value_counts())
    # return the most common type
    common=df['num-of-doors'].value_counts().idxmax()
    df['num-of-doors'].replace(np.NaN,common,inplace=True)
    # drop all the row the don't have price
    df.dropna(subset=['price'],axis=0,inplace=True)
    # reset index, because we drroped two rows
    df.reset_index(drop=True, inplace= True)

replace_Nan_value()
def format_data_type():
    df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
    df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
    df[["price"]] = df[["price"]].astype("float")
    df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")
format_data_type()
def data_standardization():
    # Convert mpg to L/100km by mathematical operation (235 divided by mpg)
    df['city-L/100km'] = 235 / df["city-mpg"]
    df['highway-mpg']=235/df['highway-mpg']
    df.rename(columns={"'highway-mpg'":'highway-L/100km'},inplace=True )
    # check your transformed data
data_standardization()
def data_normalization():
    df['length']=df['length']/df['length'].max()
    df['width'] = df['width'] / df['width'].max()
    df['height']/=df['height'].max()
data_normalization()
def data_binning():
    df['horsepower']=df['horsepower'].astype(int, copy=True)
    # pyplot.hist(df['horsepower'])
    bins=np.linspace(min(df['horsepower']), max(df['horsepower']),4)
    group_names = ['Low', 'Medium', 'High']
    df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True)
    # print(df[['horsepower', 'horsepower-binned']].head(20))
    # print(df['horsepower-binned'].value_counts())
    #pyplot.bar(group_names, df["horsepower-binned"].value_counts())
    # print(bins)
    # pyplot.hist(df["horsepower"], bins=3)
    # plt.show()
data_binning()
def one_hot():

    dummy_variable_1 = pd.get_dummies(df["fuel-type"])
    dummy_variable_1.rename(columns={'gas': 'fuel-type-gas', 'diesel': 'fuel-type-diesel'}, inplace=True)
    df = pd.concat([df, dummy_variable_1], axis=1)
    # drop original column "fuel-type" from "df"
    df.drop("fuel-type", axis=1, inplace=True)
    dummy2=pd.get_dummies(df['aspiration'])
    print(dummy2)
    df=pd.concat([df,dummy2],axis=1)
    df.drop('aspiration', axis=1,inplace=True)

one_hot()




