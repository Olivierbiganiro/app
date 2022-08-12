from email.policy import default
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Database, Profile, contact

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields ='__all__'
# database
class DatabaseForm(forms.ModelForm):
    class Meta:
        model = Database
        fields ='__all__'
        #['video', 'title', 'release_date', 'main_actors', 'genre', 'description', 'movie_poster', 'movie_trailer_link']


class registration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class contactform(forms.ModelForm):
    class Meta:
        model = contact
        fields ='__all__'       

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('gender', 'age', 'profile_image', 'registration_date')