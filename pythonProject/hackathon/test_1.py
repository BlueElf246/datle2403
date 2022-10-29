import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

# df = pd.read_csv('file_name.csv')
# print(df['job/role'].value_counts())
# df.dropna(inplace=True)
# print(df.shape)
# df.to_csv('file_name.csv')
# df['job/role'] = df['job/role'].str.lower()
# df.to_csv('file_name.csv')



# job=df['job/role'].tolist()
cong_nhan=set()
giam_doc=set()
tro_ly=set()
chuyen_vien=set()
giam_sat_vien=set()
cv=set()
nhan_vien=set()
giao_vien=set()
pho=set()
ky_su=set()
truong=set()
bac_si=set()
# for x in job:
#     m=x
#     x=x.strip()
#     x=x.split(' ')
#     if len(x)==1:
#         continue
    # if x[0]=='chuyên':
    #     chuyen_vien.add(m)
    # elif x[0]=='trợ':
    #     tro_ly.add(m)
    # elif x[0]=='công' or x[0]=='cn':
    #     cong_nhan.add(m)
    # # elif x[0]=='giám' and x[1]=='sát':
    # #     giam_sat_vien.add(m)
    # elif x[0]=='giám':
    #     giam_doc.add(m)
    # if x[0]=='n.' or x[0]== 'nhân' or x[0]=='nv':
    #     nhan_vien.add(m)
    # if x[0]=='phó':
    #     pho.add(m)
    # if x[0] == 'kỹ':
    #     ky_su.add(m)
    # if x[0]=='trưởng':
    #     truong.add(m)
    # if x[0]=='bác' or x[0]=='y':
    #     bac_si.add(m)


# print(bac_si)
# print(chuyen_vien, tro_ly,cong_nhan,giam_doc)
# lb=['Unnamed: 0']
# df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
# df['job/role']= df['job/role'].replace(cv,'chuyên viên')
# df['job/role']= df['job/role'].replace(truong,'trưởng phòng')
# df['job/role']= df['job/role'].replace(chuyen_vien,'chuyên viên')
# df['job/role']= df['job/role'].replace(tro_ly,'trợ lý')
# df['job/role']= df['job/role'].replace(giam_doc,'giám đốc')
# df['job/role']= df['job/role'].replace(giam_sat_vien,'giám sát viên')
# df['job/role']= df['job/role'].replace(nhan_vien,'nhân viên')
# df['job/role']= df['job/role'].replace(giao_vien,'giáo viên')
# df['job/role']= df['job/role'].replace(pho,'phó')
# df['job/role']= df['job/role'].replace(ky_su,'kỹ sư')
# df['job/role']= df['job/role'].replace(bac_si,'bác sĩ')
# df.to_csv('file_name.csv')

# job_1=[x for x in job if x!='công nhân' or x!='giám đốc' or x!='chuyên viên' or x!='trợ lý' or x!='nhân viên' or x!='giáo viên']
# print(job_1)

# id_bh=df['id_bh'].tolist()
# id_bh_set=set()
# for x in id_bh:
#     id_bh_set.add(x)
# print(id_bh_set,len(id_bh_set))
# df.drop(['id_management','id_office'],axis=1,inplace=True)
# df.to_csv('file_name.csv')

# print(df.loc[df['job/role']=='bác sĩ'])
# df2 = df.loc[df["job/role"] == ('bác sĩ' or 'kỹ sư' or 'phó' or 'giáo viên' or 'nhân viên' or 'giám sát viên' or 'giám đốc' or 'trợ lý' or 'chuyên viên' or 'trưởng phòng' or 'công nhân')]
# df2 = df[(df['job/role'] == 'bác sĩ') | (df['job/role'] == 'kỹ sư') | (df['job/role'] == 'phó') | (df['job/role'] == 'giáo viên') | (df['job/role'] == 'nhân viên')| (df['job/role'] == 'giám sát viên')| (df['job/role'] == 'giám đốc')| (df['job/role'] == 'trợ lý')| (df['job/role'] == 'chuyên viên')| (df['job/role'] == 'trưởng phòng')| (df['job/role'] == 'công nhân')]
# df2.to_csv('work_train_1.csv')
df2 = pd.read_csv('alo.csv')
df2.drop(df2.columns[df2.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
df2.to_csv('alo.csv')
job=df2['job/role'].to_list()
def check(x):
    lst=['bác sĩ','kỹ sư','giáo viên','nhân viên','giám đốc','trợ lý','chuyên viên','trưởng phòng','công nhân','cán bộ','thư ký','kiểm tra viên','thợ sửa','tài xế','giảng viên','điều dưỡng','lập trình viên','phóng viên','nhà nước/quân đội','bảo vệ','kế toán','học sinh/cử nhân']
    for m in lst:
        if m==x:
            return False
    return True
def check_1(job):
    other=set()
    lst=[]
    for x in job:
        if check(x):
            other.add(x)
            lst.append(x)
    return other
def replace(job,replace_name,replace_name2,replace_name3,name,df):
    s=set()
    for x in job:
        m=x
        x=x.strip()
        x=x.split(' ')
        if len(x)==1:
            continue
        if x[0]==replace_name or x[0]== replace_name2 or x[0]==replace_name3:
            s.add(m)
    print(s)
    decide=input('có cho chép ko?')
    if decide =='y':
        df['job/role']= df['job/role'].replace(s,name)
        df.to_csv('alo.csv')
        print(f'All done for {name}')
def replace_1(job,lst,name,df):
    s=set()
    for x in job:
        x=x.strip()
        for m in lst:
            if x.startswith(m):
                s.add(x)
    print(s)
    decide=input('có cho chép ko?')
    if decide =='y':
        df['job/role']= df['job/role'].replace(s,name)
        df.to_csv('alo.csv')
        print(f'All done for {name}')
# print(len(check_1(job)))
# replace(job,'cán','cán bộ',df2)
# replace(job,'kiểm','kiểm tra viên',df2)
# replace(job,'tài','lái','tài xế',df2)
# replace(job,'thợ','','thợ sửa',df2)
#replace(job,'lao','','lao động',df2)
#replace(job,'','giảng','','giảng viên',df2)
#replace_1(job,'','điều dưỡng','','điều dưỡng',df2)
#replace_1(job,'lập trình viên','lập','fefwef','lập trình viên',df2)

#replace_1(job,['thiếu','văn phòng đảng','thượng','tiểu','học viên','ủy viên','hạ','bộ','binh','đội','chỉ','cán','uỷ','trung sỹ','bí','đảng'],'nhà nước/quân đội',df2)
#replace_1(job,['bảo','bv'],'bảo vệ',df2)
#replace_1(job,['kế'],'kế toán',df2)
# replace_1(job,['phụ giảng'],'giảng viên',df2)
# replace_1(job,['cử','học'],'học sinh/cử nhân',df2)
# replace_1(job,['dược'],'bác sĩ',df2)
# replace_1(job,['lao','lđ'],'lao động',df2)
# other= check_1(job)
# df2['job/role'].replace(other,'other',inplace=True)
print(df2['job/role'].value_counts())