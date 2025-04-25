import requests
from bs4 import BeautifulSoup

# resp = requests.get('http://httpbin.org/ip')
# print(resp.content.decode())

request = (requests.get('https://en.wikipedia.org/wiki/Main_Page'))
soup = BeautifulSoup(request.text, 'html.parser')
print(soup.prettify())   