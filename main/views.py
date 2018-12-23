from django.shortcuts import render
from django.forms.fields import IntegerField
from django.http import HttpResponse


def home(request):
    # return HttpResponse('<h1>Randomizer Home</h1>')

    ##add if statements- if logged in: display___ else: display___
    return render(request, 'main/home.html', {'title': 'home'})
# Create your views here.


def custom(request):
    # return HttpResponse('<h1>This is the customizer</h1>')
    return render(request, 'main/custom.html', {'title': 'customize questions'})


def gen_questions(request):
    # return HttpResponse('<h1>This is the question generator</h1>')
    return render(request, 'main/gen_questions.html', {'title': 'generate questions'})



