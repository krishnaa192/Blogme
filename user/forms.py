from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','email' ,'username', 'password1', 'password2']
    

    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class ProfileForm(ModelForm):
    class Meta:
            model = Profile
            fields = ['Name','email','Bio','auth_image','instagram','linkedin','twitter','github']


class CreateAccountForm(ModelForm):
     class Meta:
            model = Profile
            fields = ['Bio','auth_image','instagram','linkedin','twitter','github']
     