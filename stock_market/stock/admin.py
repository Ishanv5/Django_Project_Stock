from django.contrib import admin
from .models import *

class Buy_SellAdmin(admin.ModelAdmin):
    list_display=("stock_symbol","stock_price","number_of_shares")
    
class SellAdmin(admin.ModelAdmin):
    list_display=("stock_symbol","number_of_shares")
# Register your models here.


admin.site.register(Profile)
admin.site.register(Buy_Sell,Buy_SellAdmin)
admin.site.register(Sell,SellAdmin)

