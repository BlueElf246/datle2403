import pandas as pd

'''
MỤC TIÊU CỦA FILE NÀY LÀ ĐỂ TẠO HAI FILE WORK TRAIN VÀ WORK TEST ĐÃ XỬ LÝ:
1/ THÊM CÁC GIÁ TRỊ BỊ THIẾU(NULL)
2/CHỈNH FONT CỦA CỘT JOB/ROLE
3/CHỌN 1 ID_BH CỦA FILE WORK/TEST RỒI MERGE VỚI FILE INFO
'''



# tạo work_test:
def transform_date(x):
  temp = int(x/100)
  return (temp//100)+round((temp%100)/12,2)
def work_test():
    df=pd.read_csv('work_test.csv')
    df1=pd.read_csv('info_test.csv')
    df1.drop(['address'],axis=1,inplace=True)
    df1.to_csv('info_test.csv')
    id_office_replace='7311'
    employee_lv_replace='8.0'
    df['employee_lv'].fillna(value=employee_lv_replace,inplace=True)
    df['id_office'].fillna(value=id_office_replace,inplace=True)
    df.drop(['id'],axis=1,inplace=True)
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    df.drop_duplicates(subset=["id_bh"], keep="first",inplace=True)
    df = pd.merge(df,df1, on="id_bh")
    df["to_date"] = df["to_date"].apply(transform_date)
    df["from_date"] = df["from_date"].apply(transform_date)
    df["period"] = df["to_date"] - df["from_date"]
    df['job/role'].fillna('Công nhân',inplace=True)
    df['job/role']=df['job/role'].str.strip()
    df['job/role']=df['job/role'].str.lower()
    df.to_csv('work_test_2.csv')

#tạo work train
def work_train():
    df=pd.read_csv('work_train.csv')
    df1=pd.read_csv('info_train.csv')
    df1.drop(['address'],axis=1,inplace=True)
    df1.to_csv('info_train.csv')
    id_office_replace='YN0042Z'
    employee_lv_replace='8.0'
    df['employee_lv'].fillna(value=employee_lv_replace,inplace=True)
    df['id_office'].fillna(value=id_office_replace,inplace=True)
    df.drop(['id'],axis=1,inplace=True)
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    df.drop_duplicates(subset=["id_bh"], keep="first",inplace=True)
    df = pd.merge(df,df1, on="id_bh")
    df["to_date"] = df["to_date"].apply(transform_date)
    df["from_date"] = df["from_date"].apply(transform_date)
    df["period"] = df["to_date"] - df["from_date"]
    df['job/role'].fillna('Công nhân',inplace=True)
    df['job/role']=df['job/role'].str.strip()
    df['job/role']=df['job/role'].str.lower()
    df.to_csv('work_train_2.csv')

work_test()
work_train()