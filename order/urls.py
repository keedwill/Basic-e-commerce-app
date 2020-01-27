from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('cart/<product_id>/<prod_price>/', views.cart,name='cart'),
    path('cart/<product_id>/<int:prod_price>/register/',views.register),
]
