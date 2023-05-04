from bs4 import BeautifulSoup
import requests
import pandas as pd
from converter import converter

data = []

for offset in range(0,100,100):
    print("offset is", offset)

    page = requests.get("https://finance.yahoo.com/screener/unsaved/ece7ca30-7bba-43f0-8d41-7a03005b1a09?count=100&offset="+str(offset))
    content = page.content.decode('ascii', 'ignore')

    soup = BeautifulSoup(content, 'html.parser')
    #print(soup.find_all('table'))

    table = soup.find('table', attrs={'class':'W(100%)'})
    # print(str(table).encode('ascii', 'ignore'))
    table_body = table.find('tbody')
    
    rows = table_body.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        val = {} 
        val['symbol'] = cols[0].text
        val['name'] = cols[1].text
        val['price'] = float(cols[2].text.replace(',',''))
        val['volume'] = converter(cols[5].text)
        
        data.append(val)


print(data)
print(len(data))
