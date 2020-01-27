from django.shortcuts import render
from .models import Soap, OrderList
from datetime import datetime
import uuid

uuid = uuid.uuid4()


def index(request):
    soap = Soap.objects.all()
    return render(request, 'order/index.html', {'soap': soap})


def cart(request, product_id, prod_price):
    product = Soap.objects.get(name=product_id)

    return render(request, 'order/cart.html', {'product': product})


def register(request, product_id, prod_price):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        second_name = request.POST['second_name']
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        no_of_item = int(request.POST['no_of_products'])
        product_name = product_id
        unit_cost = prod_price
        product_price = prod_price * no_of_item
        now = datetime.now()
        date = now.strftime('%Y-%m-%d %H:%M:%S')
        user = OrderList(first_name=first_name, second_name=second_name, address=address,
                         phone_number=phone_number, email=email, no_of_item=no_of_item, product_name=product_name,
                         product_price=product_price, date=date, unit_cost=unit_cost, uuid=uuid)
        user.save()
        buyer = OrderList.objects.get(id=user.pk)
        return render(request, 'order/receipt.html', {'buyer': buyer})

    else:
        return render(request, 'order/cart.html')
