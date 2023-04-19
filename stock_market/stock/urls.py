from django.contrib import admin
from django.urls import path
from stock import views

urlpatterns = [
   path("",views.index,name='home'),
   path("login.html",views.login,name='login'),
   path("signup.html",views.signup,name='signup') ,
   path("support.html",views.support,name='support'),
   path("about.html",views.about,name='about'),
   path('token_send.html' , views.token_send , name="token_send"),
   path('success.html' , views.success , name='success'),
   path('verify/<auth_token>' , views.verify , name="verify"),
   path('error.html' , views.error_page , name="error"),
   path('dash.html' , views.dash , name="dash"),
   path('portal.html' , views.portal , name="portal"),
   path('account.html' , views.account , name="account"),
   
   path('save_stock/' , views.save_stock , name="save_stock"),
   path('sell_stock/' , views.sell_stock , name="sell_stock"),
   path('buy_sell.html' , views.buy_sell , name="buy_sell"),
    path('payment.html' , views.payment , name="payment")
    
]