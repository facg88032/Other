from django.shortcuts import render
import requests
import subprocess

def button(request):

    return render(request,'test.html')

def output(request):
    if request.method=='TTTT':
        data=requests.get("https://www.google.com/")
        print(data.text)
        data=data.text
        return render(request,'test.html',{'data':data})
    return render(request,'test.html')

def submit(request):
    if request.method=='POST':
       p=subprocess.Popen(['python.exe','download.py','--url',request.POST['info'],'--subtype',request.POST['subtype']])
       return render(request,'test.html')    
    return render(request,'test.html')
