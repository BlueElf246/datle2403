import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

from scipy.stats import norm
from scipy import stats

# reading and understanding our data
housing=pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML0232EN-SkillsNetwork/asset/Ames_Housing_Data1.tsv', sep='\t')
print(housing.info())
print(housing['SalePrice'].describe())
# the distance between min and 25%, max and 75% are too big. this means that
# our data might not be normally distributed

# describe all category of attribute Sale condition
print(housing['Sale Condition'].value_counts())

hous_num=housing.select_dtypes(include=['float64','int64'])
print(hous_num.info())
hous_num_corr=hous_num.corr()['SalePrice'][:-1]
top_feature=hous_num_corr[abs(hous_num_corr)>0.5].sort_values(ascending=False)
print(top_feature)
def show_corr():
    for i in range(0, len(hous_num.columns),5):
        sns.pairplot(data=hous_num,x_vars=hous_num.columns[i:i+5], y_vars=['SalePrice'])
    plt.show()
#sp_intransformed=sns.distplot(housing['SalePrice'])

print(housing['SalePrice'].skew())
log_transformed= np.log(housing['SalePrice'])
#sp_transformed= sns.distplot(log_transformed)
print(housing['Lot Area'])
#distribution= sns.distplot(housing['Lot Area'])
print(housing['Lot Area'].skew())
log=np.log(housing['Lot Area'])
print(housing['SalePrice'].describe())
#sns.distplot(log)

duplicate= housing[housing.duplicated(['PID'])]
print(duplicate)
# dup=housing.drop_duplicates()
removed_sub = housing.drop_duplicates(subset=['Order'])
print(removed_sub)
def plot():
    total = housing.isnull().sum().sort_values(ascending=False)
    total_select = total.head(20)
    total_select.plot(kind="bar", figsize = (8,6), fontsize = 10)

    plt.xlabel("Columns", fontsize = 20)
    plt.ylabel("Count", fontsize = 20)
    plt.title("Total Missing Values", fontsize = 20)
    plt.show()
print(housing['Mas Vnr Area'].isnull().sum())
print(housing['Mas Vnr Area'].dtype)
print(housing['Mas Vnr Area'].median())
housing['Mas Vnr Area'].fillna(housing['Mas Vnr Area'].median(),inplace=True)

# scale/ normalize the value
hous_num=housing.select_dtypes(include=['float64','int64'])
norm_data=MinMaxScaler().fit_transform(hous_num)

norm_sale=MinMaxScaler().fit_transform(housing['SalePrice'][:,np.newaxis])
print(norm_sale)

#sns.boxplot(x=housing['SalePrice'])
print(housing['Gr Liv Area'].corr(housing['SalePrice']))

m=housing.sort_values(by='Gr Liv Area', ascending=False)[:2]
housing.drop(housing.index[[1499,2181]],inplace=True)
price_area = housing.plot.scatter(x='Lot Area',
                      y='SalePrice')
plt.show()