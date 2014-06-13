# Create your views here.
from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from game.models import Game, Profile

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return render(request, 'base.html')
    else:
        # Show an error page
        return render(request, 'registration/login.html')
    # if request.method == 'POST':
    #     return HttpResponse("Do something")
    # else:
    #     return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return render(request, "registration/logged_out.html")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
             
            profile = Profile.objects.create(user=new_user)
            profile.save()
            creator = Game.objects.create(created_by_id = profile.id)
            creator.save()
            return HttpResponseRedirect("/register_success/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })

def register_success(request): #new user registered successfully
    user = auth.get_user(request)
    if user.is_authenticated(): #user already logged in

        return HttpResponseRedirect('')

    else:

        return render_to_response('registration/register_success.html')    