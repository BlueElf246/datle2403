import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.utils import shuffle
from pandas.plotting import scatter_matrix
#url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df=pd.read_csv('auto_mobile.csv')
# df.drop(columns=df.columns[0],axis=1,inplace=True)
# df.columns=["symboling", "normalized-losses", "make", "fuel-type",
#               "aspiration", "num-of-doors", "body-style", "drive-wheels",
#               "engine-location","wheel-base", "length", "width",
#               "height","curb-weight","engine-type","num-of-cylinders",
#               "engine-size","fuel-system","bore","stroke",
#               "compression-ratio","hourse-power","peak-rpm","city-mpg",
#               "highway-mpg","price"]
# df.to_csv('auto_mobile.csv')
CATEGORICAL_COLUMN_NAMES=["make","fuel-type","aspiration","body-style",
                          "drive-wheels","engine-location",
                          "engine-type","fuel-system",]

CATEGORY_2_NUMBER_NAMES=["num-of-doors","num-of-cylinders"]

NUMBERIC_COLUMN_NAMES=["symboling","normalized-losses",
                       "wheel-base","length","width",
                       "height","curb-weight","engine-size",
                       "bore","stroke","compression-ratio",
                       "peak-rpm","city-mpg","highway-mpg","price"]
def data_description():
    #print head
    print('5 first row of df\n',df.head(5))
    # print info
    print(df.info())
    # value count of feature
    for x in CATEGORY_2_NUMBER_NAMES:
        print(df[x].value_counts())
    print('there are 2 missing values in num-of-doors ')
    for x in CATEGORICAL_COLUMN_NAMES:
        print(df[x].value_counts())
    for x in NUMBERIC_COLUMN_NAMES:
        print(df[x].value_counts())
#print(df.loc[df['num-of-doors']=='?','num-of-doors']) # print row, where (df['num-of-doors']=='?') and at column num-of-door
def fill_missing_value():
    for x in NUMBERIC_COLUMN_NAMES:
        df.loc[df[x]=='?', x]=np.NaN
        df.loc[:,x].fillna(df[x].median(),inplace=True) # fill nan value at all row at feature x
        df.loc[:,x]=df.loc[:,x].astype('float64')
    for x in CATEGORICAL_COLUMN_NAMES:
        highes_frequent=df[x].mode()
        df.loc[df[x]=='?',x]=np.NaN
        df.loc[:,x].fillna(highes_frequent,inplace=True)
    for x in CATEGORY_2_NUMBER_NAMES:
        highes_frequent = df[x].mode()
        df.loc[df[x] == '?', x] = np.NaN
        df.loc[:, x].fillna(highes_frequent, inplace=True)
fill_missing_value()
def display_data_histogram_for_continuous_value():
    df.hist(bins=50, figsize=(20,15))
    plt.show()
def corr_matrix():
    corr=df.corr()
    print(corr['price'].sort_values(ascending=False))
    #plot corr
    attributes = ["price", "engine-size", "curb-weight", "width", "length", "city-mpg", "highway-mpg",
                  "compression-ratio"]
    scatter_matrix(df[attributes], figsize=(12, 8))
    plt.show()
corr_matrix()
def display_category_data():
    for x in CATEGORICAL_COLUMN_NAMES:
        sns.countplot(x=df[x],order=df[x].value_counts(ascending=True).index)
        plt.show()
def display_category_data_with_continuous_label():
    for x in CATEGORICAL_COLUMN_NAMES:
        sns.boxplot(data=df,y='price',x=x)
        plt.show()
fill_missing_value()
def assign1():
    #Show 2 records of the highest and lowest price ( 2 points)
    print(df['price'].max(),df['price'].min())
def assign2():
    #Show records of top 5 city-mpg cars (2 points)
    l=df['city-mpg'].sort_values(ascending=False)
    l=l[0:5].unique()
    print(l)
    for x in l:
        print(df.loc[df['city-mpg'] ==x])
def assign3():
    #Show records of 5 random Poscher cars (2 points)
    m=df[df['make']=='porsche']
    print(m)
def assign4():
    #Filter a subset of data where price > 30k $ (2 points)
    m = df[df['price'] >30000]
    print(m)
def assign5():
    #Group this data into groups base on engine-type ( 2 points)
    m=df.groupby(['engine-type'])
    print(m)
def assign6():
    m = df.groupby(by=['body-style'],axis=0).count()
    print(m)
def assign7():
    #Create a new 'feature' or column named area so that area = width*height ( 2 points)
    df['area']=df['width']*df['height']
assign7()
def assign8():
    #Verify correlation between area and price ( 2 points)
    corr=df.corr()
    print(corr['price']['area'])
assign6()