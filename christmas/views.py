from django.shortcuts import render, HttpResponse


# Create your views here.
def generic(request):
    return HttpResponse("Hello")