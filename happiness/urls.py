"""nhelp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from .views import *
from django.urls import path

urlpatterns = [
    path('home/',home,name='home'),
    path('signup/',signup,name='signup'),
    path('viewpost/',viewpost,name='viewpost'),
    path('bevolunteer',bevolunteer,name='bevolunteer'),
    path('createpost/',createpost,name='createpost'),
    path('like/<int:user_id>/<int:id>',getclaims,name='getclaims'),
    path('report/<int:user_id>/<int:id>',getreport,name='getreports'),
    path('myposts/',mypost,name='mypost'),
    path('contact/',contactus,name='contact'),
    path('editprofile/',editprofile,name='editprofile'),
    path('assignvolunteers/<int:user_id>/<int:id>',assignvoluteer,name='assignvolunteer'),
]
