import pandas as pd
import requests
from bs4 import BeautifulSoup
def run1():
    url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
    data=requests.get(url).text
    soup=BeautifulSoup(data,'html5lib')
    netflix_data=pd.DataFrame(columns=['Data','Open','High','Low','Close','Volume'])
    for row in soup.find('tbody').find_all('tr'):
        col = row.find_all("td")
        date = col[0].text
        Open = col[1].text
        high = col[2].text
        low = col[3].text
        close = col[4].text
        adj_close = col[5].text
        volume = col[6].text

        # Finally we append the data of each row to the table
        netflix_data = netflix_data.append(
            {"Date": date, "Open": Open, "High": high, "Low": low, "Close": close, "Adj Close": adj_close,
             "Volume": volume}, ignore_index=True)
    read_html_pd=pd.read_html(url)
    print(read_html_pd[0])
def run2():
    url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html'
    html_data=requests.get(url).text
    soup=BeautifulSoup(html_data,'html5lib')
    print(soup.find('title'))
    amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])
    for row in soup.find("tbody").find_all("tr"):
        col = row.find_all("td")
        date = col[0].text
        Open = col[1].text
        high = col[2].text
        low = col[3].text
        close = col[4].text
        adj_close = col[5].text
        volume = col[6].text
        amazon_data = amazon_data.append(
            {"Date": date, "Open": Open, "High": high, "Low": low, "Close": close, "Adj Close": adj_close,
             "Volume": volume}, ignore_index=True)
    print(amazon_data.tail())
run2()