from datetime import date,datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Course, Category, Slider
from django.core.paginator import Paginator
from .forms import *
from django.contrib.auth.decorators import login_required, user_passes_test


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
    
    kurslar = Course.objects.filter(isActive=1,isHome=1)
    kategoriler = Category.objects.all()
    sliders=Slider.objects.filter(is_active=True)

    return render(request, 'courses/index.html',{
        'categories': kategoriler,
        'courses': kurslar,
        'sliders': sliders
    })


def isAdmin(user):
    return user.is_superuser

@user_passes_test(isAdmin)
def create_course(request):
    if request.method == "POST":
        form=CourseCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/kurslar")
    else:
        form = CourseCreateForm()

    return render(request, 'courses/create-course.html',{"form" :form})
    # alternate way to use post requests
    
    #     title = request.POST["title"]
    #     description = request.POST["description"]
    #     imageUrl = request.POST["imageUrl"]
    #     slug = request.POST["slug"]
    #     isActive = request.POST.get("isActive", False)
    #     isHome = request.POST.get("isHome", False)

    #     if isActive == "on":
    #         isActive = True

    #     if isHome == "on":
    #         isHome = True

    #     error=False
    #     msg = ""

    #     if title == "":
    #         error = True
    #         msg+= "title alani boş birakilamaz "
            
    #     if len(title) < 5:
    #         error = True
    #         msg+= "title alani en az 5 karakter olmalidir  "
 
    #     if error:
    #         return render(request, 'courses/create-course.html', {"error": True, "msg": msg})

        # kurs = Course(title=title, description=description, imageUrl=imageUrl, slug=slug, isActive=isActive, isHome=isHome)
        # kurs.save()
        # return redirect("/kurslar")
    
@login_required()
def course_list(request):
    kurslar = Course.objects.all()
    return render(request, 'courses/course-list.html', {
        'courses':kurslar
    })

def course_edit(request,id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        form = CourseEditForm(request.POST, instance=course)
        form.save()
        return redirect("course_list")
    else:
     form = CourseEditForm(instance=course)
    
    return render(request, "courses/edit-course.html",{"form":form})

def course_delete(request,id):
    course = get_object_or_404(Course,pk=id)

    if request.method=="POST":
        course.delete()
        return redirect("course_list")
    return render(request,"courses/course-delete.html", {"course":course })

def search(request):
    if "q" in request.GET and request.GET["q"] !=  "":
    
        q = request.GET["q"]
        kurslar = Course.objects.filter(isActive=True,title__contains=q).order_by("date")
        # print(kurslar)
        kategoriler = Category.objects.all()
    else:
        return redirect('/kurslar')

    return render(request, 'courses/search.html',{
        'categories': kategoriler,
        'courses': kurslar,
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


def getCoursesByCategory(request, slug):
    kurslar = Course.objects.filter(categories__slug=slug,isActive=True).order_by('date')
    kategoriler = Category.objects.all()

    paginator = Paginator(kurslar, 3)
    page = request.GET.get('page',1)
    page_obj = paginator.get_page(page)

    print(page_obj.paginator.count)
    print(page_obj.paginator.num_pages)

    return render(request, 'courses/list.html',{
        'categories': kategoriler,
        'page_obj': page_obj,
        'seciliKategori': slug
    })   
    
    # try:
    #     category_text = data[category_name] 
    #     return render(request, 'courses/kurslar.html',{
    #         'category': category_name,'category_text': category_text})
    # except:
    #     return HttpResponseNotFound("yanlis kategori secimi")

    


# def getCoursesById(request, category_id):
#     category_list = list(data.keys())
#     if(category_id > len(category_list) or category_id < 1):
#         return HttpResponseNotFound("yanlis kategori secimi")
    
#     category_name = category_list[category_id-1]
#     redirect_url = reverse("courses_by_category", args=[category_name])

#     return redirect(redirect_url)
