from bs4 import BeautifulSoup
import requests

page = requests.get("http://www.codeheroku.com/blog")
content = page.content.decode('ascii', 'ignore')
soup = BeautifulSoup(content, 'html.parser')
section = soup.find('section', attrs={'class':'card-group-2'})


cards = section.find_all('div', attrs={'class':'card'})


for card in cards:
    title = card.find('h2', class_= 'card-title')
    date = card.select('.card-date')
    print(date)

    print(title.text.strip(),date[0].text.strip())
