import os
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm.notebook import tqdm
import math
import re
import warnings
from datetime import datetime

warnings.filterwarnings('ignore')

import category_encoders as ce
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import plot_roc_curve, auc, roc_curve, f1_score
from sklearn.feature_selection import SelectKBest, chi2, f_classif, f_regression

from catboost import CatBoostClassifier, CatBoostRegressor, Pool
import optuna

tqdm.pandas()


def seed_all(seed):
    np.random.seed(seed)
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)

seed = 55
seed_all(seed)


#import dataset
train_work = pd.read_csv('uet-hackathon-2022-data-science/work_train.csv')
test_work = pd.read_csv('uet-hackathon-2022-data-science/work_test.csv')
train_info = pd.read_csv('uet-hackathon-2022-data-science/info_train.csv')
test_info = pd.read_csv('uet-hackathon-2022-data-science/info_test.csv')
train_label = pd.read_csv('uet-hackathon-2022-data-science/label_train.csv')
test_label = pd.read_csv('uet-hackathon-2022-data-science/label_test.csv')

#rename columns
train_work.rename(columns = {'address': 'work_address'}, inplace = True)
test_work.rename(columns = {'address': 'work_address'}, inplace = True)

train_info.rename(columns = {'address': 'home_address'}, inplace = True)
test_info.rename(columns = {'address': 'home_address'}, inplace = True)

#plot missing value
def plot_missing_values(df):
    cols = df.columns
    count = [df[col].isnull().sum() for col in cols]
    percent = [i / len(df) for i in count]
    missing = pd.DataFrame({'proportion': percent}, index=cols)
    missing = missing.sort_values(by='proportion', ascending=False)
    plt.figure(figsize=(6, 6))
    plt.title(f'Missing values on each columns')
    ax = sns.barplot(missing['proportion'], missing.index)

    for i, p in enumerate(ax.patches):
        ax.text(p.get_x() + p.get_width() + 2e-2, p.get_y() + p.get_height(), f"{missing.iloc[i]['proportion']:.2f}",
                ha='center')

    mean = np.mean(missing['proportion'])
    std = np.std(missing['proportion'])
    plt.ylabel('Columns')
    plt.plot([], [], ' ', label=f'Average missing values: {mean:.2f} \u00B1 {std:.2f}')
    plt.legend()
    plt.show()

    return missing, missing.index.tolist()
# missing_train_work, train_work_cols = plot_missing_values(train_work)
# missing_test_work, test_work_cols = plot_missing_values(test_work)
# missing_train_info, train_info_cols = plot_missing_values(train_info)
# missing_test_info, test_info_cols = plot_missing_values(test_info)


# replace Nan
train_work["job/role"] = train_work["job/role"].replace(np.nan, "thiếu")
train_work["work_address"] = train_work["work_address"].replace(np.nan, "việt nam")
train_info["home_address"] = train_info["home_address"].replace(np.nan, "việt nam")

test_work["job/role"] = test_work["job/role"].replace(np.nan, "thiếu")
test_work["work_address"] = test_work["work_address"].replace(np.nan, "việt nam")
test_info["home_address"] = test_info["home_address"].replace(np.nan, "việt nam")

#repalce vnese accent
def no_accent_vietnamese(s):
    s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
    s = re.sub('[ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬ]', 'A', s)
    s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
    s = re.sub('[ÉÈẺẼẸÊẾỀỂỄỆ]', 'E', s)
    s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
    s = re.sub('[ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ]', 'O', s)
    s = re.sub('[íìỉĩị]', 'i', s)
    s = re.sub('[ÍÌỈĨỊ]', 'I', s)
    s = re.sub('[úùủũụưứừửữự]', 'u', s)
    s = re.sub('[ÚÙỦŨỤƯỨỪỬỮỰ]', 'U', s)
    s = re.sub('[ýỳỷỹỵ]', 'y', s)
    s = re.sub('[ÝỲỶỸỴ]', 'Y', s)
    s = re.sub('đ', 'd', s)
    s = re.sub('Đ', 'D', s)
    return s
train_info["home_address"] = train_info["home_address"].apply(no_accent_vietnamese)
train_work["work_address"] = train_work["work_address"].apply(no_accent_vietnamese)
train_work["job/role"] = train_work["job/role"].apply(no_accent_vietnamese)

test_info["home_address"] = test_info["home_address"].apply(no_accent_vietnamese)
test_work["work_address"] = test_work["work_address"].apply(no_accent_vietnamese)
test_work["job/role"] = test_work["job/role"].apply(no_accent_vietnamese)

#address
def str_normalize(s):
    if type(s) == str:
        s = str(s).strip().lower()
        s = re.sub(' +', " ", s)
    return s

