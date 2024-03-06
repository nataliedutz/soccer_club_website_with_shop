from django.contrib import admin
from .models import Profile
from shop.models import Order  

class OrderInline(admin.TabularInline):
    model = Order

class ProfileAdmin(admin.ModelAdmin):
    inlines = [OrderInline]

admin.site.register(Profile, ProfileAdmin)
