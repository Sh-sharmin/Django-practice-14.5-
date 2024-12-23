from django import forms
import datetime
from .models import Author

class ExampleForm(forms.Form):
    name = forms.CharField(label="Enter Your Name")
    comment = forms.CharField(max_length = 100,widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField(help_text="Enter 2 Digits")
    cg = forms.FloatField()
    day = forms.DateField(initial=datetime.date.today())
    Time = forms.TimeField( required=False ) 
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES,widget=forms.RadioSelect)
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES,widget=forms.CheckboxSelectMultiple)
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(), 
        widget=forms.Select(attrs={'class': 'form-control'})
    )