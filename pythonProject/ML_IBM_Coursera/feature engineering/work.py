import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
# load the data, examine and explore
df=pd.read_csv('Ames_Housing_Data.tsv',sep='\t')
# khao sat dataset
def thong_tin_columns(dataset):
    print(dataset.columns.tolist())
def thong_tin_loai_du_lieu(dataset):
    print(dataset.dtypes)
def info_dataset(dataset):
    print(dataset.info())
def corr_cua_att_voi_ylabel(dataset):
    numerice_type=dataset.select_dtypes(['int64','float64'])
    corr=numerice_type.corr()['SalePrice'][:-1]
    top=corr[abs(corr)>0.5]
    top=top.index.tolist()
    print(top)
    return top
def plot_normal_distribution(dataset):
    sns.distplot(dataset['SalePrice'])
    plt.show()
def plot_att_vs_ylabel(dataset):
    price_area=dataset.plot.scatter(x='Lot Area',y='SalePrice')
    plt.show()
def plot(dataset,top):

    for x in top:
        dataset.plot.scatter(x=x,y='SalePrice')
    plt.show()
def remove_outlier(df):
    df=df.loc[df['Gr Liv Area'] <= 4000,:]
    data=df.copy()
    return df,data
# converting categorical variable into dummies
# make skew variable symmetric
def onehot(df,data):
    one_hot_encode_cols= df.dtypes[df.dtypes== np.object]
    one_hot=one_hot_encode_cols.index.tolist()
    df=pd.get_dummies(df,columns=one_hot,drop_first=True)
    mask= data.dtypes==np.float
    float_col_name= data.columns[mask]
    skew_limit=0.75
    skew_val=data[float_col_name].skew()
    skew_cols = (skew_val
                 .sort_values(ascending=False)
                 .to_frame()
                 .rename(columns={0: 'Skew'})
                 .query('abs(Skew) > {}'.format(skew_limit)))
    return df,skew_cols
def plot_1(df):
    field = "BsmtFin SF 1"

    # Create two "subplots" and a "figure" using matplotlib
    fig, (ax_before, ax_after) = plt.subplots(1, 2, figsize=(10, 5))

    # Create a histogram on the "ax_before" subplot
    df[field].hist(ax=ax_before)

    # Apply a log transformation (numpy syntax) to this column
    df[field].apply(np.log1p).hist(ax=ax_after)

    # Formatting of titles etc. for each subplot
    ax_before.set(title='before np.log1p', ylabel='frequency', xlabel='value')
    ax_after.set(title='after np.log1p', ylabel='frequency', xlabel='value')
    fig.suptitle('Field "{}"'.format(field))
    plt.show()


df,data=remove_outlier(df)
df, skew_colms=onehot(df,data)
def transform_overskewed(df,skew_col):
    for col in skew_col.index.values:
        if col=='SalePrice':
            continue
        df[col]=df[col].apply(np.log1p)
    return df
df=transform_overskewed(df,skew_colms)

df = data

def run(df):
    smaller_df= df.loc[:,['Lot Area', 'Overall Qual', 'Overall Cond',
                          'Year Built', 'Year Remod/Add', 'Gr Liv Area',
                          'Full Bath', 'Bedroom AbvGr', 'Fireplaces',
                          'Garage Cars','SalePrice']]
    smaller_df = smaller_df.fillna(0)
    return smaller_df
smaller_df=run(df)


def add_deviation_feature(X, feature, category):
    # temp groupby object
    category_gb = X.groupby(category)[feature]

    # create category means and standard deviations for each observation
    category_mean = category_gb.transform(lambda x: x.mean())
    category_std = category_gb.transform(lambda x: x.std())

    # compute stds from category mean for each feature value,
    # add to X as new feature
    deviation_feature = (X[feature] - category_mean) / category_std
    X[feature + '_Dev_' + category] = deviation_feature


def run1(smaller_df,data):
    X = smaller_df.loc[:, ['Lot Area', 'Overall Qual', 'Overall Cond',
                           'Year Built', 'Year Remod/Add', 'Gr Liv Area',
                           'Full Bath', 'Bedroom AbvGr', 'Fireplaces',
                           'Garage Cars']]

    y = smaller_df['SalePrice']
    X2 = X.copy()

    X2['OQ2'] = X2['Overall Qual'] ** 2
    X2['GLA2'] = X2['Gr Liv Area'] ** 2
    X3 = X2.copy()

    # multiplicative interaction
    X3['OQ_x_YB'] = X3['Overall Qual'] * X3['Year Built']

    # division interaction
    X3['OQ_/_LA'] = X3['Overall Qual'] / X3['Lot Area']
    pd.get_dummies(data['House Style'], drop_first=True).head()
    nbh_counts = data.Neighborhood.value_counts()
    other_nbhs= list(nbh_counts[nbh_counts<=8].index)
    X4 = X3.copy()

    X4['Neighborhood'] = data['Neighborhood'].replace(other_nbhs, 'Other')
    X5 = X4.copy()
    X5['House Style'] = df['House Style']
    add_deviation_feature(X5, 'Year Built', 'House Style')
    add_deviation_feature(X5, 'Overall Qual', 'Neighborhood')
    pf = PolynomialFeatures(degree=2)
    features = ['Lot Area', 'Overall Qual']
    pf.fit(X5[features])
    print(X5)
    return X5
X5=run1(smaller_df,data)
def onhot_X5(X5):
    one_hot_encode_cols = X5.dtypes[X5.dtypes == np.object]
    one_hot = one_hot_encode_cols.index.tolist()
    X5=pd.get_dummies(X5, columns=one_hot, drop_first=True)
    print(X5)
onhot_X5(X5)



