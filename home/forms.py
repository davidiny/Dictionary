from django import forms

class MyForm(forms.Form):

    word = forms.CharField(max_length=20)
