from django import forms
from .models import QuestionsTEKS


class QuestionsTEKSForm(forms.ModelForm):
    class Meta:
        model = QuestionsTEKS
        fields = [
            'numQ',
            'TEKS',
        ]

LEVELS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)
SPECIFY = (
    ('1', 'order decimals'),
    ('2', 'compare decimals'),
    ('3', 'both'),
)


class CustomizeForm(forms.Form):
    levels = forms.ChoiceField(widget=forms.RadioSelect, choices=LEVELS)
    specify = forms.ChoiceField(widget=forms.RadioSelect, choices=SPECIFY)
