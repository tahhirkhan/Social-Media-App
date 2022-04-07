from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Post, Profile

class addPostForm(forms.ModelForm):
	postImage = forms.ImageField()
	postDescription = forms.CharField(widget=forms.Textarea())


	class Meta:
		model = Post
		fields = ['postImage', 'postDescription']


class registerUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class addProfileForm(forms.ModelForm):
	avatar = forms.ImageField()
	bio = forms.CharField(max_length=300, widget=forms.Textarea())
	website_url = forms.CharField(max_length=200)

	class Meta:
		model = Profile
		fields = ['avatar', 'bio', 'website_url']