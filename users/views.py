from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from .forms import CustomUserCreationForm

def intro(request):
    return render(request,'users/intro.html')

def profiles(request):
    Profiles=Profile.objects.all()
    context={'Profiles':Profiles}
    return render(request,'users/profiles.html',context)

def userprofile(request,pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile': profile,'topSkills':topSkills,"otherSkills":otherSkills}
    return render(request,'users/user-profile.html',context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')
    page='login'
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'username does not exist')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request,'username or password is incorrect')

    return render(request,'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.info(request,'user was logged out!')
    return redirect('login')

def registerUser(request):
    page='register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username=user.username.lower()
            user.save()

            messages.success(request,'user account was created!')

            login(request,user)
            return redirect('profiles')
        else:
            messages.success(request,'an error has occurred')
    context={'page':page,'form':form}
    return render(request,'users/login_register.html',context)