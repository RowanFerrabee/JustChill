from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.

def testFunction(request):
    return HttpResponse("Hello Android! :D")