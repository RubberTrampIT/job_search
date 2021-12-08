from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import requests
response = requests.get("https://oxylabs.io/”)
print(response.text)
