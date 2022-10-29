import pandas as pd
import matplotlib.pyplot as plt
ten='sosanh.csv'
ten1='work_train_2.csv'
df =pd.read_csv(ten)
df1= pd.read_csv(ten1)
'''
SAU KHI XỬ LÝ PHẦN ADDRESS: CHÚNG TA SẼ CÓ 2 FILE WORK VÀ 
'''
def xoa(df,df1):
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    df.drop(['address'],axis=1,inplace=True)
    df.to_csv(ten)
    df1.drop(['id_office','id_management','gender','bithYear','employee_lv','company_type','job/role','from_date','to_date'],axis=1,inplace=True)
    df1.drop(df1.columns[df1.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    df1.to_csv(ten1)

def merge(df,df1):
    df = pd.merge(df,df1, on="id_bh")
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    df.drop(['address_x'],axis=1,inplace=True)
    df.rename(columns = {'address_y':'address'}, inplace = True)
    print(df.info())
    df.to_csv(ten)