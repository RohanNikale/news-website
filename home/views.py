from django.shortcuts import render,redirect
import json
import requests
from .models import message

# Create your views here.
def home(request):
    if request.method == "POST":
        email=request.POST.get('email') 
        messages=request.POST.get('message')
        data=message(email=email, text_field=messages)
        data.save()
        return redirect('/')
    api="https://newsapi.org/v2/top-headlines?country=in&apiKey=23dc71aa3f384611a9bc741c4cdbb122"
    tech='https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=23dc71aa3f384611a9bc741c4cdbb122'
    a=requests.get(api)
    data=json.loads(a.content)
    b=requests.get(tech)
    technology=json.loads(b.content)
    # print(data['articles'][0]['description'])
    LATEST=data['articles']
    top=data['articles']
    technews=technology['articles']
    return render(request, 'index.html',{'LATEST':enumerate(LATEST),'top':enumerate(top),'tech':enumerate(technews)})

def news(request):
    if request.method == 'GET':
        search=request.GET.get('search')
        api=f"https://newsapi.org/v2/everything?q={search}&from=2022-06-25&to=2022-06-25&sortBy=popularity&apiKey=23dc71aa3f384611a9bc741c4cdbb122"
        print(api)
        a=requests.get(api)
        data=json.loads(a.content)
        search=data['articles']
        return render(request, 'news.html',{"search":search})
    return redirect('/')