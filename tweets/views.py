from django.shortcuts import render
from django.http import HttpResponse

from .models import Tweet
# Create your views here.

def home_view(request):
   # return HttpResponse("<h1> Hello World </h1>")
    return render(request, "pages/home.html",context={}, status=200)

def tweet_details_view(request, tweet_id):
    #obj = Tweet.objects.get(id = tweet_id)
    return HttpResponse(f"<h1> Hello {tweet_id}</h1>")
