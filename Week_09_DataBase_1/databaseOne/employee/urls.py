from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
    path('add_works/', views.add_works, name='add_works'),
    path('search_company/', views.search_company, name='search_company'),
    path('add_lives/', views.add_lives, name='add_lives'),
    
]
