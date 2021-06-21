from django.urls import path, include
from books.views import *
from django.views.decorators.cache import cache_page
urlpatterns = [
    path('', index, name='index'),
    path('books/register/', RegisterUser.as_view(), name='register'),
    path('books/login/', LoginUser.as_view(), name='login'),
    path('books/logout/', logout_user, name='logout'),
    path('books/addbook/', cache_page(80) (BookCreateView.as_view()), name='book-create-view'),
    path('books/listbook/', BookListView.as_view(), name='book-list-view'),
    path('books/alllistbook/', AllBookListView.as_view(), name='all-book-list-view'),
    path('books/detailbook/<slug:book_slug>/', BookDetailView.as_view(), name='book-detail-view'),
    path('books/detailallbook/<slug:book_for_slug>/', BookAllDetailView.as_view(), name ='book-all-detail-view'),
    path('books/detailgenre/<slug:genre_slug>/', GenreDetailView.as_view(), name='genre-detail-view'),
    path('books/logged_user/', standart_view, name='standart-view'),
    path('books/email_to_echange/<slug:book_in_slug>/', EmailToExchangeView.as_view(), name='email-to-exchange'),
    path('books/likedlistbook/', BookLikedListView.as_view(), name= 'book-liked-list-view' ),
    path('books/likedmelistbook/', BookMyLikedListView.as_view(), name='book-liked-me-view'),
    path('books/userprofileview/<int:user_profile>/', UserProfileView.as_view(), name= 'user-profile-view'),
    path('books/upadate_book/<slug:book_to_slug>/', BookUpdateView.as_view(), name='book-updateview'),
    path('books/email_to_enchange/<slug:book_upper_slug>/', EmailToExchangeAnswerView.as_view(), name = 'email-to-exchange-answer'),
    path('example/', example, name='example'),
    path('javascript/', javascript, name='javascript')
]
