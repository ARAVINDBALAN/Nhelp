from django.shortcuts import render
from .models import * 
from django.contrib import messages
# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views import generic
from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages 

def home(request):
    pst = post.objects.all().order_by('datesub')
    return render(request,'happiness/home.html',{'post':pst})


@login_required
def createpost(request):
    if request.method == "POST":
        postform = postcreate(request.POST)
        if postform.is_valid():
            post1=postform.save(commit=False)
            post1.author = request.user
            post1.datesub = timezone.now()
            post1.save()
    else:
        postform = postcreate()
    return render(request,'happiness/posts.html',{'postform':postform})       

def signup(request):
    if request.method == 'POST':
        signform = SignUpForm(request.POST,request.FILES)
        if signform.is_valid():
            signform.save()
            email = signform.cleaned_data.get('email')
            raw_password = signform.cleaned_data.get('password1')
            user = authenticate(email=email,password=raw_password)
            return redirect('home')
    else:
        signform = SignUpForm()
    return render(request,'happiness/signup.html',{'signupform':signform})            

@login_required
def delete_post(request,id,user_id):
    del_ob = post.objects.get(id=id)
    if (del_ob.post_author.id == user_id):
        del_ob.delete()    
    pst = post.objects.all()
    return render(request,'blog/index.html',{'post':pst})

@login_required
def getclaims(request,user_id,id):
    pst = post.objects.get(id=id)
    if pst.claims.filter(id=user_id).exists():
        pst.claims.remove(request.user)
    else:
        pst.claims.add(request.user)
    Post = post.objects.all().order_by('-datesub')    
    context = {'post': Post}
    return render(request,'happiness/viewpost.html',context=context)    


@login_required
def getreport(request):
    pst = post.objects.get(id=id)
    if pst.reports.filter(id=user_id).exists():
        pst.reports.remove(user)
    else:
        pst.reports.add(user)
    Post = post.objects.all().order_by('-datesub')    
    context = {'post': Post}
    return render(request,'happiness/home.html',context=context) 
    

def viewpost(request):
    p = post.objects.all().order_by('-datesub')[:3]
    return render(request,'happiness/viewpost.html',{'post':p})


def editprofile(request):
    if request.method == "POST":
        form = EditProfile(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'User details changed successfully')
            #return redirect('home')
    else :
        form = EditProfile()
    return render(request,'happiness/changeuser.html',{'form':form})