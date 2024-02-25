import requests

from django.shortcuts import render
from django.http import HttpResponseRedirect
from bs4 import BeautifulSoup

from .models import Link

def index(request):
    if request.method != "POST":
        return render(request, 'facebook_crawler/index.html')
    
    site = request.POST.get('site', "")
    if site == '':
        return render(request, 'facebook_crawler/index.html')
    page = requests.get(site)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    for link in soup.find_all('a'):
        link_address = link.get('href')
        link_text = link.string
        print(link_text, link_address)
        Link.objects.create(name=link_text, address=link_address) # don't need to save
    data = Link.objects.all()
    return render(request, 'facebook_crawler/index.html', {'link_list': data})
    return HttpResponseRedirect('') # redirect is wrong