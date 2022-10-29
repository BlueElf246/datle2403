import pandas as pd
import matplotlib.pyplot as plt
train_work=pd.read_csv("uet-hackathon-2022-data-science/work_train.csv")
test_work=pd.read_csv("uet-hackathon-2022-data-science/work_test.csv")
train_info=pd.read_csv("uet-hackathon-2022-data-science/info_train.csv")
test_info=pd.read_csv("uet-hackathon-2022-data-science/info_test.csv")
y_train=pd.read_csv("uet-hackathon-2022-data-science/label_train.csv")


df=train_work
df = df.drop(columns=['id','from_date','to_date'])
print(df['company_type'].value_counts())
print(df['job/role'].value_counts())
print(df['employee_lv'].value_counts())
print(df['address'].value_counts())
df.to_csv('file_name.csv')
