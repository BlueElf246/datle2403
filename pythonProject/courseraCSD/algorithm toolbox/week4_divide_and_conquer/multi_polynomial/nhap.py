# import requests
# import bs4
# def polymonial_multiplication(A,B,n):
#     product=[]
#     for x in range(2*n-1):
#         product.append(0)
#     for ia,a in enumerate(A):
#         for ib,b in enumerate(B):
#             multiply=a*b
#             product[ia+ib]+=multiply
#     print(product)
#     return product
#
# url='https://vnexpress.net/'
# data=requests.get(url).text
# soup=bs4.BeautifulSoup(data,'html.parser')
# print(soup.prettify())
# a=soup.find_all('a')
# for x in a:
#     m=x.find_all(href=True)
#     print(m)

for x in range(10,0,-1):
    print(x)