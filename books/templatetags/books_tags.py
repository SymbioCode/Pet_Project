from django import template
from books.models import Genre, Book


register = template.Library()
@register.simple_tag()
def get_genres():
    return Genre.objects.all()


@register.inclusion_tag('books/three_first_books.html')
def show_three_first_books():
    books = Book.objects.filter(id__lte=3)
    return {'books':books}
