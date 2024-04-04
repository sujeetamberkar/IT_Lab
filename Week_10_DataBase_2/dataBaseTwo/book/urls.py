from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('add/', views.add_book, name='add_book'),
    path('', views.book_list, name='book_list'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_publisher/', views.add_publisher, name='add_publisher'),
]
