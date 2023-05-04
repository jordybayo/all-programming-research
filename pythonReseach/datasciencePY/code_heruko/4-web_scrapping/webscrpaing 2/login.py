import requests
from bs4 import BeautifulSoup

session_requests = requests.session()

payload = {
	"email": "test123@codeheroku.com", 
	"password": "test123", 
	"_formname": "login"
}

login_url = "http://www.codeheroku.com/login"
result = session_requests.get(login_url)

soup = BeautifulSoup(result.content, 'html.parser')
tag = soup.find("input",attrs={'name':'_formkey'})
payload["_formkey"]= tag['value']
print(payload)

result = session_requests.post(
	login_url, 
	data = payload, 
	headers = dict(referer=login_url)
)

print(result.content)

url = 'http://www.codeheroku.com/dashboard/'
result = session_requests.get(
	url, 
	headers = dict(referer = url)
)

# print(result.content)