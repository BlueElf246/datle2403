import pandas as pd
import plotly.express as px
import datetime
import  requests
import  json
gasoline = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML0232EN-SkillsNetwork/asset/18100001.csv")
def pri(x):
    print(x)
    print(x.value_counts())
    print(x.dtypes)
    print(x.info())
    print(x.shape)
    print(x.columns)
    print(x.isnull().sum())
data = (gasoline[['REF_DATE','GEO','Type of fuel','VALUE']]).rename(columns={"REF_DATE" : "DATE", "Type of fuel" : "TYPE"})
data[['City','Province']]=data['GEO'].str.split(',', n=1, expand=True)
data['DATE']=pd.to_datetime(data['DATE'], format='%b-%y')
data['Month']=data['DATE'].dt.month_name().str.slice(stop=3)
data['Year']=data['DATE'].dt.year

# print(data.VALUE.describe())
# print(data['GEO'].unique())
# print(data['TYPE'].unique())

calgary= data[data['GEO'] == 'Calgary, Alberta']
year=data[data['Year']== 2000]
Cities=data[data['City'].isin(['Toronto','Calgary'])]
multi= data[(data['City']=='Vancouver') & (data['Year']==1990) & (data['TYPE']=='Household heating fuel')]
multi1=data[data['Year'].isin([1979, 2021])]
geo = data.groupby('GEO')

year_city=data.groupby(['Year', 'City'])['VALUE'].median()

price_bycity = data.groupby(['Year', 'GEO'])['VALUE'].mean().reset_index(name ='Value').round(2)
fig = px.line(price_bycity
                   ,x='Year', y = "Value",
                   color = "GEO", color_discrete_sequence=px.colors.qualitative.Light24)
fig.update_traces(mode='markers+lines')
fig.update_layout(
    title="Gasoline Price Trend per City",
    xaxis_title="Year",
    yaxis_title="Annual Average Price, Cents per Litre")
fig.show()