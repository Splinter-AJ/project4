from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['username4']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def reg(request):
    if request.method =='POST':
        username=request.POST['username']
        first_name=request.POST['username1']
        last_name=request.POST['username2']
        email=request.POST['username3']
        password = request.POST['username4']
        cpassword = request.POST['username5']

        if password==cpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"username taken")
                    return redirect('reg')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,"email already exists")
                    return redirect('reg')
                else:
                    user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                    user.save();
                    return  redirect('login')


        else:
             messages.info(request,"password not matched")
             return redirect('reg')

        return  redirect('/')

    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')