def address_category(x):
    if type(x) == str:
        if "ha noi" in x or "hn" in x or "ha no" in x  or "ha n?i" in x or "thµnh phe hµ nei" in x \
        or "ha tay" in x or "tu liem" in x \
        or "cau giay" in x or "thanh xuan" in x or "dong da" in x or "dich vong" in x or "ha dong" in x or "nhan chinh" in x \
        or "dao tan" in x or "kim ma" in x or "thanh cong" in x or "phuc xa" in x or "keangnam" in x \
        or "nui truc" in x or "lang ha" in x or "nguyen van cu" in x or "thanh oai" in x \
        or "ba dinh" in x or "doi can" in x or "hoang hoa tham" in x or "yen phu" in x or "lotte center" in x \
        or "hoang minh giam" in x or "pho bach dang" in x or "viet hung" in x or "pho vong duc" in x \
        or "lac long quan" in x or "doc tam da" in x or "bo de" in x or "quan nhan" in x or "giang vo" in x \
        or "nguyen chi thanh" in x or "tho quan" in x or "de la thanh" in x or "khu mieu" in x \
        or "nam dong" in x or "kham thien" in x or "dang tien dong" in x \
        or "thai ha" in x or "dang van ngu" in x or "thai thinh" in x or "phuong mai" in x or "tay ho" in x \
        or "hai ba trung" in x or "van ho " in x or "doi cung" in x or "bach khoa" in x or "vinh tuy" in x \
        or "mai huong" in x or "hai ba t" in x or "tap the det 8/3" in x or "truong dinh" in x or "tan trieu" in x \
        or "yen hoa" in x or "quan tho " in x or "nguyen khang" in x or "pham tuan tai" in x \
        or "me tro thuong" in x or "nguyen ngoc nai" in x or "linh dam" in x or "trung hoa" in x \
        or "nguyen trai" in x or "nguyen xien" in x or "hoang van thai" in x or "chelsea park" in x or "phu kieu" in x \
        or "dai thanh" in x or "duong 32" in x or "khu tap the 664" in x or "huynh cung" in x or "yen thi" in x:
            return "ha noi"
        elif "dak lak" in x or "daklak" in x or"dakk lak" in x or "tp.bmt" in x:
            return "dak lak"
        elif "an giang" in x:
            return "an giang"
        elif "ba ria" in x or "vung tau" in x or "brvt" in x:
            return "ba ria   vung tau"
        elif "bac giang" in x or "bg" in x or "bac giang" in x or "yen the" in x or "bac gian" in x or "thon buom" in x:
            return "bac giang"
        elif "bac kan" in x or "bac can" in x:
            return "bac kan"
        elif "bac lieu" in x:
            return "bac lieu"
        elif "bac ninh" in x:
            return "bac ninh"
        elif "ben tre" in x:
            return "ben tre"
        elif "binh dinh" in x:
            return "binh dinh"
        elif "binh duong" in x:
            return "binh duong"
        elif "binh phuoc" in x:
            return "binh phuoc"
        elif "binh thuan" in x:
            return "binh thuan"
        elif "ca mau" in x:
            return "ca mau"
        elif "can tho" in x:
            return "can tho"
        elif "cao bang" in x:
            return "cao bang"
        elif "da nang" in x:
            return "da nang"
        elif "dak nong" in x or "daknong" in x:
            return "dak nong"
        elif "dien bien" in x:
            return "dien bien"
        elif "dong nai" in x:
            return "dong nai"
        elif "dong thap" in x:
            return "dong thap"
        elif "gia lai" in x:
            return "gia lai"
        elif "ha giang" in x:
            return "ha giang"
        elif "ha nam" in x:
            return "ha nam"
        elif "ha tinh" in x:
            return "ha tinh"
        elif "hai duong" in x or "an nhan tay" in x:
            return "hai duong"
        elif "hai phong" in x:
            return "hai phong"
        elif "hau giang" in x:
            return "hau giang"
        elif "hoa binh" in x or "hb" in x or "phuong huu nghi" in x:
            return "hoa binh"
        elif "hung yen" in x or "hung yon" in x:
            return "hung yen"
        elif "khanh hoa" in x:
            return "khanh hoa"
        elif "kien giang" in x:
            return "kien giang"
        elif "lam dong" in x or "ld" in x or "da lat" in x or "bao loc" in x or "duc trong" in x or "dalat" in x:
            return "lam dong"
        elif "thai nguyen" in x:
            return "thai nguyen"
        elif "nghe an" in x or "do luong" in x or "dien chau" in x or "quynh luu" in x or "q.luu" in x or "nghe an" in x:
            return "nghe an"
        elif "kon tum" in x:
            return "kon tum"
        elif "lai chau" in x:
            return "lai chau"
        elif "lam dong" in x:
            return "lam dong"
        elif "lang son" in x:
            return "lang son"
        elif "lao cai" in x:
            return "lao cai"
        elif "long an" in x:
            return "long an"
        elif "nam dinh" in x or "ý yen" in x:
            return "nam dinh"
        elif "ninh binh" in x:
            return "ninh binh"
        elif "ninh thuan" in x:
            return "ninh thuan"
        elif "phu tho" in x:
            return "phu tho"
        elif "phu yen" in x:
            return "phu yen"
        elif "quang binh" in x:
            return "quang binh"
        elif "quang nam" in x:
            return "quang nam"
        elif "quang ngai" in x:
            return "quang ngai"
        elif "quang ninh" in x or "ha long" in x:
            return "quang ninh"
        elif "quang tri" in x:
            return "quang tri"
        elif "thai nguyen" in x:
            return "thai nguyen"
        elif "ho chi minh" in x or "hcm" in x:
            return "tp ho chi minh"
        elif "soc trang" in x:
            return "soc trang"
        elif "son la" in x:
            return "son la"
        elif "tay ninh" in x:
            return "tay ninh"
        elif "thai binh" in x or "thon bich du" in x:
            return "thai binh"
        elif "thai nguyen" in x:
            return "thai nguyen"
        elif "thanh hoa" in x or "thanh hoa" in x:
            return "thanh hoa"
        elif "thua thien hue" in x or "hue" in x:
            return "thua thien hue"
        elif "tien giang" in x:
            return "tien giang"
        elif "tra vinh" in x:
            return "tra vinh"
        elif "tuyen quang" in x:
            return "tuyen quang"
        elif "vinh long" in x:
            return "vinh long"
        elif "vinh phuc" in x or "vp" in x or "vinh phu" in x:
            return "vinh phuc"
        elif "yen bai" in x:
            return "yen bai"
        else:
            return x
    else:
        return np.nan

