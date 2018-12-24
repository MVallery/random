from django.urls import path, include
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),  # include is a function that allows you to connect urls??
    path('customize/', views.customize_view, name="customize-home"),
    path('gen_questions/', views.create_data, name="gen_questions"),
]

def home(request):
    return HttpResponse('<h1>Randomizer Home</h1>')

