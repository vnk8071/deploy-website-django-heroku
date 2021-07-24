from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
class RegistrationForm(forms.Form):
    username = forms.CharField(label= 'User name', max_length= 50)
    email = forms.EmailField(label= 'Email')
    password = forms.CharField(label= 'Password', widget=forms.PasswordInput())
    password_new = forms.CharField(label= 'Input password again', widget=forms.PasswordInput())

    def clean_password_new(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            password_new = self.cleaned_data['password_new']
            if password == password_new and password:
                return password_new
        raise forms.ValidationError('Not correct password')

    def clean_username(self):
        username= self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("User name have invalid character")
        try:
            User.objects.get(username= username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("User name have used")

    def save(self):
        User.objects.create_user(username= self.cleaned_data['username'], email= self.cleaned_data['email'], password= self.cleaned_data['password'])