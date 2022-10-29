import pandas as pd

# df=pd.read_csv('work_test.csv')
# df1=pd.read_csv('info_test.csv')
# df1.drop(['address'],axis=1,inplace=True)
# df1.to_csv('info_test.csv')
# id_office_replace='7311'
# employee_lv_replace='8.0'
# df['employee_lv'].fillna(value=employee_lv_replace,inplace=True)
# df['id_office'].fillna(value=id_office_replace,inplace=True)
# df.drop(['id'],axis=1,inplace=True)
# df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
# df.drop_duplicates(subset=["id_bh"], keep="first",inplace=True)
# df = pd.merge(df,df1, on="id_bh")
# df.fillna('Công nhân',inplace=True)
# df['job/role']=df['job/role'].str.strip()
# df['job/role']=df['job/role'].str.lower()
# df.to_csv('work_test_1.csv')


# df=pd.read_csv('work_train.csv')
# df1=pd.read_csv('info_train.csv')
# df1.drop(['address'],axis=1,inplace=True)
# df1.to_csv('info_train.csv')
# id_office_replace='YN0042Z'
# employee_lv_replace='8.0'
# df['employee_lv'].fillna(value=employee_lv_replace,inplace=True)
# df['id_office'].fillna(value=id_office_replace,inplace=True)
# df.drop(['id'],axis=1,inplace=True)
# df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
# df.drop_duplicates(subset=["id_bh"], keep="first",inplace=True)
# df = pd.merge(df,df1, on="id_bh")
# df.fillna('Công nhân',inplace=True)
# df['job/role']=df['job/role'].str.strip()
# df['job/role']=df['job/role'].str.lower()
# df.to_csv('work_train_1.csv')



# df2=pd.read_csv('work_train_1.csv')
# def replace_1(job,lst,name,df):
#     s=set()
#     for x in job:
#         x=x.strip()
#         for m in lst:
#             if x.startswith(m):
#                 s.add(x)
#     print(s)
#     decide=input('có cho chép ko?')
#     if decide =='y':
#         df['job/role']= df['job/role'].replace(s,name)
#         df.to_csv('alo.csv')
#         print(f'All done for {name}')
# def check(x):
#     lst=['bác sĩ','kỹ sư','giáo viên','nhân viên','giám đốc','trợ lý','chuyên viên','trưởng phòng','công nhân','cán bộ','thư ký','kiểm tra viên','thợ sửa','tài xế','giảng viên','điều dưỡng','lập trình viên','nhà nước/quân đội','bảo vệ','kế toán','học sinh/cử nhân/thạc sĩ','lao động']
#     for m in lst:
#         if m==x:
#             return False
#     return True
# def check_1(job):
#     other=set()
#     lst=[]
#     for x in job:
#         if check(x):
#             other.add(x)
#             lst.append(x)
#     return other
# #df2.to_csv('work_test_backup.csv')
# job=df2['job/role'].tolist()
# #lst=['bác sĩ','kỹ sư','giáo viên','nhân viên','giám đốc','trợ lý','chuyên viên','trưởng phòng','công nhân','cán bộ','thư ký','kiểm tra viên','thợ sửa','tài xế','giảng viên','điều dưỡng','lập trình viên','phóng viên','nhà nước/quân đội','bảo vệ','kế toán','học sinh/cử nhân']
# replace_1(job,['cán','cb'],'cán bộ',df2)
# replace_1(job,['kiểm'],'kiểm tra viên',df2)
# replace_1(job,['tài','lái','lx','tx'],'tài xế',df2)
# replace_1(job,['thợ'],'thợ sửa',df2)
# replace_1(job,['phụ giảng','giảng'],'giảng viên',df2)
# replace_1(job,['điều dưỡng'],'điều dưỡng',df2)
# replace_1(job,['lập trình viên','lập','fefwef'],'lập trình viên',df2)
# replace_1(job,['kỹ','kiến'],'kỹ sư',df2)
# replace_1(job,['trợ'],'trợ lý',df2)
# replace_1(job,['thư ký'],'thư ký',df2)
# replace_1(job,['chuyên','cv'],'chuyên viên',df2)
# replace_1(job,['trưởng'],'trưởng phòng',df2)
# replace_1(job,['giáo','gv'],'giáo viên',df2)
# replace_1(job,['nhân','nv','cnv'],'nhân viên',df2)
# replace_1(job,['giám','gđ'],'giám đốc',df2)
# replace_1(job,['công','cn'],'công nhân',df2)
# replace_1(job,['thiếu','văn phòng đảng','thượng','tiểu','học viên','ủy viên','hạ','bộ','binh','đội','chỉ','cán','uỷ','trung sỹ','bí','đảng','nhà'],'nhà nước/quân đội',df2)
# replace_1(job,['bảo','bv'],'bảo vệ',df2)
# replace_1(job,['kế'],'kế toán',df2)
# replace_1(job,['cử','học','thạc','tiến'],'học sinh/cử nhân/thạc sĩ',df2)
# replace_1(job,['dược','bác','bs'],'bác sĩ',df2)
# replace_1(job,['lao','lđ'],'lao động',df2)
# replace_1(job,['chủ','giám'],'giám đốc',df2)
# df2.drop(df2.columns[df2.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
# #df2.to_csv('work_test_backup.csv')
# other=check_1(job)
# df2['job/role'].replace(other,'other',inplace=True)
# # print(other,len(other))
# # print(df2['job/role'].value_counts())
# df2.to_csv('work_train_1.csv')




ds=['']
doc="""An Giang
Vũng Tàu
Bạc Liêu
Bắc Kạn
Bắc Giang
Bắc Ninh
Bến Tre
Bình Dương
Bình Định
Bình Phước
Bình Thuận
Cà Mau
Cao Bằng
Cần Thơ
Đà Nẵng
Đắk Lắk
Đắk Nông
Điện Biên
Đồng Nai
Đồng Tháp
Gia Lai
Hà Giang
Hà Nam
Hà Nội
Hà Tây
Hà Tĩnh
Hải Dương
Hải Phòng
Hòa Bình
Hồ Chí Minh
Hậu Giang
Hưng Yên
Khánh Hòa
Kiên Giang
Kon Tum
Lai Châu
Lào Cai
Lạng Sơn
Lâm Đồng
Long An
Nam Định
Nghệ An
Ninh Bình
Ninh Thuận
Phú Thọ
Phú Yên
Quảng Bình
Quảng Nam
Quảng Ngãi
Quảng Ninh
Quảng Trị
Sóc Trăng
Sơn La
Tây Ninh
Thái Bình
Thái Nguyên
Thanh Hóa
Huế
Tiền Giang
Trà Vinh
Tuyên Quang
Vĩnh Long
Vĩnh Phúc
Yên Bái"""
lst=doc.split('\n')
new=[]
for x in range(0,len(lst)):
    lst[x]=lst[x].lower()
print(lst)
