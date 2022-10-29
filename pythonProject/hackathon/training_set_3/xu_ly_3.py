import pandas as pd
df=pd.read_csv('work_test_2.csv')
df1=pd.read_csv('work_train_2.csv')
# df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)





# df.drop(['address'],axis=1,inplace=True)
# df.to_csv('work_test_2.csv')
# df1.drop(['id_office','id_management','gender','bithYear','employee_lv','company_type','job/role','from_date','to_date'],axis=1,inplace=True)
# df1.drop(df1.columns[df1.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
# df1.to_csv('work_test_2_add.csv')


# df = pd.merge(df,df1, on="id_bh")
# df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
# df.to_csv('work_test_2.csv')

print(df['job/role'].value_counts())
print(df1['job/role'].value_counts())