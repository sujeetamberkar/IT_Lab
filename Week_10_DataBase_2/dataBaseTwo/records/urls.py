from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
    path('', views.human_list_update, name='human_list_update'),
    path('add/', views.add_human, name='add_human'),

]
