from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http.response import JsonResponse


# Create your views here.
def home(request):
    conv=[
        'India', 'Australia','UAE','USA','UK'
    ]
    return JsonResponse({'response':conv })
