from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.template import context
from django.contrib.auth.decorators import login_required

# Create your views here.


def registerPage(request):
       
    form = CreateUserForm()

    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for'+ user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'account/register.html', context)

def loginPage(request):

     
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blogosphere/front_page')
        else:
            messages.info(request, 'Username or password is incorrect')
        

    context = {}
    return render(request, 'account/login.html', context) 

def logoutUser(request):
    logout(request)
    return redirect('login')    


def home(request):
    return HttpResponse(request, 'account/login')


def expenses1(request):
    return render(request, 'expenses/expenses1.html')


def add_expense(request):
    return render(request, 'expenses/add_expense.html')
    
    