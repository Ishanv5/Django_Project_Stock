from .send_sms import sendsms
import random

import http.client
import requests
from stock.models import Profile
from stock.models import Buy_Sell
from stock.models import Sell
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/login.html')
        
        
        profile_obj = Profile.objects.filter(user = user_obj ).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/login.html')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/login.html')
        
        login(request)
        return redirect('/dash.html')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/signup.html')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/signup.html')
            
            user_obj = User(username = username , email = email,password = password)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('/token_send.html')

        except Exception as e:
            print(e)
    return render(request, 'signup.html')

def support(request):
    
    return render(request, 'support.html')

def about(request):
    
    return render(request, 'about.html')

def success(request):
    return render(request , 'success.html')


def token_send(request):
    return render(request , 'token_send.html')




def error_page(request):
    return  render(request , 'error.html')

def portal(request):
    response=requests.get(" https://api.stockdata.org/v1/data/quote?symbols=AAPL,TSLA,MSFT&api_token=YOUR_API_TOKEN").json()
    return  render(request , 'portal.html' ,{"response": response})

def account(request):
    data=Buy_Sell.objects.all()
    print(data)
    return  render(request , 'account.html',{"message": data})


def sell_stock(request):
    if request.method == 'POST':
        stock_symbol = request.POST.get('stock_symbol')
        number_of_shares = request.POST.get('number_of_shares')
        d1=Sell(stock_symbol=stock_symbol,number_of_shares=number_of_shares)
        d1.save()
        return  render(request , 'trade.html')
    return  render(request , 'trade.html')


def save_stock(request):
    if request.method == 'POST':
        stock_symbol = request.POST.get('stock_symbol')
        stock_price = request.POST.get('stock_price')
        number_of_shares = request.POST.get('number_of_shares')
        
        d=Buy_Sell(stock_symbol=stock_symbol,stock_price=stock_price,number_of_shares=number_of_shares)
        
        d.save()
        sendsms()
        return render(request, 'buy_sell.html')
    return  render(request , 'buy_sell.html')
        
def buy_sell(request):
    
        
    return  render(request , 'buy_sell.html')

@login_required
def dash(request):
    return  render(request , 'dash.html')


def payment(request):
    return  render(request , 'payment.html')


def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/login.html')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/login.html')
        else:
            return redirect('/error.html')
    except Exception as e:
        print(e)
        return redirect('/')
    
    
def send_mail_after_registration( email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )









