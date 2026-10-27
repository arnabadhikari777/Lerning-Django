from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse ("hello home")
    return render(request, 'index.html')
    
def about(request): # type: ignore
    return render(request, 'about.html')
    #return HttpResponse ("hello about")

    
def arnab(request): # type: ignore
    return HttpResponse ("hello Arnab")