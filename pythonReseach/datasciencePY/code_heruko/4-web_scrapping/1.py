import requests
from bs4 import BeautifulSoup

page = requests.get("http://standards-oui.ieee.org/oui/oui.txt")

print(page)

contents = page.content

print(contents)

soup = BeautifulSoup(contents, 'txt.parser')
# some parser: lxml.parser, html.parser,  xpath.parser

#print(soup)
#print(soup.prettify())
#print(soup.head) #access on the <head> tag
#print(soup.body) #access only the <body> tag
#print(soup.div) #access only the <div> tag

data = []
blog = {}

# section = soup.find('section', 'card-group-2')
section = soup.find('section', attrs={"class":"card-group-2'"})
all_cards = section.find_all('div', attrs={'class':'card'})
print(all_cards.prettify)


for card in all_cards:
    title  = card.find('h2', class_='card-title')
    print(title)

# End Result
# [
#     {'Title':"AI, ML, DL Are they different ?", 'date_pub':'March 25, 2019'},
#      {'Title':"AI, ML, DL Are they different ?", 'date_pub':'March 25, 2019'}
# ]





