# Generated by Django 4.0.3 on 2022-03-21 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_book_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['pages'], 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
    ]
