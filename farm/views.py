from django.shortcuts import render



def home(request):
    return render(request, "home.html")

def features(request):
    return render(request, "features.html")