from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import SignUpForm

def signup(request) :
    if request.method == 'POST':
        username = request.POST.get('username')
        class_num = request.POST.get('class_num')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        user = User()
        user.username = username
        user.set_password(password)
        user.save()
        return render(request, 'accounts/signup_complete.html')

    else:
        context_values = {'form':'this is form'}
        return render(request, 'accounts/signup.html', context_values)