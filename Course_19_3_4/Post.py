import requests

payload={'key1':'value1','key2':'value2'}
#偽裝 防止被發現是用Python進入
#headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}
url='http://httpbin.org/post'
html=requests.post(url,data=payload)
print(html.text)