import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
x=pd.read_csv('final.csv')
y=pd.read_csv('y_label.csv')
test=pd.read_csv('final_test.csv')
x=x.iloc[:, 1:]
y=y.iloc[:, 1:]
test=test.iloc[:,1:]
knn=KNeighborsClassifier(algorithm='auto',n_neighbors=7,weights='distance')
knn.fit(x,y)
y_pred=knn.predict(x)
y_test_pred=knn.predict(test)
# print(classification_report(y,y_pred))
# print(y_pred)
df=pd.DataFrame()
df10=pd.read_csv('IDfile_Test.csv')
df10=df10.iloc[:, 1:]
df['HeartDisease']=y_test_pred
df3=pd.concat([df10,df],axis=1)
df3.to_csv('nop_test.csv')