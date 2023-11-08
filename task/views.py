from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login as loginUser,logout
from task.forms import LoginForm, SignupForm, TasklistForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required
from task.models import Profileimg, Tasklist

# Create your views here.
def signuppage(request):
    if request.method == "POST": 
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your account has been created! now you are able to log in.")
            return redirect("loginpage")
        else:
            return redirect("signuppage")
    else:
        form = SignupForm()
    return render(request,"signup.html",{'form':form})

def loginpage(request):
    if request.method == "POST":
        form = LoginForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                loginUser(request,user)
                return redirect("homepage")
            else:
                return redirect("loginpage")
    else:
        form = LoginForm()
    return render(request,"login.html",{'form':form})

def logoutpage(request):
    logout(request)
    return redirect("loginpage")

@login_required()
def homepage(request):
    if request.user.is_authenticated:
        user = request.user
        form = TasklistForm()
        task = Tasklist.objects.filter(user=user)
        profilepic = Profileimg.objects.get(user=request.user).profilepic.url

        context = {
            'form':form,
            'task':task,
            'profilepic':profilepic,
        }
    
        return render(request,"home.html",context)

def addtask(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TasklistForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            task.save()
            return redirect("homepage")
        else:
            form = TasklistForm
    return render(request,"home.html",{'form':form})

def deletetask(request,id):
    form = Tasklist.objects.get(id=id)
    form.delete()
    return redirect("homepage")

def change_status(request,id,status):
    form = Tasklist.objects.get(id=id)
    form.status = status
    form.save()
    return redirect("homepage")

def myprofile(request):
    user = request.user
    
    context = {
        "user":user,
        
    }
    return render(request,"profile.html",context)


@login_required
def updateprofile(request):
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            # Handle the profile picture update
            profilepic = request.FILES.get('profilepic')
            if profilepic:
                profile_img, created = Profileimg.objects.get_or_create(user=request.user)
                profile_img.profilepic = profilepic
                profile_img.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('updateprofile')
    else:
        form = UpdateProfileForm(instance=request.user)
    return render(request, 'updateprofile.html', {'form': form})