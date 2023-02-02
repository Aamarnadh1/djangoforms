from django import forms


class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(min_value=5)
    email=forms.EmailField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
   
   
    
    