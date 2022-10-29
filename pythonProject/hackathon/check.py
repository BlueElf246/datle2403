import pandas as pd
import numpy
df1=pd.read_csv('training_set/work_test_1.csv')
df=pd.read_csv('training_set/work_train_1.csv')
print(df['job/role'].value_counts())
print(df1['job/role'].value_counts())