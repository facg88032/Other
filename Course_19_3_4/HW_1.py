import requests
from bs4 import BeautifulSoup


headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}

html=requests.get('https://www.nfu.edu.tw/zh/',headers=headers)

sp=BeautifulSoup(html.text,'html.parser')

items=sp.select('.tab-content')[0].select('div.tab-pane.nn_tabs-pane')[0]
for i in range(len(items)):
    print(items.select('.moduleItemDateCreated')[i].text)
    print(items.select('.moduleItemTitle')[i].text)