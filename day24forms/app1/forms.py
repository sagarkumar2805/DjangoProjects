from django import forms

class EmployeeForm(forms.Form):
    eName = forms.CharField(max_length=25)
    eAge = forms.IntegerField()
    email = forms.EmailField()