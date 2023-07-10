from datetime import date,datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Course, Category
data ={
    "programlama":"programlama kategorisindeki kurs listesi",
    "web-gelistirme":"web-gelistirme kategorisindeki kurs listesi",
    "mobil":"mobil kategorisindeki kurs listesi",
}

db = {
    "courses" : [
        {
            "title":"javascript kursu",
            "description":"javascript kursu aciklamasi",
            "imageUrl": "2.jpg",
            "slug": "javascript-kursu",
            "date": datetime.now(),
            "isActive": True,
            "isUpdated": True
        },
        {
            "title":"python kursu",
            "description":"python kursu aciklamasi",
            "imageUrl": "3.jpg",
            "slug": "python-kursu",
            "date": date(2022,9,10),
            "isActive": False,
            "isUpdated": True
        },
        {
            "title":"web gelistirme kursu",
            "description":"web gelistirme kursu aciklamasi",
            "imageUrl": "1.jpg",
            "slug": "web-gelistirme-kursu",
            "date": date(2022,8,10),
            "isActive": True,
            "isUpdated": False  
        }
    ],
    "categories": [
        {"id":1, "name":"programlama","slug":"programlama"}, 
        {"id":2, "name":"web gelistirme","slug":"web-gelistirme"}, 
        {"id":3, "name":"mobil uygulamalar","slug":"mobil"},
        ]
}

# Create your views here.


def index(request):
    
    kurslar = Course.objects.filter(isActive=1)
    kategoriler = Category.objects.all()

    return render(request, 'courses/index.html',{
        'categories': kategoriler,
        'courses': kurslar
    })


def details(request, slug):
    # try:
    #     course = Course.objects.get(pk=kurs_id)
    # except:
    #     raise Http404()
    course = get_object_or_404(Course, slug=slug)
    context = {
        'course': course
    }
    
    return  render(request, 'courses/details.html', context)


def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name] 
        return render(request, 'courses/kurslar.html',{
            'category': category_name,'category_text': category_text})
    except:
        return HttpResponseNotFound("yanlis kategori secimi")

    


def getCoursesById(request, category_id):
    category_list = list(data.keys())
    if(category_id > len(category_list) or category_id < 1):
        return HttpResponseNotFound("yanlis kategori secimi")
    
    category_name = category_list[category_id-1]
    redirect_url = reverse("courses_by_category", args=[category_name])

    return redirect(redirect_url)
