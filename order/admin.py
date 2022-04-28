from django.contrib import admin
from stripe import OrderReturn

# Register your models here.

from .models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)