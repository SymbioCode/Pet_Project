from books.models import *

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        genres = Genre.objects.all()
        context['genres'] = genres
        users = User.objects.all()
        context['users_'] = users
        return context

