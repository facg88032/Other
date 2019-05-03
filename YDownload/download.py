from pytube import YouTube
import requests, re
from argparse import ArgumentParser
from pydub import AudioSegment
parser=ArgumentParser()
parser.add_argument("--url",required=False,default='')
parser.add_argument("--subtype",required=False,default='mp4')
args=parser.parse_args()
videoList = []

url =args.url
if args.subtype == 'mp4':
    type = 'mp4'
else:
    type = 'webm'

download_local='C:/temp/'
html = requests.get(url)
r = re.findall(r'/watch[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%?=~_|]', html.text)

def download(url,count=0):
    yt = YouTube(url)
    print("開始下載:" + yt.title)  
    if type=='webm':
        title='File'+str(count)
        yt.streams.filter(subtype=type,abr='50kbps').last().download(output_path=download_local, filename=title)
        webm=AudioSegment.from_file(download_local+title+'.webm', format='webm')
        webm.export(download_local+title+'.mp3', format='mp3')
    elif type=='mp4':
        yt.streams.filter(subtype=type).first().download(output_path=download_local, filename=yt.title)
    else :
        pass    
    print("Finished Download")


def list():
    for i in r:
        if 'list=' and 'index=' in i:
            if not 'feature' in i:
                if i not in videoList:
                    videoList.append(i)

    count=0
    for video in videoList:
        url = 'https://www.youtube.com/' + video
        count+=1
        download(url,count)






for i in r :

    if 'list=' and 'index=' in i:
        list()
        break
    else :
        download(url)
        break



