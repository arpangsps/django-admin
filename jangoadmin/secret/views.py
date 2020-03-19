from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import auth
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from secret.models import user_details, user_details_2
from .forms import ContactForm
from secret.serializers import userSerializer


@login_required
def Dashboard(request):
    return render(request, 'secret/index.html',{"user":request.user})

def Login(request):
    msg = ""
    if(request.method=="POST"):
        user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            if user.is_superuser:
                auth.login(request, user)
                return redirect("/secret/")
            else:
                msg = "Login from Mobile App!"
        else:
            msg = "Incorrect Password!"
    print(msg)
    return render(request, 'secret/login.html',{"msg":msg})

def Register(request):
    return render(request, 'secret/register.html')

def ForgotPassword(request):
    return render(request, 'secret/forgot-password.html')

@login_required
def Settings(request):
    return render(request, 'secret/settings.html',
    {"msg":request.GET.get('q'),"err":request.GET.get('e')})

@login_required
def Profile(request):
    msg = ""
    if request.method=="POST":
        u = request.user
        u.first_name = request.POST.get('first_name')
        u.last_name  = request.POST.get('last_name')
        u.email      = request.POST.get('email')
        u.save()
        msg="Information Updated!"
    return redirect("/secret/settings/?q="+msg)

@login_required
def ChangePassword(request):
    msg = ""
    err = ""
    if request.method=="POST":
        u     = request.user
        opwd  = request.POST.get('opwd')
        npwd  = request.POST.get('npwd')
        cnpwd = request.POST.get('cnpwd')
        if u.check_password(opwd) == True:
            if npwd == cnpwd:
                u.set_password(npwd)
                msg="Password Updated!"
            else:
                err="New password(s) didn't match!"
        else:
            err="Incorrect Password!"
        u.save()
    return redirect("/secret/settings/?q="+msg+"&e="+err)

@login_required
def SampleListing(request):
    return render(request, 'secret/tables.html')


#Users
@login_required
def Users(request):
    user_obj = User.objects.values('id', 'first_name', 'last_name', 'username', 'email')
    details_obj = user_details.objects.values('id', 'phone_number', 'role', 'user_id')
    return render(request, 'users/users.html', {'user_obj': user_obj, 'details_obj':details_obj })


@login_required
def SampleReports(request):
    return render(request, 'secret/charts.html')

def NotFound(request):
    return render(request, 'secret/404.html')

@login_required
def Logout(request):
    auth.logout(request)
    return redirect('/secret/login/')


# Add user
def Add(request):
    form = ContactForm()
    return render(request, 'users/addUsers.html', {'form': form})
    print(user_detailsSerializer())


#Delete user
def deletepc(request, id):
    user_obj = User.objects.values('id', 'first_name', 'last_name', 'username', 'email')
    User.objects.filter(id = id).delete()
    return redirect('/secret/users')


#Edit user 
def Edit(request, id):
    print('Hello mofo')


#Submit form
def Submit(request):
    serializer = userSerializer(data=request.POST)
    user_obj = User.objects.values('id', 'first_name', 'last_name', 'username', 'email')
    obj = instance.save() 
    print(obj.id) 
    # details_obj = user_details.objects.values('id', 'user_id', 'phone_number', 'role')
    # print(request.POST.get('id'))
    # print(request.POST.get('role'))
    print(serializer.is_valid())
    print(serializer.errors)
    serializer.save() 
    return redirect('/secret/users')
    