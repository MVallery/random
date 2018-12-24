from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms

TEKS_CHOICES = (
    ('5.2B', '5.2B Compare and Order Decimals'),
    ('5.4A', '5.4A Prime & Composite'),
    ('5.3K', '5.3K Add & Subtract Decimals'),
    ('5.4F', '5.4F Order of Operations'),
    ('5.3E', '5.3E Multiply Decimals'),
    ('5.3G', '5.3G Divide Decimals'),
    ('5.3K', '5.3K Add & Subtract Fractions'),
    ('5.3B', '5.3B Multiply Whole Numbers'),
    ('5.3C', '5.3C Divide Whole Numbers'),
    ('5.3L', '5.3L Divide Fractions'),
    ('5.4B', '5.4B Represent & Solve Multi-Step Equations'),
    ('5.4C', '5.4C Tables, Patterns, Equations, Graphs'),
    ('5.4H', '5.4H Perimeter Area Volume'),
    ('5.5A', '5.5A Classify Figures'),
    ('5.8C', '5.8C Coordinate Grid'),)
# Create your models here.


class QuestionsTEKS(models.Model):
    numQ = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    TEKS = models.CharField(max_length=10, choices=TEKS_CHOICES, default='green')


