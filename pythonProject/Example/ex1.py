# import numpy as np
# import  math
# # in_arr=[3,4,5,6]
# # # num=[5,3]
# # # x=np.searchsorted(in_arr,num)
# # # print(x)
# # #create hist
# # np.random.seed(42)
# # bins=np.linspace(-100,100,1000)
# # h=np.random.multivariate_normal([0,0],[[1,2],[2,5]],100)
# # x=np.random.randn(10000)
# # plt.hist(x, bins,histtype='step')
# # plt.show()
#
# # m=dict()
# # m['q']=1
# # m['e']=2
# # m['g']=3
# # y=(1,2,3)
# # print(y[0])
# #cau b
# # while True:
# #     try:
# #         user =int(input('nhap 1 so bat ky'))
# #         break
# #     except:
# #         print ('hay nhap lai')
# #         continue
# # string='456789' # v.du
# # string=list(string)
# # length= len(string)
# # print(length)
# # for x in range(len(string)):
# #     if int(string[x])== user:
# #         m=string.pop(x)
# # if length== len(string):
# #     print('khong co so nao bi xoa!')
# #
# # print(string)
# # user=input('hay nhap so')
# # string=[1,2,3,4,5,6]
# # try:
# #     string.remove(int(user))
# # except:
# #     print('so nay ko co trong list hoac khong phai integer, hay nhap lai')
# # print(string)
# # string=list()
# # for x in range(4):
# #     string.append('_')
# # string[2]='s'
# # interface=''.join(string)
# # print(interface)
# # lst={'dat':1, 'ghu':2}
# # for x in lst:
# #     print()
# def base_conversion(tr_base,integer):
#     quotient=integer
#     lst=[]
#     while quotient!=0:
#         a=quotient % tr_base
#         quotient= quotient // tr_base
#         lst.append(a)
#     lst=lst[::-1]
#     return lst
# def add_binary(b1,b2):
#     c=0
#     lst=[]
#     for j in reversed(range(len(b1))):
#         d=math.floor((b1[j]+b2[j]+c)/2)
#         s=b1[j]+ b2[j] + c - 2*d
#         c=d
#         lst.append(s)
#     return lst
# def div_cal(number,div_num):
#     q=0
#     r=number
#     while r >=div_num:
#         r=r-div_num
#         q+=1
#     return q
# print(base_conversion(8,12345))
# b1=[1,1,1,0]
# b2=[1,0,1,1]
# print(add_binary(b1,b2))
# print(div_cal(30,2))
# import sys
# c=[[0,1,2],1,2,3,4,5]
# d=c[0:3]
# d[0][0]=10
# print(c,d)
# e=[3,4,5,6,7]
# f=[1,2]
# print(sys.getsizeof(f))
l=[1,2,3]
a,b,c=l
print(a,b,c)