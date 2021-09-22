from django.shortcuts import render, HttpResponse


# Create your views here.
def contact(request):
    return HttpResponse('<h1>Test Successful</h1>')
