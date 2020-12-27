from django.conf.urls import url
from app1 import views

urlpatterns = [
    url(r'^publisher_list/', views.publisher_list),
    url(r'^publisher_add/', views.publisher_add),
    url(r'^publisher_update/', views.publisher_update),
    url(r'^publisher_delete/', views.publisher_delete),
    url(r'^book_list/', views.book_list),
    url(r'^book_add/', views.book_add),
    url(r'^book_update/', views.book_update),
    url(r'^book_delete/', views.book_delete),
    url(r'^author_list/', views.author_list),
    url(r'^author_add/', views.author_add),
    url(r'^author_update/', views.author_update),
    url(r'^author_delete/', views.author_delete),
]