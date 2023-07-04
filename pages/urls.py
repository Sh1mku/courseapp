from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('anasayfa', views.home),
    path('hakkimizda', views.hakkimizda),
    path('iletisim', views.iletisim),
]
