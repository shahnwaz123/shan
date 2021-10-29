import requests
from bs4 import BeautifulSoup

response=requests.get("http://example.com/")
# print(response.text)
soup=BeautifulSoup(response.text,'html.parser')
# print(soup.prettify())
print(soup.title)
heading=soup.find("h1")
print(heading.text)
