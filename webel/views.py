from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SignUpForm, Contact
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.mail import BadHeaderError, send_mail


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            return redirect('home')
        username = request.POST['username']
        password = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        if password != password2:
            return render(request, 'signup.html', context={"error": "گذرواژه و تکرار گذرواژه یکسان نیستند"})
        user = User.objects.filter(username=str(username)).count()
        if user > 0:
            return render(request, 'signup.html', context={"error": "نام کاربری شما در سیستم موجود است "})
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

def contact(request):
    if request.method == "GET":
        form = Contact()
    else:
        form = Contact(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            try:
                send_mail(title, text, email, ['webe19lopers@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contactdone')
    return render(request, "contact.html", {'form': form})

def contactdone(request):
    return render(request, 'contactdone.html')