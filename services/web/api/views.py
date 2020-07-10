import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from main.settings import DEBUG
from django.db.models import Count

from .models import Calls, Conversations

if DEBUG:
    CLIENT_ID = os.environ.get('CLIENT_ID', 8)

# Create your views here.
def pong(request):
    """
    Checking uptime of webapp
    """
    return HttpResponse("pong")

def get_count_of_calls(request):
    """
    Get count of calls for CLIENT_ID = 8 during development.
    Get all calls when deployed in Prod. To be used for client-specific deployments.
    TODO: Add a dropdown for CLIENT_ID
    """
    calls = Calls.objects.filter(client_id=CLIENT_ID).count()

    return JsonResponse({'Calls': calls})


def get_predicted_intent_distribution(request):
    """
    Get call distribution for predicted_intent
    """
    predicted_intent_distribution = (Conversations.objects
                                        .filter(call__client_id=CLIENT_ID)
                                        .values('metadata__predicted_intent')
                                        .annotate(Count('call_id', distinct=True)))
    print(predicted_intent_distribution)

    return JsonResponse({'predicted_intent': "Predicted intent distribution"})