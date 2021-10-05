from django.urls import path
from .views import SubscriptionCreate, SubscriptionView, SubscriptionDelete

urlpatterns = [
    path('create', SubscriptionCreate.as_view()),
    path('view', SubscriptionView.as_view()),
    path('delete', SubscriptionDelete.as_view())
]