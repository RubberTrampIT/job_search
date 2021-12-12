from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    #return HttpResponse("Hello, mars")
    import requests
    response = requests.get('https://www.google.com/search?q=100%25+remote+information+security+jobs+-clearance+-calls')
    return HttpResponse(response.text)
