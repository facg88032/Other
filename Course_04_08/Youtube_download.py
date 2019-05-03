from pytube import YouTube
import requests ,re
videoList=[]
# url='https://www.youtube.com/watch?v=HbSitAjGo6U'
url='https://www.youtube.com/watch?v=w1AKzkYj6T8&amp;list=PLuDDmFtAAumQkWz4hDX4sGR-DcTQVGoa8&amp;index=1'
html=requests.get(url)
r=re.findall(r'/watch[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%?=~_|]',html.text)
for i in r :
    if 'list=' and 'index='  in i:
        if not 'feature' in i:
            if i not in videoList:
                videoList.append(i)

for video in videoList:
    url='https://www.youtube.com/'+video
    
    yt = YouTube(url)
    print("開始下載:"+yt.title)
    yt.streams.first().download(output_path='D:\Downloads',filename=yt.title)
    print("Finished Download")
# yt=YouTube(url)
# print(yt.streams.filter(subtype='mp4',res='720p').first())
# yt.streams.filter(subtype='mp4',res='720p').first().download(output_path='D:\Downloads')
# for item in yt.streams.filter(subtype='mp4',res='720p').all():
#     print(item)
# print("開始下載:"+yt.title)
# yt.streams.first().download(output_path='D:\Downloads',filename="1"+yt.title)
# print("Finished Download")