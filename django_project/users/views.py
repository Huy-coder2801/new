from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import RegisterStaffForm


# To register a Staff
def register_staff(request):
    if request.method == 'POST':
        form = RegisterStaffForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_staff = True
            var.save()
            messages.info(request, 'Account Created Successfully. Please login to continue.')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong. Please check your form input.')
    else:
        form = RegisterStaffForm()
    
    context = {'form': form}
    return render(request, 'users/register_staff.html', context)


#Login a User

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.info(request, 'Login Successfully. Please enjoy your session')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something Went Wrong. Please Check your form input')
            return redirect('login')
    else:
        return render(request, 'users/login.html')
    
#logout a user

def logout_user(request):
    logout(request)
    messages.info(request, 'Logout Successfully, your session has ended.')
    return redirect('login')