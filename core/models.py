from django.db import models

class Author(models.Model):
    name = models.CharField('Имя', max_length=128)

class Book(models.Model):
    author = models.ForeignKey('core.Author', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField('Название', max_length=128)
    pages = models.IntegerField('Количество страниц', blank=True, null=True)

    def __str__(self):
        return self.name