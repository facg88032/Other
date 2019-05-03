import requests
from bs4 import BeautifulSoup
url="http://aaa.24ht.com.tw"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
html=requests.get(url,headers=headers)
html.encoding='utf-8'
print(html.text)

sp=BeautifulSoup(html.text,'lxml')

# print(sp.title)
# print(sp.title.text)
#

# print(sp.find('h1').text)
# item=sp.find_all('h1')
# print(sp.find_all('h1')[0].text)

# for u in item:
#     print(u.text)

item=sp.select('#author')
print(item[0])
