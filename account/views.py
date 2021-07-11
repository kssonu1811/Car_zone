from myapp.views import contact
import account
from django.contrib.messages.api import error
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from contacts.models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            messages.success(request,'you are now logged in.')
            return redirect("account:dashboard")
        else:
            messages.error(request,'Invalid login details')
            return redirect("account:login")
    return render(request,'accounts/login.html')

def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:

            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exist')
                return redirect('account:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Registration Failed - Try different email address')
                    return redirect('account:register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
                    auth.login(request,user, backend='django.contrib.auth.backends.ModelBackend')
                    # auth.login(request,user)
                    messages.success(request,'you are now logged in.')
                    return redirect('account:dashboard')
        else:
            messages.error(request, 'password dose not match')
            return redirect('account:register')
    else:
        return render(request,'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')


@login_required(login_url = 'account:login')
def dashboard(request):
    User_inquiry = Contact.objects.order_by('created_date').filter(user_id=request.user.id)
    data ={
        'inquiries' : User_inquiry
    }
    return render(request,'accounts/dashboard.html', data)