def address_preprocess(x):
    x = str_normalize(x)
    x = address_category(x)
    return x
print("sample: ", len(train_info))
before_nan = train_info["home_address"].isna().sum()
print("before nan: ", before_nan)




train_info["home_address"] = train_info["home_address"].apply(address_preprocess)

after_nan = train_info["home_address"].isna().sum()
print("after nan: ", after_nan)
print("increase nan: ", after_nan - before_nan)
print("increase nan: ", (after_nan - before_nan) / len(train_info))

print("sample: ", len(test_info))
before_nan = test_info["home_address"].isna().sum()
print("before nan: ", before_nan)




test_info["home_address"] = test_info["home_address"].apply(address_preprocess)

after_nan = test_info["home_address"].isna().sum()
print("after nan: ", after_nan)
print("increase nan: ", after_nan - before_nan)
print("increase nan: ", (after_nan - before_nan) / len(test_info))


print("sample: ", len(train_work))
before_nan = train_work["work_address"].isna().sum()
print("before nan: ", before_nan)

train_work["work_address"] = train_work["work_address"].apply(address_preprocess)

after_nan = train_work["work_address"].isna().sum()
print("after nan: ", after_nan)
print("increase nan: ", after_nan - before_nan)
print("increase nan: ", (after_nan - before_nan) / len(train_work))



print("sample: ", len(test_work))
before_nan = test_work["work_address"].isna().sum()
print("before nan: ", before_nan)

test_work["work_address"] = test_work["work_address"].apply(address_preprocess)

after_nan = test_work["work_address"].isna().sum()
print("after nan: ", after_nan)
print("increase nan: ", after_nan - before_nan)
print("increase nan: ", (after_nan - before_nan) / len(test_work))

