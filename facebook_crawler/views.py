from django.shortcuts import render

import requests
from bs4 import BeautifulSoup

def index(request):
    page = requests.get('https://www.google.com')
    soup = BeautifulSoup(page.text, 'html.parser')
    
    link_list = []
    for link in soup.find_all('a'):
        link_list.append(link.get('href'))

    return render(request, 'facebook_crawler/index.html', {'link_list': link_list})
