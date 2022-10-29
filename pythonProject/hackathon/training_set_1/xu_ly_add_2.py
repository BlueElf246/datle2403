import pandas as pd
import re
import numpy as np
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
for x in range(0,len(lst)):
    lst[x]=lst[x].lower()
ten='work_train_1.csv'
df=pd.read_csv(ten+'_exam.csv')
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
df.to_csv(ten)
add=df['address'].to_list()
# for x in range(0,len(add)):
#     m=add[x]
#     lst=m.split(' ')
#     if lst[0]=='tỉnh':
#         lst=lst[1:]
#         lst=' '.join(lst)
#         add[x]=lst
# df.to_csv(ten+'_exam.csv')

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
        df.to_csv(ten+'_exam.csv')
        print(f'All done for {name}')
def check(exclude_list,x):
    for e in exclude_list:
        c=re.search(e,x)
        if c is not None:
            return False
    if c is None:
        return True

def replace_2(job,lst,exclude_lst,name,df):
    s=set()
    for x in job:
        x=x.strip()
        for m in lst:
            if x.startswith(m):
                if check(exclude_lst,x):
                    s.add(x)

    print(s)
    decide=input('có cho chép ko?')
    if decide =='y':
        df['address']= df['address'].replace(s,name)
        df.to_csv(ten+'_exam.csv')
        print(f'All done for {name}')
def replace_3(job,name_find,name,df):
    s=set()
    for x in job:
        x=x.strip()
        for m in name_find:
            c=re.search(m,x)
            if c is None:
                continue
            else:
                s.add(x)
    print(s)
    decide=input('có cho chép ko?')
    if decide =='y':
        df['address']= df['address'].replace(s,name)
        df.to_csv(ten+'_exam.csv')
        print(f'All done for {name}')


# replace_1(add,['q','q.','quận','tp hồ','hcm','hồ'],'hồ chí minh',df)
# for x in lst:
#     print(x)
#     lst_1=[]
#     while True:
#         name=input('nhap ten goi y\n')
#         lst_1.append(name)
#         d=input('tiep ko?')
#         if d=='y':
#             continue
#         else:
#             break
#     replace_3(add,lst_1,x,df)

#replace_3(add,['quận','q'],'hồ chí minh',df)

def check_2(x,lst):
    #lst=['bác sĩ','kỹ sư','giáo viên','nhân viên','giám đốc','trợ lý','chuyên viên','trưởng phòng','công nhân','cán bộ','thư ký','kiểm tra viên','thợ sửa','tài xế','giảng viên','điều dưỡng','lập trình viên','phóng viên','nhà nước/quân đội','bảo vệ','kế toán','học sinh/cử nhân']
    for m in lst:
        if m==x:
            return False
    return True
def check_1(job,lst1):
    other=set()
    lst=[]
    for x in job:
        if check_2(x,lst1):
            other.add(x)
            lst.append(x)
    return other
other=check_1(add,lst)
print(other)
print(len(other))
# replace_3(add,['đắk lăk'],'đắk lắk',df)
# replace_3(add,['phú tho'],'phú thọ',df)
#replace_3(add,['linh trung','thủ đức','tđ','gò vấp','tân phú'],'hồ chí minh',df)
#replace_3(add,['tây hồ','nghi xuân','kim liên','hà nộ','từ liêm','đống đa','nôi','gia lâm','pà','thanh xuân','hà nội','hà  nội','thành phố hà nội'],'hà nội',df)
#replace_3(add,['lăk'],'đắk lắk',df)
#replace_3(add,['phúc'],'vĩnh phúc',df)
#replace_3(add,['đà l','lạt'],'lâm đồng',df)
#replace_3(add,['thanh hoá'],'thanh hóa',df)
#replace_3(add,['vn','việt nam'],'việt nam',df)
df['address'].replace(other,'việt nam',inplace=True)
df.to_csv('work_train_1.csv')
print(df['address'].value_counts())
