import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Subscription


@method_decorator(csrf_exempt, name="dispatch")
class HomeView(View):
    def get(self, request):
        return render(
            request,
            "base.html",
        )

    def post(self, request):
        data = json.loads(request.body)
        add_user = Subscription(
            customer_name=data["customername"],
            email=data["email"],
            subscription_type=data["subscriptiontype"],
        )
        add_user.save()
        return JsonResponse({"data": "response"}, status=201)


class SubscriptionList(View):
    def get(self, request):
        all_subscriptions = Subscription.objects.all()
        return render(
            request, "table.html", context={"all_subscriptions": all_subscriptions}
        )
