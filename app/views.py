from django.shortcuts import render
from .models import Product, Seller, Buyer
import datetime


def index(request):
    product = Product.objects.all()
    seller = Seller.objects.all()
    context = {
        'products': product,
        'seller': seller,
    }
    return render(request, 'index.html', context=context)


def buy(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        quantity = int(request.POST['quantity'])

        buyer = Buyer(name=name, address=address, phone=phone)
        buyer.save()

        amount = float(product.price)
        product_name = product.name
        description = product.description
        product_quantity = quantity
        product_total = amount*quantity
        seller = Seller.objects.all()
        context = {
            'id': buyer.id,
            'product_date': datetime.datetime.now(),
            'product_name': product_name,
            'product': product,
            'buyer_name': name,
            'buyer_address': address,
            'buyer_phone': phone,
            'product_description': description,
            'product_price': amount,
            'product_quantity': product_quantity,
            'product_total': product_total,
            'seller': seller
        }
        return render(request, 'pdf.html', context)
    return render(request, 'buy.html')


def pdf(request):
    seller = Seller.objects.all()
    context = {
        'seller': seller

    }
    return render(request, 'pdf.html', context)
