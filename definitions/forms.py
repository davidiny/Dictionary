from django import forms

class MyForm(forms.Form):

    word = forms.CharField(label="", help_text="", max_length=20)
