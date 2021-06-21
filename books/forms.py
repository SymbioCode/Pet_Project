from django.core.exceptions import ValidationError

from books.models import *
from django import forms
from captcha.fields import CaptchaField

class BookAddForm(forms.ModelForm):
    captcha = CaptchaField(label='Введіть наведені символи')
    class Meta:
        model = Book
        exclude = ('user','is_interested','user_interested','is_exchanged')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['genre'].empty_label = 'Категорія не вибрана'

    def clean_pages_of_book(self):
        pages_of_book = self.cleaned_data['pages_of_book']
        if len(pages_of_book) <= 0:
            raise ValidationError('Книга не може мати таку малу кількість сторінок')


class EMailToExchangeForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Назва книги')
    body = forms.CharField(label='Ваші побажання', widget=forms.TextInput(attrs={'class':'special', 'size': '40'}))
    from_email_user = forms.EmailField(label='Ваш актуальний email-адрес')

    def clean_body(self):
        body = self.cleaned_data['body']
        if len(body) < 10:
            raise ValidationError('Для заохочення ведіть більше слів')

class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('user','is_interested','user_interested', 'is_exchanged')



class EMailToExchangeAnswerForm(forms.Form):

    book_choose_name = forms.CharField(max_length=100, label='Назва книги Вашого вибору')
    book_from_user_name = forms.CharField( label='Назва книги вибору користувача')
    post_address = forms.CharField(max_length=120, label='Поштові дані')
    telephon_number = forms.IntegerField(label='Контактний телефон')
    greeting = forms.CharField(label='Ваші побажання')
    from_email_user = forms.EmailField(label='Ваш актуальний email-адрес')

