from django import forms
from . import models

class MainForm(forms.Form):
    numQ = forms.CharField()


