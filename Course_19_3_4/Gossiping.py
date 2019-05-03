import requests
from bs4 import BeautifulSoup
payload={'from':'https://www.ptt.cc/bbs/gossiping/index.html',
         'yes':'yes'}

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}

rs=requests.Session()
rs.post('https://www.ptt.cc/ask/over18',data=payload,headers=headers)
html=rs.get('https://www.ptt.cc/bbs/gossiping/index.html',headers=headers)

sp=BeautifulSoup(html.text,'html.parser')

items=sp.select('.r-ent')
for i in range(len(items)):
    print(items[i].select('.title')[0].text)
    print(items[i].select('.date')[0].text)
    print(items[i].select('.author')[0].text)
    print(" ")