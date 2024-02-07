from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as authlogin,logout as authlogout,authenticate
from django.contrib import messages
from home.models import todo 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

# Create your views here
# @login_required
def home(request, default=None):
    # return HttpResponse("home")
    if request.user.is_authenticated:
        all_todo = todo.objects.filter(user=request.user)
        context = {
            'todos': all_todo
        }
        return render(request, 'home.html', context)
    else :
        return render(request, 'home.html')

def register(request):
    # return HttpResponse("register")
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        usernames = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(len(password))
        if len(password) < 8:
            messages.error(request,"error,password must be more than 8 characters")
            return redirect('register')
        get_all_user_by_username = User.objects.filter(username=usernames)
        if get_all_user_by_username :
            messages.error(request,"error, username already exist")
            return redirect('register')
        password = make_password(password)
        new_user = User.objects.create(username=usernames, email=email, password=password)
        new_user.save()
        messages.success(request,"User Created , Login Now !!!")
        return redirect('login')

    return render(request, 'register.html',{})

def login(request):
    # return HttpResponse("login")
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        print(username, password)
        user_login = authenticate(username=username , password=password)
        print(user_login)

        if user_login is not None :
            authlogin(request, user_login)
            return redirect('task')
        else:
            user_lo = User.objects.filter(username=username)
            if user_lo :
                messages.error(request,"error,please enter valid password")
                return redirect('login')
            else:
                messages.error(request,"error,please enter valid username")

    return render(request, 'login.html',{})

# @login_required
def task(request):
    if request.method == 'POST':
        print('hello')
        task_name = request.POST.get('Task')
        desc = request.POST.get('Description')
        date = request.POST.get('Date')
        new_todo = todo(user=request.user, todo_name=task_name, description=desc, date=date)
        new_todo.save()

    return render(request, 'task.html')

@login_required
def DeleteTask(request, slug):
    get_todo = todo.objects.get(user=request.user, todo_name=slug)
    get_todo.delete()
    return redirect('home')

@login_required
def Update(request, slug):
    get_todo = todo.objects.get(user=request.user, todo_name=slug)
    get_todo.status = True
    get_todo.save()
    return redirect('home')

def Search(request, slug):
    get_todo = todo.objects.get(user=request.user, todo_name=slug)

@login_required
def logout(request):
    authlogout(request)
    return redirect('login')