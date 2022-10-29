import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df=pd.read_csv(path)
def run():
    print(df['peak-rpm'].dtypes)
    d=df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr()
    print(d)
def run1():
    #sns.regplot(x='engine-size', y='price',data=df)
    #sns.regplot(x="highway-mpg", y="price", data=df)
    plt.ylim(0,)
    plt.show()
    d=df[["engine-size", "price"]].corr()
    e = df[["highway-mpg", "price"]].corr()
    print(e)
def run2():
    print(df[['stroke','price']].corr())
    #sns.regplot(x='stroke',y='price',data=df)
    #sns.boxplot(x="body-style", y="price", data=df)
    #sns.boxplot(x="engine-location", y="price", data=df)
    sns.boxplot(x="drive-wheels", y="price", data=df)
    plt.show()
def run3():
    print(df['drive-wheels'].unique())
    df_group_one = df[['drive-wheels', 'body-style', 'price']]
    df_group_one = df_group_one.groupby(['drive-wheels'], as_index=False).mean()
    print(df_group_one)
    df_gptest = df[['drive-wheels', 'body-style', 'price']]
    grouped_test1 = df_gptest.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
    print(grouped_test1)
    grouped_pivot = grouped_test1.pivot(index='drive-wheels', columns='body-style')
    print(grouped_pivot)
    # plt.pcolor(grouped_pivot, cmap='RdBu')
    # plt.colorbar()
    # plt.show()
    fig, ax = plt.subplots()
    im = ax.pcolor(grouped_pivot, cmap='RdBu')

    # label names
    row_labels = grouped_pivot.columns.levels[1]
    col_labels = grouped_pivot.index

    # move ticks and labels to the center
    ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
    ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

    # insert labels
    ax.set_xticklabels(row_labels, minor=False)
    ax.set_yticklabels(col_labels, minor=False)

    # rotate label if too long
    plt.xticks(rotation=90)

    fig.colorbar(im)
    plt.show()
def run4():
    df_p=df[['body-style','price']]
    df_p=df_p.groupby(['body-style'],as_index=False).mean()
    print(df_p)
def run5():
    pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
    print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)
    pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
    print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)
    pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
    print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)
    pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
    print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)
    pearson_coef, p_value = stats.pearsonr(df['curb-weight'], df['price'])
    print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)
    pearson_coef, p_value = stats.pearsonr(df['engine-size'], df['price'])
    print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)
    pearson_coef, p_value = stats.pearsonr(df['bore'], df['price'])
    print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =  ", p_value)
    pearson_coef, p_value = stats.pearsonr(df['bore'], df['price'])
    print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =  ", p_value)
run5()
