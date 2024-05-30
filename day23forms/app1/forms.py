from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField (max_length=25)
    last_name = forms.CharField( max_length=25)
    email =  forms.EmailField()
    age = forms.IntegerField()

    def clean_first_name(self):
        data = self.cleaned_data["first_name"]

        if not(data.isalpha()) or len(data)<3:

            raise ValueError("name must be string and length must be greater than 3")
        
        return data
    
    def clean_age(self):
        data = self.cleaned_data["age"]

        if int(data)<=18:
            raise ValueError("age must be greater than and equal to  18")
        return data
    
    


    
    

