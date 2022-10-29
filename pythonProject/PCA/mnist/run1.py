import numpy as np
from sklearn.datasets import fetch_openml
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
f = plt.figure()
f.set_figwidth(100)
f.set_figheight(100)
def standardized(dataset):
    scaler = StandardScaler()
    scaler.fit(dataset)
    dataset = scaler.transform(dataset)
    return dataset
def create_dataset(num):
    df=pd.read_csv('mnist_784_csv.csv')
    df_num=df[df['class']==num]
    x=df_num.drop('class',axis=1).to_numpy()
    return x
def pca(data,num):
    pca = PCA(n_components=num) # 95% of variance equal to 330 Principal component
    pca.fit(data)
    data = pca.transform(data)
    print(np.sum(pca.explained_variance_ratio_) )
    return data
def write(data):
    with open("output.txt", "w") as txt_file:
        for line in data:
            txt_file.write(" ".join(str(line)) + "\n")
def split(data,n):
    data=np.array(data).T
    x=data[0][:n]
    y=data[1][:n]
    return x,y
def present(x,y):
    plt.plot(x, y, 'o')
def run(num,percent):
    x=create_dataset(num)
    x=standardized(x)
    data=pca(x,2)
    num_datapint=int(data.shape[0]*percent)
    x,y=split(data,num_datapint)
    present(x,y)
run(5,0.5)
run(6,0.5)
plt.show()