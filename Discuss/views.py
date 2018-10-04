from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, Add_Post
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from .models import Posts

User = get_user_model()

# 'Discuss' landing page
def discuss(request):
    context = {}
    posts = Posts.objects.all()
    context["posts"] = posts
    return render(request,'Discuss/discuss.html',context)

@login_required(login_url='/login')
def add_post(request):
    form = Add_Post(request.POST)
    context = {'form':form,}
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.username
            post.save()
            return redirect('/discuss')
    else:
        context['form'] = Add_Post()
    context["user"] = request.user.username
    return render(request,'Discuss/add_post.html',context)

def register_user(request):
    form=RegisterForm(request.POST or None)
    context={
        'form':form,
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        new_user=User.objects.create_user(username=username,email=None,password=password)
        new_user.save()
        return redirect("/login")
    return render(request,'Discuss/register.html',context)

def login_user(request):
    form=LoginForm(request.POST or None)
    context={
        'form':form,
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/discuss")
        else:
            context['form']=LoginForm()
            context['error']="Invalid credentials."
    return render(request,'Discuss/login.html',context)