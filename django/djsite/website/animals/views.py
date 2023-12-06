from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def index(request): 
    return HttpResponse("<h1>əsas səhifə</h1>")

def about(request): 
    return HttpResponse("<h1>səhifə haqqında</h1>")

def contact(request): 
    return HttpResponse("<h1>əlaqə</h1>")

def pageNotFound(request, exception): 
    return HttpResponseNotFound("<h1> Səhifə tapılmadı </h1> <p>Əsas səhifəyə qayıtmağa çalışın.<p/>")
