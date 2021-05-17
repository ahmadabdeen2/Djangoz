# from django import forms

# CHOICES= [
#     ('Branding', 'Branding'),
#     ('Marketing', 'Marketing'),
#     ('mango', 'Mangoes'),
#     ('honeydew', 'Honeydews'),
#     ]

# class UserForm(forms.Form):
#     first_name= forms.CharField(max_length=100)
#     last_name= forms.CharField(max_length=100)
#     email= forms.EmailField()
#     age= forms.IntegerField()
#     favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.RadioSelect(choices=FRUIT_CHOICES))
from django import forms 
from .models import CustomerInfo

class CustomerForm(forms.ModelForm):
    class Meta():
        model = CustomerInfo
        fields = '__all__'
