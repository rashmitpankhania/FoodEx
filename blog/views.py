from django.shortcuts import render
from django.http import HttpResponse
from .models import Items
import datetime

def home(request):
    items = Items.objects.all()
    content = {
        'items':items,
    }
    return render(request, 'front.html', content)


def payment(request):
    return HttpResponse('this is Payment')

def cart(request):
    return HttpResponse('this is cart')