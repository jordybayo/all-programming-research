import requests
from bs4 import BeautifulSoup
import pandas as pd

link = "https://www.cnbcafrica.com/special-report/2020/02/21/the-forbes-billionaires-list-africas-billionaires-2020/"


#request get all raw input data
linked_text = requests.get(link).text
#print(linked_text)

#soup = BeautifulSoup(linked_text, 'lxml')
soup = BeautifulSoup(linked_text, 'html.parser')
#print(soup.prettify())

#title
print(soup.title())
#to get only the string part typr
print(soup.title.string)


#explore only <a> objects
#print(soup.a)
#explore all a tags
#print(soup.findAll('a'))


#fetch all the tables tags
all_tables = soup.find_all('table')
#print(all_tables)


#find all strogs tags because they contain billionaires name
all_strong = soup.findAll('strong')
#print(all_strong)



billionnaire = []
for bill in all_strong:
    billionnaire.append(bill)
print(billionnaire)


#save all in xls file with pandas
# df = pd.DataFrame(billionnaire)
# print(df)
    