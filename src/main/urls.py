from django.urls import path
from .views import(MainPokerBotApiView)

urlpatterns = [
    path('api', MainPokerBotApiView.as_view()),
]