from django.shortcuts import render

def input(request):
    return render(request, 'pdf/input.html')