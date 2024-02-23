from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Product, Order
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

def checkout(request):
    if request.method == "POST":
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address1 = request.POST.get('address1', "")
        address2 = request.POST.get('address2', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zip = request.POST.get('zip', "")

        order = Order(name=name, email=email, address1=address1, address2=address2, city=city, state=state, zip=zip)
        order.save()

    return render(request, 'ecom/checkout.html')