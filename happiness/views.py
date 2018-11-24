from __future__ import unicode_literals
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
    if request.method == "POST":
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Message has been notified')
            return redirect('home')
            
    else :
        form = contactform()
    pst = post.objects.all().order_by('-datesub')
    user = request.user   
    return render(request,'happiness/home.html',{'post':pst,'user':user,'form':form})

@login_required
def bevolunteer(request):
    user = request.user
    if user.is_also_volunteer == False or user.is_also_volunteer == None:
        user.is_also_volunteer = True
        user.save()
        messages.success(request,'You Became a volunteer')
    else :
        user.is_also_volunteer = False
        user.save()
        messages.success(request,'You are not a volunteer anymore')    
    return redirect('home')    


def contactus(request):
    if request.method == "POST":
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else :
        form = contactform()
    return render(request,'happiness/home.html',{'form':form})    


@login_required
def makeassited(request,user_id,post_id):
    user = User.objects.get(id=user_id)
    pst = post.objects.get(id=post_id)
    if user.assisted.filter(id=post_id).exists():
        user.assisted.remove(pst)
    else:
        user.assisted.add(pst)
    Post = post.objects.all().order_by('-datesub')    
    context = {'post': Post}
    return redirect('mypost')    



@login_required
def profile(request):
    user = request.user
    pst = post.objects.filter(author=request.user).count()
    return render(request,'happiness/profile.html',{'ser':user,'co1':pst})

@login_required
def mypost(request):
    pst = post.objects.filter(author=request.user).order_by('-datesub')
    return render(request,'happiness/myposts.html',{'post':pst})

@login_required
def createpost(request):
    if request.method == "POST":
        postform = postcreate(request.POST)
        if postform.is_valid():
            post1=postform.save(commit=False)
            post1.author = request.user
            user = request.user
            post1.datesub = timezone.now()
            post1.save()
            user.served +=1
            user.save()
            return redirect('home')
    else:
        postform = postcreate()
    return render(request,'happiness/posts.html',{'postform':postform})       


@login_required
def activepost(request,p_id):
    pst = post.objects.get(id=p_id)
    print(pst)
    if pst.active_post == True :
        pst.active_post = False
        pst.save()
    else :
        pst.active_post = True
        pst.save()
    return redirect('mypost')

#from django.http import JsonResponse


@login_required
def claimit(request,user_id,id):
    pst = post.objects.get(id=id)
    if pst.claims.filter(id=user_id).exists():
        pst.claims.remove(request.user)
    else:
        pst.claims.add(request.user)
    p=pst.claims.count()    
    Post = post.objects.all().order_by('-datesub')
    data = {'claimcount':p }
    print(data)
    return JsonResponse(data)

@login_required
def assistit(request,user_id,id):
    pst = post.objects.get(id=id)
    if pst.volunteers.filter(id=user_id).exists():
        pst.volunteers.remove(request.user)
    else:
        pst.volunteers.add(request.user)
    p=pst.volunteers.count()    
    Post = post.objects.all().order_by('-datesub')
    data = {'assiscount':p }
    print(data)
    return JsonResponse(data)


@login_required
def reportpost(request,user_id,id):
    pst = post.objects.get(id=id)
    if pst.reports.filter(id=user_id).exists():
        pst.reports.remove(request.user)
    else:
        pst.reports.add(request.user)
    p=pst.reports.count()    
    Post = post.objects.all().order_by('-datesub')
    data = {'repcount':p }
    print(data)
    return JsonResponse(data)


def ho(request,p_id):
    pst = post.objects.get(id=p_id)
    print(pst)
    if pst.active_post == True :
        pst.active_post = False
        pst.save()
    else :
        pst.active_post = True
        pst.save()
    data = {'status':pst.active_post}
    return JsonResponse(data)
    


@login_required()
def viewprofile(request,user_id):
    user = User.objects.get(id=user_id)
    pst = post.objects.filter(author_id=user_id)
    print(user)
    return render(request,'happiness/profile1.html',{'ser':user,'co':pst})


@login_required
def makefulfilled(request,user_id,post_id):
    user = User.objects.get(id=user_id)
    pst = post.objects.get(id=post_id)
    if user.fulfilled.filter(id=post_id).exists():
        user.fulfilled.remove(pst)
    else:
        user.fulfilled.add(pst)
    Post = post.objects.all().order_by('-datesub') 
    use = User.objects.all()   
    context = {'post': Post,'user1':use}
    return render(request,'happiness/myposts.html',context=context) 


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
            messages.success(request,"Enter valid datas")    
    else:
        signform = SignUpForm()
    return render(request,'happiness/signup.html',{'signupform':signform})            



@login_required
def activeordel(request,p_id):
    pst = post.objects.get(id=p_id)
    print(pst)
    if pst.active_post == True :
        pst.active_post = False
        pst.save()
    else :
        pst.active_post = True
        pst.save()    
    data = {'status':pst.active_post}
    print(data)        
    return JsonResponse(data)


@login_required
def makefulfilledone(request,user_id,p_id):
    user = User.objects.get(id=user_id)
    pst = post.objects.get(id=p_id)
    if user.fulfilled.filter(id=p_id).exists():
        user.fulfilled.remove(pst)
    else:
        user.fulfilled.add(pst)
    Post = post.objects.all().order_by('-datesub') 
    use = User.objects.all() 
    p =  user.fulfilled.count()
    print(p)
    data = {'post': p}
    return JsonResponse(data)
    


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
def getreport(request,user_id,id):
    pst = post.objects.get(id=id)
    if pst.reports.filter(id=user_id).exists():
        pst.reports.remove(request.user)
    else:
        pst.reports.add(request.user)
    Post = post.objects.all().order_by('-datesub')
    context = {'post': Post}
    return render(request,'happiness/viewpost.html',context=context) 
    
@login_required
def viewpost(request):
    p = post.objects.all().order_by('-datesub')
    return render(request,'happiness/viewpost.html',{'post':p})


def editprofile(request):
    if request.method == "POST":
        form = EditProfile(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'User details changed successfully')
            #return redirect('home')
    else :
        form = EditProfile(instance=request.user)
    return render(request,'happiness/changeuser.html',{'form':form})

def assignvoluteer(request,user_id,id):
    pst = post.objects.get(id=id)
    if pst.volunteers.filter(id=user_id).exists():
        pst.volunteers.remove(request.user)
    else:
        pst.volunteers.add(request.user)
    Post = post.objects.all().order_by('-datesub')    
    context = {'post': Post}
    return render(request,'happiness/viewpost.html',context=context)