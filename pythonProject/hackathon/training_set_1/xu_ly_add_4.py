import pandas as pd
df1=pd.read_csv('work_test_1.csv_exam.csv')
df2=pd.read_csv('chathca.csv')
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
# print(df1['address'].value_counts())
# print(df2['address'].value_counts())

# l1=df1['address'].to_list()
# l2=df2['address'].to_list()
# def counting(l1):
#     la = dict()
#     for x in l1:
#         la[x]=la.get(x,0)+1
#     return la
# m=counting(l1)
# n=counting(l2)
# value = set(m) - set(n)
# print(value)
# lst1=['quảng ninh', 'phú yên', 'tiền giang', 'cà mau']
# df1['address'].replace(lst1,'việt nam',inplace=True)
# df1.to_csv('work_test_1.csv_exam.csv')
# lst=['ninh thuận', 'an giang', 'đồng tháp', 'vĩnh long', 'bắc kạn', 'sóc trăng', 'trà vinh', 'kon tum', 'ninh bình']
# df1['address'].replace(lst,'việt nam',inplace=True)
# df1.to_csv('work_train_1.csv')
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

# l2=df2['address'].to_list()
# l1=df1['address'].to_list()
# def counting(l1):
#     la = dict()
#     for x in l1:
#         la[x]=la.get(x,0)+1
#     return la
# m=counting(l1)
# n=counting(l2)
# value = set(m) - set(n)
# print(value)

print(df1['address'].value_counts())