def job_category(x):
    if type(x) == str:
        if "cong nhan vien" in x or "nhan vien" in x or "giao dich vien" in x or "van thu" in x \
        or "thu ky" in x or "tro ly" in x or "nv" in x or "kiem soat vien" in x \
        or "van phong" in x or "xa vien" in x or "kiem thu vien" in x or "vien chuc" in x \
        or "kiem lam vien" in x or "chap hanh vien" in x or "hanh chinh" in x or "kiem tra chat luong" in x \
        or "thu vien" in x or "quan trac vien" in x or "phu trach quan he nguoi tieu dung" in x:
            return "nhan vien"
        elif "cong nhan" in x or "may cong nghiep" in x or "san pham" in x or "cn" in x or "khai thac" in x or "tho" in x \
        or "phet keo de va mu giay" in x or "ve sinh may chai ,day truyen soi ,det ,nhuom" in x or "c.n" in x \
        or "son, in da va pha che hoa chat de son, in da" in x or "sua chua" in x or "kt 3d" in x \
        or "cung nhon lap rop mach dien tu " in x or "luu hoa cac san pham cao su" in x or "qc" in x \
        or "thuy thu" in x or "cat vai trong cong nghe may" in x or "son, in da va pha che hoa chat de son, in da" in x \
        or "phay" in x or "phet keo mu giay" in x:
            return "cong nhan"
        elif "can bo" in x or "can su" in x:
            return "can bo/ can su"
        elif "chuyen vien" in x or "chuyen gia" in x:
            return "chuyen vien"
        elif "chu tich" in x:
            return "chu tich"
        elif "pho chu tich" in x:
            return "pho chu tich"
        elif "giam doc" in x or "tong giam doc" in x:
            return "giam doc"
        elif "pho giam doc" in x or "pho tong giam doc" in x or "pho gd" in x or "p. giam doc" in x or "p.giam doc" in x:
            return "pho giam doc"
        elif "hieu truong" in x:
            return "hieu truong"
        elif "pho hieu truong" in x or "hieu pho" in x:
            return "pho hieu truong"
        elif "to truong" in x or "truong phong" in x or "quan ly" in x or "chuyen truong " in x or "doi truong" in x \
        or "chu nhiem" in x or "quan ly" in x or "giam sat" in x or "nhom truong" in x or "truong ca" in x \
        or "truong nhom" in x or "quan doc" in x or "cua hang truong" in x or "thuyen truong" in x \
        or "kiem soat truong" in x or "doc cong" in x or "chu quan" in x or "tram truong" in x or "ca truong" in x:
            return "quan ly truong"
        elif "to pho " in x or "pho truong phong" in x or "pho phong" in x or "pho chanh" in x or "pho chu nhiem" in x \
        or "pho quan doc" in x or "doi pho" in x or "pho chi cuc truong" in x:
            return "quan ly pho"
        elif "bi thu" in x or "uy vien ban thuong vu" in x or "uy vien uy ban kiem tra" in x or "thuong truc dang uy" in x:
            return "bi thu"
        elif "pho bi thu" in x:
            return "pho bi thu"
        elif "chi huy truong quan su " in x or "truong cong an" in x:
            return "truong quan su"
        elif "bo doi" in x or "thanh tra vien" in x or "chien sy" in x:
            return "quan su"
        elif "ky su" in x or "ky thuat" in x or "kien truc su" in x or "lap trinh vien" in x or "ky thuat" in x:
            return "ky su"
        elif "giao vien" in x or "giang vien" in x:
            return "giao vien"
        elif "lai xe" in x or "tai xe " in x or "lai" in x or "lx" in x or "phu xe" in x:
            return "lai xe"
        elif "bao ve" in x:
            return "bao ve"
        elif "ke toan truong" in x:
            return "ke toan truong"
        elif "ke toan" in x or "kinh te vien" in x or "mau dich vien" in x or "kinh te" in x or "thong ke" in x:
            return "kinh te vien"
        elif "lao dong" in x or "ldpt" in x:
            return "lao dong"
        elif "y sy" in x or "bac sy" in x or "trinh duoc vien" in x or "duoc sy" in x:
            return "y sy"
        elif "dieu duong" in x or "ho ly" in x or "ho sinh" in x or "y ta" in x or "duoc ta" in x:
            return "dieu duong"
        elif "thu quy" in x or "thu kho" in x:
            return "thu nhan"
        elif "phong vien" in x or "bien tap vien" in x:
            return "truyen hinh"
        elif "nghien cuu vien" in x:
            return "nghien cuu vien"
        elif "ban hang" in x or "kinh doanh" in x:
            return "kinh doanh"
        elif "phien dich" in x or "phien dich tieng han" in x:
            return "phien dich"
        elif "dia chinh - xay dung " in x:
            return "dia chinh   xay dung"
        elif "van hoa - xa hoi" in x:
            return "van hoa   xa hoi"
        elif "tu phap - ho tich" in x or "luat su" in x or "kiem sat vien" in x or "tu phap ho tich" in x:
            return "tu phap   ho tich"
        elif "tham phan" in x:
            return "tham phan"
        elif "tap vu" in x:
            return "tap vu"
        elif "nghi thai san" in x:
            return "nghi thai san"
        elif "cap duong" in x:
            return "cap duong"
        elif "dien vien" in x:
            return "dien vien"
        elif "nau an" in x or "phu bep" in x:
            return "nau an"
        else:
            return x
    else:
        return np.nan

def job_preprocess(x):
    x = str_normalize(x)
    x = job_category(x)
    return x

print("sample: ", len(train_work))
before_nan = train_work["job/role"].isna().sum()
print("before nan: ", before_nan)

train_work["job/role"] = train_work["job/role"].apply(job_preprocess)

after_nan = train_work["job/role"].isna().sum()
print("after nan: ", after_nan)
print("increase nan: ", after_nan - before_nan)
print("increase nan: ", (after_nan - before_nan) / len(train_work))


print("sample: ", len(test_work))
before_nan = test_work["job/role"].isna().sum()
print("before nan: ", before_nan)




test_work["job/role"] = test_work["job/role"].apply(job_preprocess)

after_nan = test_work["job/role"].isna().sum()
print("after nan: ", after_nan)
print("increase nan: ", after_nan - before_nan)
print("increase nan: ", (after_nan - before_nan) / len(test_work))



train_work["id_management"] = train_work["id_management"].astype(str)
train_work["company_type"] = train_work["company_type"].replace(-1, 9)
train_work["company_type"] = train_work["company_type"].astype(str)
train_work["job/role"] = train_work["job/role"].replace(np.nan, "thieu")
train_work["work_address"] = train_work["work_address"].replace(np.nan, "viet nam")
train_work["id_office"] = train_work["id_office"].replace(np.nan, "ZZ000ZZ")
train_work["id_office_1"] = train_work["id_office"].map(lambda x: x[0:2])
train_work["id_office_2"] = train_work["id_office"].map(lambda x: x[2:])

