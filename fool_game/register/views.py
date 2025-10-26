from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import User

from django.http import HttpResponse


def index(request):

    users = User.objects.all()
    context = {
        "users" : users
    }

    return render(request, "register/index.html", context)


def get_user(request, user_id):
    
    #user = User.objects.get(pk=user_id)
    user = get_object_or_404(User, pk=user_id)
    context = {
        "user" : user
    }

    return render(request, "register/get_user.html", context)
