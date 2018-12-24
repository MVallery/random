from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuestionsTEKSForm
from .forms import CustomizeForm
from .models import QuestionsTEKS
from django.http import HttpResponseRedirect

def home(request):
    # add if statements- if logged in: display___ else: display___
    return render(request, 'main/home.html', {'title': 'home'})


def customize(request):
    return render(request, 'main/customize.html', {'title': 'customize questions'})


def gen_questions_view(request):
    form = QuestionsTEKSForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CustomizeForm()
    context = {
        'form': form
    }
    return render(request, "main/gen_questions.html", context)


def customize_view(request):
    form = CustomizeForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CustomizeForm()
    context = {
        'form': form
    }
    return render(request, "main/customize.html", context)
def gen_custom_view(request):
    form = QuestionsTEKSForm(request.POST or None)
    customform = CustomizeForm(request.POST or None)
    if form.is_valid():
        form.save()
        # form = CustomizeForm()
    if customform.is_valid():
        customform.save()
        # customform = CustomizeForm()
    context = {
        'form': form,
        'customform': customform,
    }
    return render(request, "main/gen_questions.html", context)



# def gen_custom_view(request):
#     form = QuestionsTEKSForm(request.POST or None)
#     customform = CustomizeForm(request.POST or None)
#     if request.method =='POST':
#         if form.is_valid():
#             form.save()
#             #form = CustomizeForm()
#         if customform.is_valid():
#             customform.save()
#             #customform = CustomizeForm()
#     context = {
#         'form': form
#     }
#     return render(request, "main/gen_questions.html", context)
def create_data(request):
    form = QuestionsTEKSForm(request.POST)
    customform = CustomizeForm(request.POST)

    if form.is_valid():
        # process form data
        obj = QuestionsTEKS()  # gets new object
        obj.numQ = form.cleaned_data['numQ']
        obj.TEKS = form.cleaned_data['TEKS']
        # finally save the object in db
        obj.save()
        if obj.TEKS == '5.2B':
            pass

        return HttpResponseRedirect('/')

    if customform.is_valid():
        # process form data
        obj = QuestionsTEKS()  # gets new object
        obj.levels = customform.cleaned_data['levels']
        obj.specify = customform.cleaned_data['specify']
        # finally save the object in db
        obj.save()
        #return HttpResponseRedirect('/')
    context = {
        'form': form,
        'customform': customform,
    }
    return render(request, "main/gen_questions.html", context)
