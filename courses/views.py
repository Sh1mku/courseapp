from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

data ={
    "programlama":"programlama kategorisindeki kurs listesi",
    "web-gelistirme":"web-gelistirme kategorisindeki kurs listesi",
    "mobil":"mobil kategorisindeki kurs listesi",
}

# Create your views here.

def kurslar(request):
    return HttpResponse('kurs listesi')

def details(request, kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfasi")

def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name] 
    except:
        HttpResponseNotFound("yanlis kategori secimi")


    return HttpResponse(category_text)

def getCoursesById(request, category_id):
    category_list = list(data.keys())
    if(category_id > len(category_list) or category_id < 1):
        return HttpResponseNotFound("yanlis kategori secimi")
    
    category_name = category_list[category_id-1]
    redirect_url = reverse("coursers_by_category", args=[category_name])

    return redirect(redirect_url )