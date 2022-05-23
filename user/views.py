
from django.shortcuts import render
from .models import Profile
from django.shortcuts import redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm,ProfileForm
from blogging.models import Blog
from django.contrib.auth.decorators import login_required

def authors(request):
    author=Profile.objects.all()
    a_pms={'author':author}
    return render(request, "author.html" , a_pms)

def loginuser(request):
    page= login
    if request.user.is_authenticated:
        return redirect("Home")

    if request.method == 'POST':
        username = request.POST['username'] 
        password =request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "username does not exist")

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            messages.error(request,"User not found")

    return render(request, 'newsignin.html')



def logoutuser(request):
    logout(request)
    return redirect('login')


#view for signin page




def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.email = form.cleaned_data.get('email')
            user.profile.Name = form.cleaned_data.get('Name')

            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('edit_profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def profile(request):
    # profile=Profile.objects.all()
    blog=Blog.objects.all()
    profile=request.user.profile
    context={ 'profile': profile, 'blog': blog}
    return render(request, 'profile.html',context)

@login_required(login_url="login")
def edit_profile(request):
    profile=request.user.profile

    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form=ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
        return redirect('profile')


    context ={'form': form}
    return render(request, 'edit_profile.html',context)