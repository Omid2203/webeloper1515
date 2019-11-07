from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            return redirect('home')
        password = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        if password != password2:
            return render(request, 'signup.html', context={"error": "گذرواژه و تکرار گذرواژه یکسان نیستند"})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print('hello')
            if user is not None:
                login(request, user)
                return redirect('/')
        else:
            print('hi')
            return render(request, template_name='login.html', context={"error": "error is this!", "form": form})
    form = AuthenticationForm()
    return render(request, template_name="login.html", context={"form": form})



def logout_view(request):
    logout(request)
    return redirect('/')