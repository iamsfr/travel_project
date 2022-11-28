from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Login failed')
            return redirect('login')
    return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        first = request.POST['first_name']
        last = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first, last_name=last, email=email, username=username, password=password)
            user.save()
            return redirect('login')
            print('created user')
        else:
            messages.info(request,"password mismatch")
            return redirect('register')
        return redirect('/')
        
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')