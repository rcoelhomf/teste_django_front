from django.shortcuts import render
from .models import User

def home(request):
    return render(request, 'index.html')

def usersView(request):
    new_user = User()
    new_user.username = request.POST.get('name')
    new_user.password = request.POST.get('password')
    new_user.save()

    return render(request, 'index.html')

def listUserView(request):
    all_users = {
        'users': User.objects.all()
    }

    return render(request, 'users.html', all_users)