from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def balaya(request):
    return HttpResponse('<h1>jai balaya</h1>')