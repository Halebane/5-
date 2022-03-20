from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
import core.models


def index(request):
    books = core.models.Book.objects.all()
    return render(request, 'core/index.html', {'books': books})
