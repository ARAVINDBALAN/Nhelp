from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','first_name','last_name','is_also_volunteer','avatar','phone_no','password1','password2')



class postcreate(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title','message','location','timelimit')

class EditProfile(UserChangeForm):
    class Meta:
        model = User
        fields = ('email','first_name','last_name','is_also_volunteer','avatar','phone_no','password')