# import requests
#
# payload={'key1':'value1','key2':'value2'}
# #偽裝 防止被發現是用Python進入
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}
# url='http://httpbin.org'
# html=requests.get(url,params=payload,headers=headers)
# print(html.headers)
import requests

url='http://aaa.24ht.com.tw'
html=requests.get(url,headers=headers)
html.encoding="utf-8"
print(html.text)
# if html.status_code==requests.codes.ok:
#     print(html.text)