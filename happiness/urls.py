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
    path('fulfilled/<int:user_id>/<int:post_id>',makefulfilled,name='makefulfilled'),
    path('makeassisted/<int:user_id>/<int:post_id>',makeassited,name='makeassisted'),
    path('createpost/',createpost,name='createpost'),
    path('like/<int:user_id>/<int:id>',getclaims,name='getclaims'),
    path('report/<int:user_id>/<int:id>',getreport,name='getreports'),
    path('activepost/<int:p_id>',activepost,name='activepost'),
    path('myposts/',mypost,name='mypost'),
    path('claimit/<int:user_id>/<int:id>',claimit,name='claimit'),
    path('assistit/<int:user_id>/<int:id>',assistit,name='assistit'),
    path('reportpost/<int:user_id>/<int:id>',reportpost,name='reportpost'),
    path('ho/<int:p_id>',ho,name='ho'),
    path('contact/',contactus,name='contact'),
    path('viewprofile/<int:user_id>',viewprofile,name='viewprofile'),
    path('profile/',profile,name='profile'),
    path('editprofile/',editprofile,name='editprofile'),
    path('assignvolunteers/<int:user_id>/<int:id>',assignvoluteer,name='assignvolunteer'),
]
