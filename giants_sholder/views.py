from django.shortcuts import render

def index(request):
    return render(request, 'giants_sholder/index.html')

