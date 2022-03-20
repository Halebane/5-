from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def hello(request):
    return render(request, 'core/hello.html', {'name': 'Vasya'})
