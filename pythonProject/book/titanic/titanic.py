import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import tensorflow.keras as keras
import  numpy as np
NUMBERIC_COLUMNS = ["age", "n_siblings_spouses", "parch", "fare"]

def load_dataset():
    train=pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv')
    test=pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv')
    train1=train.copy()
    test1=test.copy()
    y_train=train['survived']
    train.drop(['survived'],axis=1,inplace=True)
    x_train =train
    y_test = test['survived']
    test.drop(['survived'], axis=1, inplace=True)
    x_test =test

    x_train.to_csv('x_train.csv')
    x_test.to_csv('x_test.csv')
    y_train.to_csv('y_train.csv')
    y_test.to_csv('y_test.csv')
    return train1,test1,x_train,y_train,x_test,y_test

train,test, x_train,y_train,x_test,y_test=load_dataset()


def info(df): # use to see the number of columns, data type and number of non-null
    print(df.info())
def info_feature(df,feature_name): # category of that feature and its appearances
    print(df[feature_name].value_counts())
def describe_data(df):# describe the data set numberically
    print(df.describe())
    #std mean standared deviation, 68-95-99.7
    # 25% mean 25% of the dataset will have that value < 25%(value)
def plot_histogram(df,feature_name=None,bin=50):
    # vectical axis: number of instance at that value
    if feature_name == None:
        df.hist(bins=50)
    else:
        df[feature_name].hist(bins=bin)
        plt.xlabel(feature_name)
        plt.ylabel(f'The number of {feature_name}')
    plt.show()

def plot_histogram_for_text_category(df,feature_name=None,bin=50):
    if feature_name == None:
        df.value_counts().plot(kind='barh')
    else:
        df[feature_name].value_counts().plot(kind='barh')
        plt.ylabel(feature_name)
        plt.xlabel(f'The number of {feature_name}')
    plt.show()



def visualizing(df,x,y):
    df.plot(kind='scatter',x=x,y=y,alpha=0.1)
    #alpha make the density clearer
    plt.show()
def correlation(df,y):
    corr=df.corr()
    print(corr[y].sort_values(ascending=False))
    # positive corr
    # negative corr
    # no corr (=0)
from pandas.plotting import scatter_matrix
def plot_correlation(df,attribute):
    scatter_matrix(df[attribute])
    plt.show()
def show_data_head(df):
    print(df.head())

# cac buoc thuc hien
# data visualization
category_columns = ["sex", "class", "deck", "embark_town", "alone"]
numberic_columns = ["age", "n_siblings_spouses", "parch", "fare",'survived']
def visualize():
    show_data_head(train)

    # describe numerical data
    describe_data(df=x_train)

    # plot category columns
    # bar plots
    for x  in category_columns:

        sns.countplot(x=x,data=train,palette='husl')
        plt.show()
    # plot numerical columns

    plot_histogram(train,numberic_columns)
    plt.show()
    correlation(train[numberic_columns],'survived')
    plot_correlation(train,numberic_columns)

# clean data
num_pipeline=Pipeline([
    ('std_scaler',StandardScaler())
])
full_pipeline=ColumnTransformer([
    ('num',num_pipeline,NUMBERIC_COLUMNS),
    ('cat',OneHotEncoder(),category_columns),
])
x_train_prepared=full_pipeline.fit_transform(x_train)
print(x_train_prepared)

def linear_regression(x,y):
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error
    lin_reg=LinearRegression()
    lin_reg.fit(x,y)

    x_train_prediction=lin_reg.predict(x)
    lin_mse=mean_squared_error(y,x_train_prediction)
    lin_mse=np.sqrt(lin_mse)
    print(lin_mse)
    print(x_train_prediction[:5])
    print(y_train[:5])

def dnn(x,y):
    import tensorflow as tf
    class myCallback(tf.keras.callbacks.Callback):
        def on_epoch_end(self, epoch, logs={}):
            if (logs.get('accuracy') > 0.95):
                print("\nReached 95% accuracy so cancelling training!")
                self.model.stop_training = True

    callback = myCallback()
    base_model = keras.Sequential([
        keras.layers.Dense(30, activation='relu', input_shape=x.shape[1:]),
        keras.layers.Dense(10, activation='relu'),
        keras.layers.Dense(1, activation='sigmoid')  # For binary classification, please refer slide to double check
    ])
    base_model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
    base_model.fit(x, y, callbacks=[callback], epochs=1000)
    x_test_prepared=full_pipeline.transform(x_test)
    base_model.evaluate(x_test_prepared,y_test)
    prediction=base_model.predict(x_test_prepared)
    print(prediction[:5])
    print(y_test[:5])
# dnn(x_train_prepared,y_train)





