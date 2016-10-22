from django.shortcuts import render

# Create your views here.


def signin_view(request):
    # more code here to to respond to actions taken by user
    return render(request, 'sigin.html')


def signup_view(request):
    # more code here to to respond to actions taken by user
    return render(request, 'signup.html')


def recipe_view(request):
    # more code here to to respond to actions taken by user
    return render(request, '')