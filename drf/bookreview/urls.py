from django.contrib import admin
from django.urls import path, include
from .views import AuthorView, AuthorInstanceView, index_view

urlpatterns = [
    path('index/', index_view, name='index'),
    path('authors/', AuthorView.as_view(), name='author-list'),
    path('authors/<int:pk>', AuthorInstanceView.as_view(), name='author-instance')
]
