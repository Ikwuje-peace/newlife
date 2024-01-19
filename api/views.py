from django.shortcuts import render
from rest_framework import generics
from core.models import Book
from api.serializers import BookSerializer

# Create your views here.
class BookApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer