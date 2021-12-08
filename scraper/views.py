from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    #return HttpResponse("Hello, mars")
    import requests
    response = requests.get("https://oxylabs.io/”)
    return HttpResponse(response.text)
