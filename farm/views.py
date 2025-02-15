from django.shortcuts import render,redirect
from .models import Farmer,Consumer
from django.contrib.auth.decorators import login_required
from rest_framework import generics,permissions
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError, transaction



@login_required(login_url='farmer_login')
def home(request):
    farmer = None
    consumer = None

    if request.user.is_authenticated:
        # Check if user is Farmer
        farmer = Farmer.objects.filter(user=request.user).first()

        # Check if user is Consumer (only if farmer is not found)
        if not farmer:
            consumer = Consumer.objects.filter(user=request.user).first()

    return render(
        request,
        'home.html',
        {'farmer': farmer, 'consumer': consumer},
    )


@login_required(login_url='login')
def features(request):
    return render(request, "features.html")

@login_required(login_url='login')
def farmer_dashboard(request):
    return render(request, 'farmer_dashboard.html')




####################  FARMER FIELD  #########################
def farmer_register(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('farmer_register')

        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        email = request.POST.get('email', '')
        full_name = request.POST['full_name']
        mobile_number = request.POST['mobile_number']
        # ✅ Check if Mobile Number Already Exists
        if Farmer.objects.filter(mobile_number=mobile_number).exists():
            messages.error(request, 'Mobile number already exists!')
            return redirect('farmer_register')

        aadhaar_number = request.POST['aadhaar_number']
        # Aadhaar Validation: 12 Digits Numeric Check
        if Farmer.objects.filter(aadhaar_number=aadhaar_number).exists():
            messages.error(request, 'Aadhaar Number already exists. Please use a different Aadhaar Number.')
            return render(request, 'farmer_register.html')
        
        elif len(aadhaar_number) != 12 or not aadhaar_number.isdigit():
            messages.error(request, "Invalid Aadhaar Number. It should be 12 digits.")
            return render(request, 'farmer_register.html')
        
        date_of_birth = request.POST['date_of_birth']
        gender = request.POST.get('gender', '') 

        if password == confirmpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email is already exists')
                return redirect('farmer_register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username is alredy exists')
                return redirect('farmer_register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                farmer = Farmer.objects.create(
                user=user,
                full_name=full_name,
                mobile_number=mobile_number,
                aadhaar_number=aadhaar_number,
                date_of_birth=date_of_birth,
                gender=gender


                )
                farmer.save()
                user.save()
                return redirect('farmer_login')
        else:
            messages.info(request, 'password doent match')
            return render(request, 'farmer_register.html')
    else:
        return render(request, "farmer_register.html")
    



def farmer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'username is not exists or password is incorrect')
            return redirect('farmer_login')
        
    else:
        return render(request, 'farmer_login.html')
    




def farmer_logout(request):
    logout(request)
    return redirect('farmer_login')





