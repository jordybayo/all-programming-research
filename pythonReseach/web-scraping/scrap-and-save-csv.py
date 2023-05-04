from bs4 import BeautifulSoup
import requests
import csv


soup = BeautifulSoup(requests.get("http://localhost:3000/").get, 'lxml')

csv_file = open("data_csv,csv", "w", newline="")
writer = csv.writer(csv_file)

writer.writerow("title", "summary", "links")

for articles in soup.findAll('div', attrs={"class":'post'}):
    title = articles.h3.a.text
    summary = articles.p.text
    link = "http://localhost:3000{0}".format(articles.h3.a['href'])
    row = [title, summary, link]
    writer.writerow(row)
    
csv_file.close()
    

