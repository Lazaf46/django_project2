from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def gm_view(request):
    return HttpResponse('<h1>Good Morning</h1>')

def ge_view(request):
    return HttpResponse('<h1> Godd Evening </h1>')

def gn_view(request):
    return HttpResponse('<h1>Good Night</h1>')