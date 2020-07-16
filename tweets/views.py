from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_views(request, tweet_id):
    return HttpResponse(f"<h1> Hello {tweet_id} </h1>")
