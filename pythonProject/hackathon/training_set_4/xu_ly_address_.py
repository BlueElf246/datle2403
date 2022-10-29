import pandas as pd
import re
import numpy as np
'''
ĐÂY LÀ BƯỚC XỬ LÝ PHẦN ADDRESS: LOẠI BỎ CÁC YẾU TỐ DƯ THỪA BÊN Ở ADDRESS VÀ QUY NÓ THÀNH MỘT ĐỊA ĐIỂM NHẤT ĐỊNH
VÌ MỘT SỐ LÝ DO MÀ CHÚNG TÔI PHẢI KẾT HỢP LỌC THỦ CÔNG VÀ LỌC QUA FUNCTION.
'''
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
df=pd.read_csv(ten)
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
df.to_csv(ten)
add=df['address'].to_list()
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
for x in lst:
    print(x)
    lst=[x]
    while True:
        name=input('nhap ten goi y\n')
        lst.append(name)
        d=input('tiep ko?')
        if d=='y':
            continue
        else:
            break
    replace_3(add,lst,x,df)

def check_2(x,lst):
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
replace_3(add,['đắk lăk'],'đắk lắk',df)
replace_3(add,['phú tho'],'phú thọ',df)
replace_3(add,['bình thạnh','củ chi','nhà bè','linh trung','thủ đức','tđ','gò vấp','tân phú','hcm','hóc','bình chánh','hócmôn','bình tân'],'hồ chí minh',df)
replace_3(add,['tây hồ','nghi xuân','kim liên','hà nộ','từ liêm','đống đa','nôi','gia lâm','pà','thanh xuân','hà nội','hà  nội','thành phố hà nội','hn','hà đông','cầu','ba đình','nghĩa tân','hoàn kiếm','thanh trì','đông anh'],'hà nội',df)
replace_3(add,['lăk','đắklắk'],'đắk lắk',df)
replace_3(add,['phúc'],'vĩnh phúc',df)
replace_3(add,['đà l','lạt'],'lâm đồng',df)
replace_3(add,['thanh hoá'],'thanh hóa',df)
replace_3(add,['vn','việt nam'],'việt nam',df)
replace_3(add,['thành phố vinh'],'nghệ an',df)
replace_3(add,['bd','binh dương','binh duong','bình  dương'],'bình dương',df)
replace_3(add,['hoà bình'],'hòa bình',df)
replace_3(add,['trảng bom','biên hoà'],'đồng nai',df)
replace_3(add,['đăk'],'đắk nông',df)
replace_3(add,['đn'],'đà nẵng',df)
replace_3(add,['brvt','vt'],'vũng tàu',df)
replace_3(add,['hạ long'],'quảng ninh',df)
replace_3(add,['bảo lộc'],'lâm đồng',df)
other=check_1(add,lst)
df['address'].replace(other,'việt nam',inplace=True)
df.to_csv(ten)