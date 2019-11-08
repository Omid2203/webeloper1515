from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test

from django.shortcuts import render, redirect

from django.conf import settings

from django.urls import reverse
from .forms import SignUpForm, Contact, EditProfileForm

from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import BadHeaderError, send_mail, EmailMessage



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():


            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password != password2:
                return render(request, 'signup.html', context={"error": "گذرواژه و تکرار گذرواژه یکسان نیستند"})
            user = User.objects.filter(username=str(username)).count()
            if user > 0:
                return render(request, 'signup.html', context={"error": "نام کاربری شما در سیستم موجود است "})
            form.save()
            return redirect('home')
        else:
            username = request.POST['username']
            password = request.POST['password1']
            password2 = request.POST['password2']
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
            title = request.POST['title']
            email = request.POST['email']
            email_from = settings.EMAIL_HOST_USER
            text = request.POST['text']
            print(title, text, email)
  #          send_mail(title, text, email_from, ['mohammadomid.79@gmail.com'])
   ##         email = EmailMessage(title, text, to=['mohammadomid.79@gmail.com'])
     #       email.send()
            return redirect('contactdone')
    return render(request, "contact.html", {'form': form})

def contactdone(request):
    return render(request, 'contactdone.html')

@login_required
def userprofile(request):
    username = request.user.username
    first_name = request.user.first_name
    last_name = request.user.last_name
    context = {
        'username':username,
        'first_name':first_name,
        'last_name':last_name,
    }
    return render(request, 'userprofile.html', context)

@login_required
def userprofileedit(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST,instance=request.user)
        first_name = request.user.first_name
        last_name = request.user.last_name
        context = {
            'first_name': first_name,
            'last_name': last_name,
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('userprofile')
    else:
        form = EditProfileForm(request.POST,instance=request.user)
        first_name = request.user.first_name
        last_name = request.user.last_name
        context = {
            'first_name': first_name,
            'last_name': last_name,
            'form': form,
        }
        return render(request, 'userprofileedit.html', context)

@login_required
def panel(request):
    return render(request, 'panel.html')


@user_passes_test(lambda u: u.is_superuser)
def my_view(request):
    pass