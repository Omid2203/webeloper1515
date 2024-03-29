"""webel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views
from course import views as appview
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('signup/', views.signup, name="signup"),
    path('login/', views.loginview, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contact, name="contact"),
    path('contactdone/', views.contactdone, name='contactdone'),
    path('userprofile/', views.userprofile, name="userprofile"),
    path('userprofileedit/', views.userprofileedit, name="userprofileedit"),
    path('panel/', views.panel, name="panel"),
    path('courses/', appview.course, name="courses"),
    path('courselist/', appview.CourseListView.as_view(), name='courselist'),



]
