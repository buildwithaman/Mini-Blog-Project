from django.shortcuts import render , HttpResponseRedirect
from .forms import ContactForm , PostForm
from .models import ContactModel , PostModel
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User , Group

# Create your views here.
def base(request):
    return render(request , "blog/base.html")

def home(request):
    posts = PostModel.objects.all()
    return render(request,"blog/home.html",{"posts":posts})

def about(request):
    return render(request,"blog/about.html")

def contact(request):
    if request.method == "POST":
        fm = ContactForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data["name"]
            gmail  = fm.cleaned_data["gmail"]
            message = fm.cleaned_data["message"]
            contactUser = ContactModel(name=name,gmail=gmail,message=message)
            contactUser.save()
            messages.success(request,"Your message has been Successfully Delivered Wait for 1-2 hour for Response Form our Side")
            fm = ContactForm()
    else:
        fm = ContactForm()
    return render(request , "blog/contact.html",{"form":fm})

def signin(request):
    if not request.user.is_authenticated :
        if request.method == "POST":
            fm = AuthenticationForm(request=request , data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data["username"]
                pass1 = fm.cleaned_data["password"]
                author = authenticate(username=uname , password=pass1)
                if author is not None:
                    login(request , author)
                    messages.success(request,"Logged In Successfully")
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = AuthenticationForm()
        return render(request,"blog/signin.html",{"form":fm})
    else:
        return HttpResponseRedirect("/dashboard/")

def signup(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            user = fm.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            messages.success(request,"Account Has been successfully created")
            fm = UserCreationForm()
    else:
        fm = UserCreationForm()
    return render(request,"blog/signup.html",{"form":fm})


def dashboard(request):
    if request.user.is_authenticated :
        posts = PostModel.objects.all()
        full_name = request.user.get_full_name()
        grp = request.user.groups.all()

        return render(request,"blog/dashboard.html",{"posts":posts , "name":full_name , "group":grp})
    else:
        return HttpResponseRedirect("/signin/")



def signout(request):
    logout(request)
    messages.success(request , "You're Successfully logged Out")
    return HttpResponseRedirect('/')

def post(request):
    if request.user.is_authenticated :
        if request.method == "POST":
            posts = PostForm(request.POST)
            if posts.is_valid():
                title = posts.cleaned_data["title"]
                description = posts.cleaned_data["desc"]
                postCheck = PostModel(title=title , desc=description)
                postCheck.save()
                messages.success(request,"Blog Post Updated Successfully!!!....")
                posts = PostForm()
                return HttpResponseRedirect("/dashboard/")
        else:
            posts = PostForm()
        return render(request,"blog/post.html",{"posts":posts})
    else:
        return HttpResponseRedirect("/signin/")
    
def editpost(request , id):
    if request.user.is_authenticated :
        if request.method == "POST":
            pi = PostModel.objects.get(pk=id) 
            post = PostForm(request.POST , instance=pi)
            if post.is_valid():
                post.save()
                messages.success(request,"Blogpost Upadated Successfully")
                return HttpResponseRedirect("/dashboard/")
        else:
            pi = PostModel.objects.get(pk=id)
            post = PostForm(instance=pi)
            
        return render(request,"blog/editpost.html",{"form":post})
    else:
        return HttpResponseRedirect("/signin/")
    
def deletepost(request , id):
    if request.user.is_authenticated :
        if request.method =="POST":
            pi = PostModel.objects.get(pk=id)
            pi.delete()
            messages.success(request,"Blog Post deleted Successfully")
            return HttpResponseRedirect("/dashboard/")
        else:
            return HttpResponseRedirect("/signin/")
    
    

    
    