train_info["home_address"] = train_info["home_address"].replace(np.nan, "viet nam")

test_work["id_management"] = test_work["id_management"].astype(str)
test_work["company_type"] = test_work["company_type"].replace(-1, 9)
test_work["company_type"] = test_work["company_type"].astype(str)
test_work["job/role"] = test_work["job/role"].replace(np.nan, "thieu")
test_work["work_address"] = test_work["work_address"].replace(np.nan, "viet nam")
test_work["id_office"] = test_work["id_office"].replace(np.nan, "ZZ000ZZ")
test_work["id_office_1"] = test_work["id_office"].apply(lambda x: x[0:2])
test_work["id_office_2"] = test_work["id_office"].apply(lambda x: x[2:])

test_info["home_address"] = test_info["home_address"].replace(np.nan, "viet nam")




train_work["employee_lv"] = train_work["employee_lv"].replace(-1.0, np.nan)
test_work["employee_lv"] = test_work["employee_lv"].replace(-1.0, np.nan)

train_work.loc[train_work["employee_lv"] > 100.0, "employee_lv"] = np.nan
test_work.loc[test_work["employee_lv"] > 100.0, "employee_lv"] = np.nan


train_info["age"] = 2022 - train_info["bithYear"]
test_info["age"] = 2022 - test_info["bithYear"]

