import pandas as pd
import numpy as np
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import fuzzywuzzy



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

ten='work_train_1.csv'
df=pd.read_csv(ten)
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
df.to_csv(ten)
# function to replace rows in the provided column of the provided dataframe
# that match the provided string above the provided ratio with the provided string
def replace_matches_in_column(df, column, string_to_match, min_ratio=47,limit=9):
    # get a list of unique strings
    strings = df[column].unique()

    # get the top 10 closest matches to our input string
    matches = fuzzywuzzy.process.extract(string_to_match, strings,
                                         limit=limit, scorer=fuzzywuzzy.fuzz.token_sort_ratio)
    print(matches)
    # only get matches with a ratio > 90
    close_matches = [matches[0] for matches in matches if matches[1] >= min_ratio]

    # get the rows of all the close matches in our dataframe
    rows_with_matches = df[column].isin(close_matches)

    # replace all rows with close matches with the input matches
    df.loc[rows_with_matches, column] = string_to_match
    # let us know the function's done
    # d=input('co muon chep ko')
    # if d=='y':
    #     df.to_csv(ten+'_exam.csv')
    print("All done!")

# df2=pd.read_csv(ten+'_exam.csv')
# for x in lst:
#     while True:
#         limit=int(input('chon limit'))
#         replace_matches_in_column(df=df2, column='address', string_to_match=x,limit=limit)
#         m=input('ban muon chinh limit ko?')
#         if m=='1':
#             continue
#         n = input('ban muon bo qua ko?')
#         if n=='2':
#             break
#print(add)
# df2.to_csv(ten + '_exam.csv')





#df2.to_csv(ten+'_exam.csv')
# add=df['address'].unique()
# print(add)
# matches = fuzzywuzzy.process.extract("hà nội",add, limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)
# print(matches)



# use the function we just wrote to replace close matches to "south korea" with "south korea"

# print(df2['address'].value_counts())
# print(df['address'].value_counts())
# get the top 10 closest matches to "south korea"