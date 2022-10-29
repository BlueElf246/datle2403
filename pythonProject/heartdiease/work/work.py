import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('Test.csv')
def analyse():
    #grab the column detail
    columns_name=df.columns.values.tolist()
    print(columns_name)
    # grab the data-type of each columns
    datatype=df.dtypes
    print(datatype)
def null_value():
    print(df.info())
    # null value in here is zero(0)
def value_count():
    columns_name = df.columns.values.tolist()
    for x in columns_name:
        print(df[x].describe())
def null_resting_BP():
    v=df['RestingBP']==0
    #print(len(df[v]))
    #value=df['RestingBP'].value_counts()
    avg=df['RestingBP'].astype('float').mean(axis=0)
    df['RestingBP'].replace(0,avg,inplace=True)
    #most common value
    common=df['RestingBP'].value_counts().idxmax()
null_resting_BP()
def null_Cholesterol():
    #count how many 0
    num=len(df[df['Cholesterol']==0])
    avg=df['Cholesterol'].astype('float').mean(axis=0)
    df['Cholesterol'].replace(0,avg,inplace=True)
null_Cholesterol()
def plot():
    bin=np.linspace(min(df['Age']),max(df['Age']), 4)
    group_name=['youth','adult','senoir']
    df['Age-binned']=pd.cut(df['Age'],bins=bin,labels=group_name,include_lowest=True)
    plt.hist(df['Age-binned'])
plot()
def age_normalized():
    df['Age']/=df['Age'].max()
age_normalized()
def Old_peak_normalized():
    df['Oldpeak']/=df['Oldpeak'].max()
Old_peak_normalized()
def RestingBP_normalized():
    df['RestingBP']/=df['RestingBP'].max()
RestingBP_normalized()
def Cholesterol():
    df['Cholesterol'] /= df['Cholesterol'].max()
Cholesterol()
def MaxHR():
    df['MaxHR']/=df['MaxHR'].max()
MaxHR()
def one_hot():
    dummy_Sex=pd.get_dummies(df['Sex'])
    dummy_ChestPainType=pd.get_dummies(df['ChestPainType'])
    dummy_ST_slope=pd.get_dummies(df['ST_Slope'])
    dummy_Age_binned=pd.get_dummies(df['Age-binned'])
    dummy_RestingECG=pd.get_dummies(df['RestingECG'])
    dummy_ExerciseAngina=pd.get_dummies(df['ExerciseAngina'])
    df2=pd.concat([df,dummy_Sex,dummy_ST_slope,dummy_Age_binned,dummy_ChestPainType,dummy_RestingECG,dummy_ExerciseAngina],axis=1)
    df4=df2['ID']
    df4.to_csv('IDfile_Test.csv')
    df2.drop(['Sex', 'ChestPainType', 'ST_Slope', 'Age-binned','ExerciseAngina','RestingECG','ID'], axis=1,inplace=True)
    df2.to_csv('final_test.csv')
    print(df2)
one_hot()
