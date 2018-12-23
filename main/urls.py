from django.urls import path, include
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),  # include is a function that allows you to connect urls??
    path('custom/', views.custom, name="custom-home"),
    path('gen_questions/', views.gen_questions, name="gen_questions"),
]

def home(request):
    return HttpResponse('<h1>Randomizer Home</h1>')

