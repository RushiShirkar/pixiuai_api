from django.urls import path
from .views import IdeaCreate, IdeaView

urlpatterns = [
    path('create', IdeaCreate.as_view()),
    path('view', IdeaView.as_view())
]