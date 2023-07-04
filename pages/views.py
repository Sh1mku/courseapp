from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('anasayfa')

def hakkimizda(request):
    return HttpResponse('hakkimizda sayfasi')

def iletisim(request):
    return HttpResponse('iletisim sayfasi')