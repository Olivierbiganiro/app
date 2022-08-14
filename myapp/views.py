from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from myapp.models import Database, Profile
from .forms import  DatabaseForm, ProfileEditForm, UserEditForm, contactform, profileForm, registration
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def logoutsite(request):
    logout(request)
    messages.success(request, " You logout success")
    return redirect('home1')
    
@login_required(login_url='signin')   
#@allowed_users(allowed_roles=['Profile'])
def profiledata(request):
    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.owner=request.user.id
            profile.save()
            return HttpResponseRedirect('edit')

    form = profileForm()
    return render(request, 'profile.html', {'forms': form})

# save data in database Datab 
@login_required(login_url='signin')
def datab_data(request):
    if request.method == 'POST':
        form = DatabaseForm(request.POST, request.FILES)
        if form.is_valid():
            videos=form.save(commit=False)
            videos.owner=request.user.id
            videos.save()
            return HttpResponseRedirect('home')

    form = DatabaseForm()
    return render(request, 'form.html', {'forms': form})
@login_required(login_url='signin')    
def home1(request):
    #video={Database.objects.all()}
    context = {
       'video':Database.objects.all(),
       'profile':Profile.objects.all()
       }
    return render(request, 'home1.html', context)    

#@login_required(login_url='login')
@login_required(login_url='signin') 
def home(request):
    #video={Database.objects.all()}
    context = {
       'video':Database.objects.all(),
       'profile':Profile.objects.all()
       }
    return render(request, 'home1.html', context)

def signin(request):
    form = registration()
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            return redirect('home1')
        else:
            messages.info(request, 'incorrect user')

    return render(request, 'signin.html', {'form': form})


def register(request):
    form = registration()
    if request.method == 'POST':
        form = registration(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            #Profile.objects.create(User=User)
            messages.success(request, 'thank for create account success \t' + user)
            return redirect('signin')
    return render(request, 'register.html', {'form': form})
    
@login_required(login_url='signin') 
def contactdata(request):
    form=contactform()
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            messages.success(request, ' thank you for contact us \t' + user)
            return redirect('home1')
    return render(request, 'contact.html', {'form': form})

@login_required(login_url='signin') 
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                data=request.POST)
        profile_form = ProfileEditForm(
                instance=request.user.profile,
                data=request.POST,
                files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return render(request, 'home1.html')
        else:
            messages.error(request, 'Error updating your profile')
            return render(request, 'profile.html')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                    'edit.html',
                    {'user_form': user_form,
                        'profile_form': profile_form})

def play(request):
    context={
       'video':Database.objects.all(),
    }
    return render(request, 'play.html',context)
