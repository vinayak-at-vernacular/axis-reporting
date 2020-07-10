from django.urls import path, include
from .views import *

urlpatterns = [
    path('', get_count_of_calls),
    path('ping/', pong),
    path('predict/', get_predicted_intent_distribution)
]