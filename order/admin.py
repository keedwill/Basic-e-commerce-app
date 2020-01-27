from django.contrib import admin
from . models import Soap,OrderList


class SoapAdmin(admin.ModelAdmin):
    list_display =('name','price','stock')


admin.site.register(Soap,SoapAdmin)


class OrderListAdmin(admin.ModelAdmin):
    list_display =('first_name','second_name','address','phone_number','no_of_item','product_name','product_price','date','unit_cost','uuid')


admin.site.register(OrderList,OrderListAdmin)
