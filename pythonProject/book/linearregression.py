import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model
import os
import tarfile
from six.moves import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing") # use for save the data in given directory
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz" #use to download the dataset

def fetchdata(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path): # check if directory exist
        os.makedirs(housing_path) # create the directory
    tgz_path=os.path.join(housing_path,'housing.tgz')
    urllib.request.urlretrieve(housing_url,tgz_path)# download the file from housing_url and save at tgz_path
    housing_tgz=tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path) # extract the tgz file to given path
    housing_tgz.close()

def load_housing_data():
    csv_path=os.path.join(HOUSING_PATH,'housing.csv')
    return pd.read_csv(csv_path)
df=load_housing_data()
def info(df): # use to see the number of columns, data type and number of non-null
    print(df.info())
def info_feature(df,feature_name): # category of that feature and its appearances
    print(df[feature_name].value_counts())
def describe_data(df):# describe the data set numberically
    print(df.describe())
    #std mean standared deviation, 68-95-99.7
    # 25% mean 25% of the dataset will have that value < 25%(value)
info(df)
def plot_histogram(df,feature_name=None,bin=50):
    # vectical axis: number of instance at that value
    if feature_name == None:
        df.hist(bins=50, figsize=(20,15))
    else:
        df[feature_name].hist(bins=bin)
    plt.show()



from zlib import crc32
def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32
def split_train_test_by_id(data, test_ratio, id_column):
    ids=data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]

df["income_cat"] = pd.cut(df["median_income"],
                                   bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
labels=[1, 2, 3, 4, 5])


from sklearn.model_selection import StratifiedShuffleSplit
split=StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(df, df["income_cat"]):
    strat_train_set = df.loc[train_index]
    strat_test_set = df.loc[test_index]
for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis=1, inplace=True)


# NOW WE HAVE TRAIN AND TEST SET:
dft=strat_train_set.copy()

# visualizing geometrical data
def visualizing(df,x,y):
    df.plot(kind='scatter',x=x,y=y,alpha=0.1)
    #alpha make the density clearer
    plt.show()

def visualizing_with_feature(df,x,y,feature1,feature2):
    df.plot(kind='scatter',x=x,y=y, alpha=0.4, s=df[feature1]/100,label='population',c=df[feature2],cmap=plt.get_cmap('jet'),colorbar=True)
    plt.show()
#visualizing_with_feature(dft,'longitude','latitude','population','median_house_value')

def correlation(df,y):
    corr=df.corr()
    print(corr[y].sort_values(ascending=False))
    # positive corr
    # negative corr
    # no corr (=0)
# correlation(dft,'median_house_value')

from pandas.plotting import scatter_matrix
def plot_correlation(df,attribute):
    scatter_matrix(df[attribute])
    plt.show()
attributes = ["median_house_value", "median_income", "total_rooms","housing_median_age"]

# WE WILL COMBINE THE FEATURE
def combine_feture(df,new,x,y):
    df[new]=df[x]/df[y]
combine_feture(dft,'rooms_per_household','total_rooms','households')
combine_feture(dft,'bedrooms_per_household','total_bedrooms','households')
combine_feture(dft,'population_per_household','population','households')



housing=strat_train_set.drop('median_house_value',axis=1)
housing_label=strat_train_set['median_house_value'].copy()
def fill_nan(df,feature,option=None):
    if option==1: # drop the x if its feature is nan
        df.dropna(subset=[feature])
    if option==2: # drop the whole column
        df.drop(feature,axis=1)
    if option==3:
        median=df[feature].median()
        df[feature].fillna(median,inplace=True)
from sklearn.impute import SimpleImputer

def fill_nan_using_impute_method(df,strategy='median',object=None):
    #this method only apply for numebrical dataset
    df_num=df.drop(object,axis=1)
    impute=SimpleImputer(strategy=strategy)
    impute.fit(df_num)
    print(impute.statistics_)
    #fill nan
    X=impute.transform(df_num)
    # convert numpy array to dataframe
    df=pd.DataFrame(X,columns=df_num.columns)
    print(df)
    return df
#fill_nan_using_impute_method(housing,object='ocean_proximity')



# WE WILL CONVERT OBJECT TO NUMBER
# USING ORDINAL ENCODER
from sklearn.preprocessing import OrdinalEncoder
def encoding(df,feature):
    # IT IS ONLY FOR ASCENDING CATEGORY SUCH AS LOW, MEDIUM, HIGH
    df_feature=df[[feature]]
    ordinal_encoder = OrdinalEncoder()
    df_feature_encoded = ordinal_encoder.fit_transform(df_feature)
    print(df_feature_encoded)
    print(ordinal_encoder.categories_)
from sklearn.preprocessing import OneHotEncoder
def one_hot_encoding(df,feature):
    # IT IS USE FOR INDEPENDENT CATEGORY
    cat_encoder=OneHotEncoder()
    df_feature=df[[feature]]
    df_one_hot=cat_encoder.fit_transform(df_feature)
    print(df_one_hot)
    #sparse row format: save up memory instead of saving zero
    print(cat_encoder.categories_)
#one_hot_encoding(housing,'ocean_proximity')

# FEATURE SCALING
# TWO METHOD ARE MIX_MAX SCALING AND STANDARDIZATION
# 2ND METHOD LESS AFFECT BY THE OUTLIERS

from sklearn.base import BaseEstimator, TransformerMixin
rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6
class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True): # no *args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room
    def fit(self, X, y=None):
        return self # nothing else to do
    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household,bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]
# attr_adder = CombinedAttributesAdder(add_bedrooms_per_room=False)
# housing_extra_attribs = attr_adder.transform(housing.values)

# TRANSFORMATION PIPELINE
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer


num_pipeline= Pipeline([
    ('imputer',SimpleImputer(strategy='median')),
    ('attribs_adder',CombinedAttributesAdder()),
    ('std_scaler',StandardScaler()),
])
housing_num=housing.drop(['ocean_proximity'],axis=1)

num_att=list(housing_num)
cat_att=['ocean_proximity']
full_pipeline= ColumnTransformer([
    ('num',num_pipeline,num_att),
    ('cat',OneHotEncoder(),cat_att)
])


housing_prepared=full_pipeline.fit_transform(housing)

#MAKE PREDICTION
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(housing_prepared,housing_label)
print(len(housing_prepared[0]))

some_data=housing.iloc[:5]
some_label=housing_label.iloc[:5]
some_data_prepared=full_pipeline.transform(some_data)
print(lin_reg.predict(some_data_prepared))
print(list(some_label))

housing_prediction=lin_reg.predict(housing_prepared)
from sklearn.metrics import mean_squared_error
lin_mse=mean_squared_error(housing_label,housing_prediction)
lin_mse=np.sqrt(lin_mse)
print(lin_mse)











