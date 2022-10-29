import pandas as pd
info_train=pd.read_csv('info_train.csv')
work_train=pd.read_csv('work_train_1.csv')
info_test=pd.read_csv('info_test.csv')
work_test=pd.read_csv('work_test_1.csv')




work_train.drop(['bithYear','gender'],axis=1,inplace=True)
work_train = pd.merge(work_train,info_train, on="id_bh")
work_train.drop(work_train.columns[work_train.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
work_train.to_csv('work_train_2.csv')

work_test.drop(['bithYear','gender'],axis=1,inplace=True)
work_test = pd.merge(work_test,info_test, on="id_bh")
work_test.drop(work_test.columns[work_test.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
work_test.to_csv('work_test_2.csv')