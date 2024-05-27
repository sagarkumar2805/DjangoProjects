from django import forms

class Register(forms.Form):
    first_name = forms.CharField (max_length=25)
    last_name = forms.CharField( max_length=25)
    email =  forms.EmailField()
    age = forms.IntegerField()

