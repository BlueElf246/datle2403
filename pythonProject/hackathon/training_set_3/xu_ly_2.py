import pandas as pd
import re
ten='work_train_2.csv'
df=pd.read_csv(ten)
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
df.to_csv(ten)
def check(x,lst):
    #lst=['bác sĩ','kỹ sư','giáo viên','nhân viên','giám đốc','trợ lý','chuyên viên','trưởng phòng','công nhân','cán bộ','thư ký','kiểm tra viên','thợ sửa','tài xế','giảng viên','điều dưỡng','lập trình viên','nhà nước/quân đội','bảo vệ','kế toán','học sinh/cử nhân/thạc sĩ','lao động']
    for m in lst:
        if m==x:
            return False
    return True
def check_1(job,lst):
    other=set()
    lst1=[]
    for x in job:
        if check(x,lst):
            other.add(x)
            lst1.append(x)
    print(len(lst1))
    return other
def replace_3(job,name_find,name,df,ten):
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
        df['job/role']= df['job/role'].replace(s,name)
        df.to_csv(ten)
        print(f'All done for {name}')
job=df['job/role'].to_list() # chua xu ly: giam doc, nhan vien, tro ly, chuyen vien , truong phong, can bo, thu ky, kiem tra vien,tho
#lst=['bác sĩ','kỹ thuật viên','giáo viên','nhân viên','giám đốc','trợ lý','chuyên viên','trưởng phòng','công nhân','cán bộ','thư ký','kiểm tra viên','thợ','tài xế','giảng viên','điều dưỡng','lập trình viên','nhà nước/quân đội','bảo vệ','kế toán','học sinh/cử nhân/thạc sĩ','lao động']
lst2=['bác sĩ','kỹ thuật viên','giám đốc','giáo viên','công nhân','tài xế','thợ sửa','điều dưỡng','bảo vệ','giảng viên','học sinh/cử nhân/thạc sĩ','kinh doanh','bán hàng','quân đội','kế toán','kỹ sư','vận hành máy','lễ tân/cskh','cntt','phục vụ','phiên dịch viên','ô tô','diễn viên','trưởng phòng','nhân viên','cán bộ']
# replace_3(job,['thú y','bác','y sỹ','bs','dược','y tế','y sĩ','răng hàm'],'bác sĩ',df,ten)
# replace_3(job,['giáo viên','gv'],'giáo viên',df,ten)
# replace_3(job,['giám đốc','gđ','phó giám đốc','pgđ','chủ tịch','hđqt','lãnh đạo'],'giám đốc',df,ten)
# replace_3(job,['công nhân','cn','cnv'],'công nhân',df,ten)
# replace_3(job,['tài xế','lái xe','lái','lx','tx','vận chuyển','vận tải'],'tài xế',df,ten)
# replace_3(job,['thợ'],'thợ sửa',df,ten)
# replace_3(job,['điều dưỡng'],'điều dưỡng',df,ten)
#replace_3(job,['kỹ thuật'],'kỹ thuật viên',df,ten)
#replace_3(job,['bảo vệ','bv'],'bảo vệ',df,ten)
#replace_3(job,['giảng viên','trợ giảng'],'giảng viên',df,ten)
#replace_3(job,['học sinh','cử nhân','thạc sĩ'],'học sinh/cử nhân/thạc sĩ',df,ten)
#replace_3(job,['kinh'],'kinh doanh',df,ten)
#replace_3(job,['bán'],'bán hàng',df,ten)
#replace_3(job,['công an','binh','sĩ','uý','quân','quân khu','chiến','tiểu đội','hạ sỹ','hạ sĩ','bộ đội','bộ đội','tiểu đoàn','tiểu khu','sỹ'],'quân đội',df,ten)
#replace_3(job,['kế','tài chính'],'kế toán',df,ten)
#replace_3(job,['kỹ sư','cơ khí'],'kỹ sư',df,ten)
#replace_3(job,['vận','điều'],'vận hành máy',df,ten)
#replace_3(job,['lễ','khách','chăm sóc','cskh','tư vấn','dịch vụ'],'lễ tân/cskh',df,ten)
#replace_3(job,['công nghệ','lập trình','cntt'],'cntt',df,ten)
#replace_3(job,['xây','đường','công trình','kiến trúc sư','địa'],'xây dựng/đất đai',df,ten)
#replace_3(job,['phiên','dịch thuật'],'phiên dịch viên',df,ten)
#replace_3(job,['phục','tạp'],'phục vụ',df,ten)
#replace_3(job,['ô tô','xe'],'ô tô',df,ten)
#replace_3(job, ['diễn'], 'diễn viên', df, ten)
#replace_3(job, ['cán'], 'cán bộ', df, ten)
#replace_3(job, ['nhân','viên','nv'], 'nhân viên', df, ten)
#replace_3(job, ['trưởng','phòng'], 'trưởng phòng', df, ten)
#replace_3(job, ['lao'], 'lao động', df, ten)






other=check_1(job,lst2)
df['job/role'].replace(other,'other',inplace=True)
df.to_csv('work_train_2.csv')
print(other)
print(len(other))

