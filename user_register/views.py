from rest_framework.views import APIView, Request
from django.shortcuts import render
from .models import User

def home(request):
    return render(request, 'index.html')

class UserView(APIView):

    def post(self, request: Request):
        new_user = User()
        new_user.username = request.data.get('username')
        new_user.password = request.data.get('password')
        new_user.save()

        return render(request, 'index.html')

    def get(self, request: Request):
        all_users = {
            'users': User.objects.all()
        }

        return render(request, 'users.html', all_users)