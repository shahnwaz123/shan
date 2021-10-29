# from os import openpty
import requests
from bs4 import BeautifulSoup
from requests.exceptions import URLRequired
# import urllib
import random

response=requests.get("https://en.wikipedia.org/wiki/Elon_Musk")
soup=BeautifulSoup(response.text,"html.parser")
# print(soup.prettify())
elon_musk_image=[]
all_images_tags=soup.find_all("img")

for image in all_images_tags:
    elon_musk_image.append(image['src'])

# Download karna hai
for elon in elon_musk_image:
    image_data=requests.get("https:"+elon)
    with open(str(random.randint(1,1000))+".png","wb") as file:
        file.write(image_data.content)
        print("Downloaded",str(random.randint(1,1000))+".png")

