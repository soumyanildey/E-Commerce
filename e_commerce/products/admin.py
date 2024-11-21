from django.contrib import admin
from .models import Seller,Products,Category
# Register your models here.
admin.site.register(Seller)
admin.site.register(Products)
admin.site.register(Category)