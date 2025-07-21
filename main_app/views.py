from django.shortcuts import render
# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

# about view
def about(request):
    # Send a simple HTML response
    return HttpResponse('<h1>About the Cat Collector App ᓚᘏᗢ</h1>')