from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.base import View

from books.forms import *
from books.utils import DataMixin
from django.core.mail import send_mail


def index(request):
    return render(request, 'base.html')

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'books/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('standart-view')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'books/login.html'

    def get_success_url(self):
        return reverse_lazy('standart-view')

def logout_user(request):
    logout(request)
    return redirect('index')

class BookCreateView(CreateView):
    form_class = BookAddForm
    template_name = 'books/book_create.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        print("HERE")
        if form.is_valid():
            print('provirkarka')
            book = form.save(commit=False)
            book.user = request.user
            print(request.user.id)
            book.save()
            return redirect('book-list-view')
        return render(request, self.template_name, {'form': form})

class BookListView(ListView):
    model = Book

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

class AllBookListView(DataMixin, ListView):
    model = Book
    paginate_by = 2
    template_name = 'books/allbook_list.html'

    def get_queryset(self):
        return Book.objects.exclude(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        my_context = self.get_user_context()
        context = dict(list(context.items()) + list(my_context.items()))
        return context

class BookDetailView(DetailView):
    model = Book
    slug_url_kwarg = 'book_slug'

class BookAllDetailView(DetailView):
    model = Book
    slug_url_kwarg = 'book_for_slug'
    template_name = 'books/book_all_detail.html'

class GenreDetailView(DetailView):
    model = Genre
    slug_url_kwarg = 'genre_slug'
    template_name = 'books/genre_detail.html'

def standart_view(request):
    return render(request, 'books/greeting_logged_user.html')

class EmailToExchangeView(View):
    def get(self, request, book_in_slug):
        book_q_set = Book.objects.filter(slug=book_in_slug)
        subject = book_q_set[0].name
        form = EMailToExchangeForm(initial={'subject':subject})
        return render(request, 'books/email_to_exchange.html', {'form': form})

    def post(self, request, book_in_slug):
        form = EMailToExchangeForm(request.POST)
        book_q_set = Book.objects.filter(slug=book_in_slug)
        book_only = book_q_set[0]
        user_book = book_q_set[0].user
        if form.is_valid():
            user_book.email_user(form.cleaned_data['subject'], form.cleaned_data['body'], from_email=form.cleaned_data['from_email_user'], fail_silently = True)
            book_only.is_interested = True
            book_only.save()
            print(book_only.is_interested)
            book_only.user_interested.add(request.user)
            return redirect('standart-view')

class BookLikedListView(ListView):
    model = Book
    template_name = 'books/booklikedlistview.html'

    def get_queryset(self):
        return Book.objects.filter(user= self.request.user).filter(is_interested=True)

class BookMyLikedListView(ListView):
    model = Book
    template_name = 'books/bookmylikedlistview.html'

    def get_queryset(self):
        return Book.objects.filter(user_interested=self.request.user)

class UserProfileView(View):
    def get(self,request, user_profile):
        user_profile = User.objects.get(id=user_profile)
        return render(request, 'books/user_profile_view.html', {'user_profile':user_profile})

class BookUpdateView(UpdateView):
    model =Book
    form_class = BookUpdateForm
    slug_url_kwarg = 'book_to_slug'
    template_name = 'books/book_updateview.html'
    success_url = reverse_lazy( 'book-list-view')

class EmailToExchangeAnswerView( View):
    def get(self, request, book_upper_slug):
        book_q_set = Book.objects.filter(slug=book_upper_slug)
        book_choose_name = book_q_set[0].name
        query_interested_books =Book.objects.filter(user=request.user).filter(is_interested=True).filter(is_exchanged=False)
        str_names = ''.join([book_.name for book_ in query_interested_books])
        form = EMailToExchangeAnswerForm(initial={'book_choose_name':book_choose_name, 'book_from_user_name': str_names})
        return render(request, 'books/email_to_exchange_answer.html', {'form': form})

    def post(self, request, book_upper_slug):
        form =EMailToExchangeAnswerForm(request.POST)
        book_q_set = Book.objects.filter(slug=book_upper_slug)
        book_only = book_q_set[0]
        user_book = book_q_set[0].user
        print(user_book)
        if form.is_valid():
            body_message = str(form.cleaned_data['book_from_user_name'] + form.cleaned_data['post_address'] + form.cleaned_data['greeting'] + str( form.cleaned_data['telephon_number']))
            user_book.email_user(subject=form.cleaned_data['book_choose_name'],message=body_message, from_email=form.cleaned_data['from_email_user'], fail_silently = True)
            book_only.is_exchanged = True
            book_only.save()
            book_now_user = Book.objects.get(name=form.cleaned_data['book_from_user_name'][0])
            book_now_user.is_exchanged = True
            book_now_user.save()
            print(book_now_user.is_exchanged)
            print(book_only.is_exchanged)
            # book_only.user_interested.exclude(request.user)
            return redirect('standart-view')

def example(request):
    all_book = Book.objects.all()
    return  render(request, 'books/examples.html', {'all_book':all_book})

def page_bot_found(request, *args, **argv):
    return  render(request, 'books/handlers/handler404.html')

def server_error(request, *args, **argv):
    return  render(request, 'books/handlers/handler500.html')

def page_transfer_temperory_on_another_url(request, *args, **argv):
    return  render(request, 'books/handlers/handler302.html')

def javascript(request):
    return render(request, 'books/javascript.html')






