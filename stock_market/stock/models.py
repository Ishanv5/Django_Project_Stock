from django.db import models
from django.contrib.auth.models import User
from .models import *


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.user.username
        
    
    
class Buy_Sell(models.Model):
    stock_symbol = models.CharField(max_length=100)
    stock_price = models.BigIntegerField()
    number_of_shares=models.BigIntegerField()
    
class Sell(models.Model):
    stock_symbol = models.CharField(max_length=100)
    number_of_shares=models.BigIntegerField()
    

    

    