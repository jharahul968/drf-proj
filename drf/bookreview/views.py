from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView

# Create your views here.


class AuthorView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorInstanceView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


def index_view(request):
    response = {
        'authors': Author.objects.all(),
        # 'books': Book.objects.all(),
    }
    return render(request, 'bookreview/index.html', response)
