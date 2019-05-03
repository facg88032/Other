import requests
import re
from bs4 import BeautifulSoup
import pandas
import matplotlib.pyplot as plt
url="https://www.cambridgeenglish.org/blog/relationship-between-tech-and-the-english-language-teacher/"
html=requests.get(url)

sp=BeautifulSoup(html.text,'lxml')
item=sp.select(".panel__body")
source=item[1].text
print(source)

w=re.findall('[a-zA-Z]',source)


dic={}
for i in range(26):
    dic[chr(65+i)]=0

for i in w:
    k=i.upper()
    dic[k]=dic[k]+1

# print(dic)
#
# datas=[1,2,3,4,5]
# index=['k','t','a','j','g']

df=pandas.DataFrame(dic.values(),index=dic.keys())

df.plot(kind="bar")
plt.savefig('hw2.png')
plt.show()

