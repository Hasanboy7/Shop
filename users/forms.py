from typing import Any
from django import forms
from .models import User

class LoginForms(forms.Form):
    username=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':"form-control"}))
    password=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':"form-control"}))

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))  # Use forms.EmailField
    password1 = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    photo=forms.ImageField(required=True,widget=forms.FileInput(attrs={'class': "form-control"}))

    
    def clean_password(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password1 != password2:
            raise forms.ValidationError("Parollaringiz ikki xil")

        return cleaned_data

class Profile(forms.ModelForm):

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','phone_number','photo','bio')

    