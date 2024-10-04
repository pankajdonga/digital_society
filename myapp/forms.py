from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordResetForm
from .models import *


class CustomUserForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','email','password1','password2','mobile','birthdate','gender','address','adhar','profile_img','membertype','gate','city','state','is_staff']


class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','email','mobile','birthdate','gender','address','adhar','profile_img','membertype']
        


class CustomPasswordResetForm(PasswordResetForm):
    class Meta:
        model=CustomUser
        fields=['email']     
        