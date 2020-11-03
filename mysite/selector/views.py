from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def search(request):
    return HttpResponse('<h1> Search for food items </h1>')

def edit(request):
    return HttpResponse('<h1> edit database </h1>')
