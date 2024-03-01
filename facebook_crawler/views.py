import requests

from django.shortcuts import render
from django.http import HttpResponseRedirect
from bs4 import BeautifulSoup

from .models import Link, Keyword
import pandas as pd


def clear(request):
    Link.objects.all().delete()
    return render(request, 'facebook_crawler/index.html')

def index(request):
    ## default value
    data = []
    ## POST -> add new keyword
    if request.method == "POST":
        word = request.POST.get('site', '')
        new_keyword = Keyword(user= request.user, word=word)
        new_keyword.save()
        return render(request, 'facebook_crawler/index.html', {'data': data})

    ## else, read keyword, scrape show result 
    else:
        keywords = Keyword.objects.filter(user=request.user)
        if len(keywords) == 0:
            print("There is no keyword registered")
            return render(request, 'facebook_crawler/index.html', {'data': data})
        query_word = []
        for keyword in keywords:
            query_word.append(keyword.word)
        
        base_url = "https://www.nature.com/search?q="
        url = base_url + " ".join(query_word) + "&journal="
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "lxml")
        print(page.text)

        icon_part = soup.find_all("ul", class_="app-article-list-row")
        data = []
        for ul_tag in icon_part:
            for li in ul_tag.find_all('li'):
                datum = li.text.split("\n")
                cleaned_data = []
                for d in datum:
                    if len(d) > 0:
                        cleaned_data.append(d)
                if len(cleaned_data) > 1:
                    data.append(cleaned_data)
        return render(request, 'facebook_crawler/index.html', {'data': data})
