import requests

url='http://www.e-happy.com.tw'
html=requests.get(url)
html.encoding="utf-8"
print(html.status_code)
# if html.status_code==requests.codes.ok:
#     print(html.text)