train_info["age_class"] = (train_info["age"] // 10).astype(str)
test_info["age_class"] = (test_info["age"] // 10).astype(str)

def date_normalize(s):
    s = str(s)[0:6]
    s = pd.to_datetime(s, format="%Y%m")
    return s

train_work["from_date"] = train_work["from_date"].apply(date_normalize)
train_work["to_date"] = train_work["to_date"].apply(date_normalize)

test_work["from_date"] = test_work["from_date"].apply(date_normalize)
test_work["to_date"] = test_work["to_date"].apply(date_normalize)


train_work["total_years_distance"] = (train_work["to_date"] - train_work["from_date"]).astype('timedelta64[Y]').astype('int')
train_work["total_months_distance"] = (train_work["to_date"] - train_work["from_date"]).astype('timedelta64[M]').astype('int')
train_work["total_days_distance"] = (train_work["to_date"] - train_work["from_date"]).dt.days
train_work["total_years_now"] = (date_normalize(20220400) - train_work["from_date"]).astype('timedelta64[Y]').astype('int')
train_work["total_months_now"] = (date_normalize(20220400) - train_work["from_date"]).astype('timedelta64[M]').astype('int')
train_work["total_days_now"] = (date_normalize(20220400) - train_work["from_date"]).dt.days
train_work["expire_years"] = ((date_normalize(20220400) - train_work["to_date"]).astype('timedelta64[Y]').astype('int')).apply(lambda x: x if x >= 0 else 0)
train_work["expire_months"] = ((date_normalize(20220400) - train_work["to_date"]).astype('timedelta64[M]').astype('int')).apply(lambda x: x if x >= 0 else 0)
train_work["expire_days"] = ((date_normalize(20220400) - train_work["to_date"]).dt.days).apply(lambda x: x if x >= 0 else 0)

test_work["total_years_distance"] = (test_work["to_date"] - test_work["from_date"]).astype('timedelta64[Y]').astype('int')
test_work["total_months_distance"] = (test_work["to_date"] - test_work["from_date"]).astype('timedelta64[M]').astype('int')
test_work["total_days_distance"] = (test_work["to_date"] - test_work["from_date"]).dt.days
test_work["total_years_now"] = (date_normalize(20220400) - test_work["from_date"]).astype('timedelta64[Y]').astype('int')
test_work["total_months_now"] = (date_normalize(20220400) - test_work["from_date"]).astype('timedelta64[M]').astype('int')
test_work["total_days_now"] = (date_normalize(20220400) - test_work["from_date"]).dt.days
test_work["expire_years"] = ((date_normalize(20220400) - test_work["to_date"]).astype('timedelta64[Y]').astype('int')).apply(lambda x: x if x >= 0 else 0)
test_work["expire_months"] = ((date_normalize(20220400) - test_work["to_date"]).astype('timedelta64[M]').astype('int')).apply(lambda x: x if x >= 0 else 0)
test_work["expire_days"] = ((date_normalize(20220400) - test_work["to_date"]).dt.days).apply(lambda x: x if x >= 0 else 0)



train_df = train_info.merge(train_label, on="id_bh")
test_df = test_info.merge(test_label, on="id_bh")

train_df["count_job"] = train_work.groupby(["id_bh"]).size().reindex(train_df["id_bh"].values).values

# for m in ["mean", "median", "std", "min", "max", "sum"]:
for m in ["mean", "std", "min", "max"]:
    train_df["total_years_distance_{}".format(m)] = train_work.groupby(["id_bh"])["total_years_distance"].agg(
        m).reindex(train_df["id_bh"].values).values
    train_df["total_months_distance_{}".format(m)] = train_work.groupby(["id_bh"])["total_months_distance"].agg(
        m).reindex(train_df["id_bh"].values).values
    train_df["total_days_distance_{}".format(m)] = train_work.groupby(["id_bh"])["total_days_distance"].agg(m).reindex(
        train_df["id_bh"].values).values

for m in ["mean", "median", "std", "min", "max"]:
    train_df["employee_lv_{}".format(m)] = train_work.groupby(["id_bh"])["employee_lv"].agg(m).reindex(
        train_df["id_bh"].values).values

for m in ["max"]:
    train_df["total_years_now_{}".format(m)] = train_work.groupby(["id_bh"])["total_years_distance"].agg(m).reindex(
        train_df["id_bh"].values).values
    train_df["total_months_now_{}".format(m)] = train_work.groupby(["id_bh"])["total_months_distance"].agg(m).reindex(
        train_df["id_bh"].values).values
    train_df["total_days_now_{}".format(m)] = train_work.groupby(["id_bh"])["total_days_distance"].agg(m).reindex(
        train_df["id_bh"].values).values

# first work
train_df["total_years_distance_first_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='first')[
    "total_years_distance"].values
train_df["total_months_distance_first_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='first')[
    "total_months_distance"].values
train_df["total_days_distance_first_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='first')[
    "total_days_distance"].values
train_df["total_years_now_first_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='first')[
    "total_years_now"].values
train_df["total_months_now_first_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='first')[
    "total_months_now"].values
train_df["total_days_now_first_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='first')[
    "total_days_now"].values
train_df["expire_years_first_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='first')["expire_years"].values
train_df["expire_months_first_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='first')[
    "expire_months"].values
train_df["expire_days_first_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='first')["expire_days"].values
train_df["employee_lv_first_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='first')["employee_lv"].values

# last work
train_df["total_years_distance_last_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='last')[
    "total_years_distance"].values
train_df["total_months_distance_last_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='last')[
    "total_months_distance"].values
train_df["total_days_distance_last_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='last')[
    "total_days_distance"].values
train_df["total_years_now_last_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='last')[
    "total_years_now"].values
train_df["total_months_now_last_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='last')[
    "total_months_now"].values
train_df["total_days_now_last_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='last')[
    "total_days_now"].values
train_df["expire_years_last_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='last')["expire_years"].values
train_df["expire_months_last_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='last')["expire_months"].values
train_df["expire_days_last_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='last')["expire_days"].values
train_df["employee_lv_last_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='last')["employee_lv"].values

# delta last work - first work
train_df["total_years_distance_last_first_work"] = train_df["total_years_distance_last_work"] - train_df[
    "total_years_distance_first_work"]
train_df["total_months_distance_last_first_work"] = train_df["total_months_distance_last_work"] - train_df[
    "total_months_distance_first_work"]
train_df["total_days_distance_last_first_work"] = train_df["total_days_distance_last_work"] - train_df[
    "total_days_distance_first_work"]
train_df["total_years_now_last_first_work"] = train_df["total_years_now_last_work"] - train_df[
    "total_years_now_first_work"]
train_df["total_months_now_last_first_work"] = train_df["total_months_now_last_work"] - train_df[
    "total_months_now_first_work"]
train_df["total_days_now_last_first_work"] = train_df["total_days_now_last_work"] - train_df[
    "total_days_now_first_work"]
train_df["expire_years_last_first_work"] = train_df["expire_years_last_work"] - train_df["expire_years_first_work"]
train_df["expire_months_last_first_work"] = train_df["expire_months_last_work"] - train_df["expire_months_first_work"]
train_df["expire_days_last_first_work"] = train_df["expire_days_last_work"] - train_df["expire_days_first_work"]
train_df["employee_lv_last_first_work"] = train_df["employee_lv_last_work"] - train_df["employee_lv_first_work"]

## test_df
test_df["count_job"] = test_work.groupby(["id_bh"]).size().reindex(test_df["id_bh"].values).values

# for m in ["mean", "median", "std", "min", "max", "sum"]:
for m in ["mean", "std", "min", "max"]:
    test_df["total_years_distance_{}".format(m)] = test_work.groupby(["id_bh"])["total_years_distance"].agg(m).reindex(
        test_df["id_bh"].values).values
    test_df["total_months_distance_{}".format(m)] = test_work.groupby(["id_bh"])["total_months_distance"].agg(
        m).reindex(test_df["id_bh"].values).values
    test_df["total_days_distance_{}".format(m)] = test_work.groupby(["id_bh"])["total_days_distance"].agg(m).reindex(
        test_df["id_bh"].values).values

for m in ["mean", "median", "std", "min", "max"]:
    test_df["employee_lv_{}".format(m)] = test_work.groupby(["id_bh"])["employee_lv"].agg(m).reindex(
        test_df["id_bh"].values).values

for m in ["max"]:
    test_df["total_years_now_{}".format(m)] = test_work.groupby(["id_bh"])["total_years_distance"].agg(m).reindex(
        test_df["id_bh"].values).values
    test_df["total_months_now_{}".format(m)] = test_work.groupby(["id_bh"])["total_months_distance"].agg(m).reindex(
        test_df["id_bh"].values).values
    test_df["total_days_now_{}".format(m)] = test_work.groupby(["id_bh"])["total_days_distance"].agg(m).reindex(
        test_df["id_bh"].values).values

# first work
test_df["total_years_distance_first_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='first')[
    "total_years_distance"].values
test_df["total_months_distance_first_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='first')[
    "total_months_distance"].values
test_df["total_days_distance_first_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='first')[
    "total_days_distance"].values
test_df["total_years_now_first_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='first')[
    "total_years_now"].values
test_df["total_months_now_first_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='first')[
    "total_months_now"].values
test_df["total_days_now_first_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='first')[
    "total_days_now"].values
test_df["expire_years_first_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='first')["expire_years"].values
test_df["expire_months_first_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='first')["expire_months"].values
test_df["expire_days_first_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='first')["expire_days"].values
test_df["employee_lv_first_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='first')["employee_lv"].values

# last work
test_df["total_years_distance_last_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='last')[
    "total_years_distance"].values
test_df["total_months_distance_last_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='last')[
    "total_months_distance"].values
test_df["total_days_distance_last_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='last')[
    "total_days_distance"].values
test_df["total_years_now_last_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='last')[
    "total_years_now"].values
test_df["total_months_now_last_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='last')[
    "total_months_now"].values
test_df["total_days_now_last_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='last')["total_days_now"].values
test_df["expire_years_last_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='last')["expire_years"].values
test_df["expire_months_last_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='last')["expire_months"].values
test_df["expire_days_last_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='last')["expire_days"].values
test_df["employee_lv_last_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='last')["employee_lv"].values

# delta last work - first work
test_df["total_years_distance_last_first_work"] = test_df["total_years_distance_last_work"] - test_df[
    "total_years_distance_first_work"]
test_df["total_months_distance_last_first_work"] = test_df["total_months_distance_last_work"] - test_df[
    "total_months_distance_first_work"]
test_df["total_days_distance_last_first_work"] = test_df["total_days_distance_last_work"] - test_df[
    "total_days_distance_first_work"]
test_df["total_years_now_last_first_work"] = test_df["total_years_now_last_work"] - test_df[
    "total_years_now_first_work"]
test_df["total_months_now_last_first_work"] = test_df["total_months_now_last_work"] - test_df[
    "total_months_now_first_work"]
test_df["total_days_now_last_first_work"] = test_df["total_days_now_last_work"] - test_df["total_days_now_first_work"]
test_df["expire_years_last_first_work"] = test_df["expire_years_last_work"] - test_df["expire_years_first_work"]
test_df["expire_months_last_first_work"] = test_df["expire_months_last_work"] - test_df["expire_months_first_work"]
test_df["expire_days_last_first_work"] = test_df["expire_days_last_work"] - test_df["expire_days_first_work"]
test_df["employee_lv_last_first_work"] = test_df["employee_lv_last_work"] - test_df["employee_lv_first_work"]
for m in ["nunique"]:
    train_df["id_management_{}".format(m)] = train_work.groupby(["id_bh"])["id_management"].agg(m).reindex(
        train_df["id_bh"].values).values
    train_df["id_office_{}".format(m)] = train_work.groupby(["id_bh"])["id_office"].agg(m).reindex(
        train_df["id_bh"].values).values
    train_df["id_office_1_{}".format(m)] = train_work.groupby(["id_bh"])["id_office_1"].agg(m).reindex(
        train_df["id_bh"].values).values
    train_df["id_office_2_{}".format(m)] = train_work.groupby(["id_bh"])["id_office_2"].agg(m).reindex(
        train_df["id_bh"].values).values
    train_df["company_type_{}".format(m)] = train_work.groupby(["id_bh"])["company_type"].agg(m).reindex(
        train_df["id_bh"].values).values
    train_df["job/role_{}".format(m)] = train_work.groupby(["id_bh"])["job/role"].agg(m).reindex(
        train_df["id_bh"].values).values
    train_df["work_address_{}".format(m)] = train_work.groupby(["id_bh"])["work_address"].agg(m).reindex(
        train_df["id_bh"].values).values

# # first work
# train_df["id_management_first_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='first')["id_management"].values
# train_df["id_office_first_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='first')["id_office"].values
# train_df["id_office_1_first_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='first')["id_office_1"].values
# train_df["id_office_2_first_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='first')["id_office_2"].values
# train_df["company_type_first_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='first')["company_type"].values
# train_df["job/role_first_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='first')["job/role"].values
# train_df["work_address_first_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='first')["work_address"].values

# last work
train_df["id_management_last_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='last')["id_management"].values
train_df["id_office_last_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='last')["id_office"].values
train_df["id_office_1_last_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='last')["id_office_1"].values
train_df["id_office_2_last_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='last')["id_office_2"].values
train_df["company_type_last_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='last')["company_type"].values
train_df["job/role_last_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='last')["job/role"].values
train_df["work_address_last_work"] = train_work.drop_duplicates(subset=['id_bh'], keep='last')["work_address"].values

for m in ["nunique"]:
    test_df["id_management_{}".format(m)] = test_work.groupby(["id_bh"])["id_management"].agg(m).reindex(
        test_df["id_bh"].values).values
    test_df["id_office_{}".format(m)] = test_work.groupby(["id_bh"])["id_office"].agg(m).reindex(
        test_df["id_bh"].values).values
    test_df["id_office_1_{}".format(m)] = test_work.groupby(["id_bh"])["id_office_1"].agg(m).reindex(
        test_df["id_bh"].values).values
    test_df["id_office_2_{}".format(m)] = test_work.groupby(["id_bh"])["id_office_2"].agg(m).reindex(
        test_df["id_bh"].values).values
    test_df["company_type_{}".format(m)] = test_work.groupby(["id_bh"])["company_type"].agg(m).reindex(
        test_df["id_bh"].values).values
    test_df["job/role_{}".format(m)] = test_work.groupby(["id_bh"])["job/role"].agg(m).reindex(
        test_df["id_bh"].values).values
    test_df["work_address_{}".format(m)] = test_work.groupby(["id_bh"])["work_address"].agg(m).reindex(
        test_df["id_bh"].values).values

# first work
# test_df["id_management_first_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='first')["id_management"].values
# test_df["id_office_first_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='first')["id_office"].values
# test_df["id_office_1_first_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='first')["id_office_1"].values
# test_df["id_office_2_first_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='first')["id_office_2"].values
# test_df["company_type_first_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='first')["company_type"].values
# test_df["job/role_first_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='first')["job/role"].values
# test_df["work_address_first_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='first')["work_address"].values

# last work
test_df["id_management_last_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='last')["id_management"].values
test_df["id_office_last_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='last')["id_office"].values
test_df["id_office_1_last_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='last')["id_office_1"].values
test_df["id_office_2_last_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='last')["id_office_2"].values
test_df["company_type_last_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='last')["company_type"].values
test_df["job/role_last_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='last')["job/role"].values
test_df["work_address_last_work"] = test_work.drop_duplicates(subset=['id_bh'], keep='last')["work_address"].values


# categorical feature
features_full = train_df.columns.tolist()
features_categorical = ["gender",
                        "age_class",
                        "home_address",
                        "id_management_last_work",
                        "id_office_last_work",
                        "id_office_1_last_work",
                        "id_office_2_last_work",
                        "company_type_last_work",
                        "job/role_last_work",
                        "work_address_last_work",
#                         "id_management_first_work",
#                         "id_office_first_work",
#                         "id_office_1_first_work",
#                         "id_office_2_first_work",
#                         "company_type_first_work",
#                         "job/role_first_work",
#                         "work_address_first_work"
                        ]

# remove feature
target = "label"
for c in ["label",
          "bithYear",
          "id_bh"]:
    features_full.remove(c)

train_data = train_df[features_full]
train_label = train_df[target]
test_data = test_df[features_full]

category_idx = np.array([])
for i in features_categorical:
  category_idx= np.append(category_idx, train_data.columns.get_loc(i))
category_idx = category_idx.astype(np.int)

train_data_temp = train_data
train_data_temp = train_data_temp.fillna('None')
cbe_encoder = ce.cat_boost.CatBoostEncoder()
cbe_encoder.fit(train_data_temp, train_label)
train_cbe = cbe_encoder.transform(train_data_temp)
bestfeatures = SelectKBest(score_func=f_classif, k='all')
fit = bestfeatures.fit(train_cbe,train_label)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(train_cbe.columns)

featureScores = pd.concat([dfcolumns,dfscores],axis=1)
featureScores.columns = ['Feature','Score']
print(featureScores.nlargest(100,'Score'))



X_train, X_valid, y_train, y_valid = train_test_split(train_data, train_label, test_size=0.1, random_state=42)

params = {
        'max_depth': 8,
        'learning_rate': 0.09,
        'n_estimators': 3750,
        'max_bin': 271,
        'min_data_in_leaf': 417,
        'l2_leaf_reg': 0.0002403681946051935,
        'subsample': 0.8658782253625072,
        'early_stopping_rounds' : 200,
        'random_state': 42,
    #     'leaf_estimation_method': 'Gradient',
        'bootstrap_type': 'Bernoulli',
        'objective': 'MultiClass',
        'verbose': 0,
        "eval_metric" : 'TotalF1',
        "task_type" : "GPU",
        "devices" : '0:1'
    }

clf = CatBoostClassifier(**params)

clf.fit(
    X_train, y_train,
    cat_features=category_idx,
    eval_set=(X_valid, y_valid),
    verbose=False,
    plot=True
)
y_pred = clf.predict(X_valid)
f1_scr = f1_score(y_valid, y_pred, average="weighted")
print("f1 score: {:.5f}".format(f1_scr))
