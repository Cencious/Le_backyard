from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Post,Business,NeighbourHood


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'prompt srch_explore'}), max_length=50, required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'prompt srch_explore'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'prompt srch_explore'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'prompt srch_explore'}))

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content','image')


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('name', 'email','description','image')
class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ('admin',)



