import requests
from bs4 import BeautifulSoup
import pandas as pd
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup=BeautifulSoup(html,'html.parser')
# tag_object=soup.h3
# tag_child=tag_object.b
# print(soup.prettify())
# print(tag_child.attrs)
table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table=BeautifulSoup(table,'html.parser')
# pretify=table.prettify()
# find=table.find_all('tr')
# find1=table.find_all(name=['tr','td'])
# find2=table.find_all(id='flight')
# find3=table.find_all(href=True)
# print(find3)
# f=find[0]

two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"
two_table=BeautifulSoup(two_tables,'html.parser')
# k=(two_table.find('table'))
# j=two_table.find('table',class_='pizza') # find the second table

#Downloading And Scraping The Contents Of A Web Page
def run():
    url="http://www.ibm.com"
    data=requests.get(url).text
    ibm=BeautifulSoup(data,'html.parser')
    link_list=ibm.find_all('a')
    for x in link_list:
        print(x)
#Scrape data from HTML tables
def run1():
    url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
    data=requests.get(url).text
    table=BeautifulSoup(data,'html.parser')
    for row in table.find_all('tr'):
        cols=row.find_all('td')
        name=cols[2].string
        color_code=cols[3].string
        print(name,'->>>>',color_code)
def run2():
    url="https://en.wikipedia.org/wiki/World_population"
    data=requests.get(url).text
    table=BeautifulSoup(data,'html.parser')
    tables=table.find_all('table')
    for index,table in enumerate(tables):
        if(("10 most densely populated countries") in str(table)):
            table_index=index
    tab=tables[5]
    population=pd.DataFrame(columns=['rank','country','population','area','density'])
    for row in tab.find_all('tr'):
        col=row.find_all('td')
        if (col !=[]):
            rank=col[0].text
            country=col[1].text
            pop=col[2].text.strip()
            area=col[3].text.strip()
            desity=col[4].text.strip()
            population=population.append({'rank':rank,'country':country,'population':pop,'area':area,'density':desity},ignore_index=True)
    ta=pd.read_html(str(tab),flavor='bs4')
    #print table directly from url
    dataframe_list=pd.read_html(url,flavor='bs4')
    dataframe_list[1].to_csv('data.csv')
    r=pd.read_html(url,match='10 most densely populated countries',flavor='bs4')
run2()