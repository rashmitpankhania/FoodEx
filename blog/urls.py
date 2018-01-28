from django.conf.urls import url
from . import views

app_name = 'FoodEx'

urlpatterns = [
    url(r'home/$', views.home, name='home'),
    url(r'payment/$', views.payment, name='payment'),
    url(r'cart/$', views.cart, name='cart')
]