from django import forms
from inoperate.models import Person
from captcha.fields import CaptchaField

class SearchForm(forms.Form):
    name = forms.CharField(max_length=100)
    account_number = forms.CharField(max_length=20)
    captcha = CaptchaField()