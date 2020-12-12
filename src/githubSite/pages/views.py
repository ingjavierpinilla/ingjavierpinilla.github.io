from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text": "this is about us",
        "my_number": 14        
    }
    return render(request, "contact.html", my_context)    