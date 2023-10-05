from django.shortcuts import render
from django.http import HttpResponse
def display(request):
    s='<h1>my name is kalyan kumar</h1>'
    return HttpResponse(s)
