from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Product
# Create your views here.

def shop(request):
    product_objects = Product.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)
    # Paginator
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'ecom/index.html', {'product_objects': product_objects})

def product_detail(request, id):
    product_object = Product.objects.get(id=id)
    return render(request, 'ecom/detail.html', {'product_object': product_object})