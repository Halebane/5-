from django.http import HttpResponseNotFound
from django.shortcuts import render
import core.models

def index(request):
    books= core.models.Book.objects.all()
    return render(request, 'core/index.html', {'books': books})

def book_list(request):
    books= core.models.Book.objects.all()
    return render(request, 'core/book_list.html', {'books': books})

def book_detail(request, pk):
    return HttpResponseNotFound('Не найдено')
    book= core.models.Book.objects.get(pk=pk)
    return render(request, 'core/book_detail.html', {'book': book})

def admin(request):
    return render(request, 'core/index.html')