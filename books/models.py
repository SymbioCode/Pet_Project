from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Жанр')
    description = models.TextField(verbose_name='Опис')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre-detail-view', kwargs={'genre_slug': self.slug})

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанри'

class Book(models.Model):
    name = models.CharField(max_length=120, verbose_name='Назва')
    name_of_author = models.CharField(max_length=100, verbose_name='ПІБ автора')
    number_of_edition = models.SmallIntegerField(default=1, verbose_name='Номер видання')
    year_of_edition = models.PositiveIntegerField(verbose_name='Рік видання')
    description = models.TextField(verbose_name='Опис')
    count_of_pages = models.IntegerField(blank=True, null=True, verbose_name='Кількість сторінок')
    book_cover = models.ImageField(upload_to='books_cover/%d/%m/%Y')
    pages_of_book = models.ImageField(upload_to='pages_of_book/%d/%m/%Y')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Власник', related_name='book_set_up')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Жанр')
    is_interested = models.BooleanField(default=False, verbose_name='Є вподобана')
    user_interested = models.ManyToManyField(User, blank=True, null=True, verbose_name='Зацікавлений користувач' )
    is_allowed_to_exchange = models.BooleanField(default=True, verbose_name='Дозволити для обміну')
    is_exchanged = models.BooleanField(default=False, verbose_name='Була обміняна')
    time_create = models.DateField(auto_now_add=True, verbose_name='Дата внесення книги', blank=True, null=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book-detail-view', kwargs={'book_slug': self.slug})

    def get_new_url(self):
        return reverse('book-all-detail-view', kwargs={'book_for_slug': self.slug})

    def get_newest_url(self):
        return reverse('email-to-exchange', kwargs={'book_in_slug': self.slug})

    def get_for_put(self):
        return reverse('book-updateview', kwargs={'book_to_slug': self.slug})

    def get_for_end(self):
        return reverse('book-updateview', kwargs={'book_to_slug': self.slug})
    def get_upper_end(self,):
        return reverse('email-to-exchange-answer', kwargs={'book_upper_slug': self.slug})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

class Review(models.Model):
    name_of_user = models.CharField(max_length=60, verbose_name='ПІБ користувача')
    text = models.TextField(verbose_name='Вміст відгуку')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'



