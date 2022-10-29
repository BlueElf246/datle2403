import pandas as pd
import numpy as np
import json
import urllib.request
import xml.etree.ElementTree as ET
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

def run1():
    url ='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv'
    df=pd.read_csv(url,header=None)
    df.columns=['First name','Last name','Location','City','State','Area code']
    #print the column
    column1=df['First name']
    #use loc to select row
    row1=df.loc[0]
    #or to select row at column...
    row=df.loc[[0,1],'City']
    #use iloc to index row, column
    p=df.iloc[[0,1,2,3],1]
    print(p)
def run2():
    df=pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]),columns=['a','b','c'])
    #add 10 to each element in dataframe
    df=df.transform(func=lambda x:x+10)
    #find square foot
    df=df.transform(func=['sqrt'])
    print(df)
def run3():
    #writing json to a file
    person = {
        'first_name': 'Mark',
        'last_name': 'abc',
        'age': 27,
        'address': {
            "streetAddress": "21 2nd Street",
            "city": "New York",
            "state": "NY",
            "postalCode": "10021-3100"
        }
    }
    #json.dump convert dict to json object
    # file only shown in 1 row
    with open('person.json','w') as f:
        json.dump(person,f)
    # serialization
    json_object=json.dumps(person,indent=4)
    with open('sample.json','w') as outfile:
        outfile.write(json_object)
def run4():
    # reading json to a file( Deserialization)
    with open('sample.json','r') as openfile:
        # reading from json file
        json_object=json.load(openfile)
    print(json_object)
def run5():
    #XLSX is a Microsoft Excel Open XML file format. It is another type of Spreadsheet file format.
    urllib.request.urlretrieve(
        "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx",
        "sample.xlsx")
    df = pd.read_excel("sample.xlsx")
    print(df)
def run6():
    """
    The xml.etree.ElementTree module comes built-in with Python.
    It provides functionality for parsing and creating XML documents.
    ElementTree represents the XML document as a tree.
    We can move across the document using nodes which are elements and sub-elements of the XML file.
    """
    # create the file structure
    employee = ET.Element('employee')
    details = ET.SubElement(employee, 'details')
    first = ET.SubElement(details, 'firstname')
    second = ET.SubElement(details, 'lastname')
    third = ET.SubElement(details, 'age')
    first.text = 'Shiv'
    second.text = 'Mishra'
    third.text = '23'

    # create a new XML file with the results
    mydata1 = ET.ElementTree(employee)
    # myfile = open("items2.xml", "wb")
    # myfile.write(mydata)
    with open("new_sample.xml", "wb") as files:
        mydata1.write(files)
    df=pd.read_xml('new_sample.xml')
    df.to_csv('new_sample.csv', index=False)
def run7():
    #binary file format
    #Binary files can range from image files like JPEGs or GIFs, audio files like MP3s or binary document formats like Word or PDF.
    #reading the iamge file
    urllib.request.urlretrieve(
        "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg",
        "dog.jpg")
    img=Image.open('dog.jpg')
run7()
def run8():
    # read the csv file about diabetes
    path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
    df=pd.read_csv(path)
    #check to n row of dataframe
    first5=df.head(5)
    last5=df.tail(5)
    #dimension of df
    dim=df.shape
    #statistical overview of dataset
    info=df.info()
    #view some basic statical details
    des=df.describe()
    #Identify and handle missing values
    missing_data=df.isnull()
    for column in missing_data.columns.values.tolist():
        print(column)
        print(missing_data[column].value_counts())
        print('')
    #view the type of each column
    type=df.dtypes
    labels='Diabetic','Not Diabetic'
    plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
    plt.legend()
    plt.show()

run8()

