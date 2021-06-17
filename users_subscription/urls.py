from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="subscription-page"),
    path(
        "subsciption_list/", views.SubscriptionList.as_view(), name="subscription-list"
    ),
]
