from django.shortcuts import render
from profile_page.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url="{% url 'landing_page:login' %}")
def show_profile(request):
    user_loggedin = False

    if request.user.is_authenticated:
        user_loggedin = True
    context = {
        'username' : request.user.username, 
        'user_loggedin': user_loggedin
    }

    return render(request, "profile.html", context)

@login_required(login_url="{% url 'landing_page:login' %}")
def edit_profile(request):
    user_profile = Profile.objects.get(user = request.user)
    user_loggedin = False

    if request.user.is_authenticated:
        user_loggedin = True

    context = {
        'profile' : user_profile,
        'user_loggedin' : user_loggedin
    }
    return render(request, "modify.html", context)