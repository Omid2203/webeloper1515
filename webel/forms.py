from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

class Contact(forms.Form):
    title = forms.CharField(required=True)
    text = forms.CharField(max_length=250, min_length=10,required=True)
    email = forms.EmailField(required=True)


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

















