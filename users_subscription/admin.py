from django.contrib import admin
from .models import Subscription

# Register your models here.


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["id", "customer_name", "email", "subscription_type"]
