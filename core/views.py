from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

import core.models
import core.forms
import core.filters


class TitleMixin:
    title: str = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = self.get_title()
        return context


class IndexView(TitleMixin, TemplateView):
    template_name = 'core/index.html'
    title = "Главная страница"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['info'] = self.get_info()
        return context

    def get_info(self):
        return 'Главная страница'


# def index(request):
# return render(request, 'core/index.html')

class Books(TitleMixin, ListView):
    title = 'Книги'

    def get_filters(self):
        return core.filters.BookFilter(self.request.GET)

    def get_queryset(self):
        # name = self.request.GET.get('name')
        # queryset = core.models.Book.objects.all()
        # if name:
        #     queryset = queryset.filter(name__icontains=name)
        return self.get_filters().qs

    def get_context_data(self):
        context = super().get_context_data()
        # context['form'] = core.forms.BookSearch(self.request.GET or None)
        context['filters'] = self.get_filters()
        return context


# def book_list(request):
#    name = request.GET.get('name')
#    books = core.models.Book.objects.all()
#    if name:
#        books = books.filter(name__icontains=name)
#    return render(request, 'core/book_list.html', {'books': books})

class BookDetail(TitleMixin, DetailView):
    queryset = core.models.Book.objects.all()

    def get_title(self):
        return str(self.get_object())


# def book_detail(request, pk):
#    return HttpResponseNotFound('Не найдено')
#    book= core.models.Book.objects.get(pk=pk)
#    return render(request, 'core/book_detail.html', {'book': book})

def admin(request):
    return render(request, 'core/index.html')
