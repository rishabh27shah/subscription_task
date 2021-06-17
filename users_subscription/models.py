from django.db import models


class Subscription(models.Model):
    customer_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    subscription_type = models.CharField(max_length=20)
