from django import forms

import core


class BookSearch(forms.Form):
    name = forms.CharField(label='Название', required=False)
    min_pages = forms.IntegerField(label='Количество страниц', required=False,
                                   help_text='Минимальное количество страниц')

    def clean_min_pages(self):
        cleaned_data = self.cleaned_data
        min_pages = cleaned_data.get('min_pages')
        if min_pages and min_pages > 1000:
            raise forms.ValidationError('Количество страниц не должно быть больше 1000')

        return cleaned_data

class BookEdit(forms.ModelForm):
    class Meta:
        model = core.models.Book
        fields = '__all__'
