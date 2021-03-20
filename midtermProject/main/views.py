from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Book, Journal
from .serializers import BookSerializer, JournalSerializer
# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)

    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = (AllowAny,)
    #     elif self.action == 'retrieve':
    #         permission_classes = (AllowAny,)
    #     elif self.action == 'create':
    #         permission_classes = (IsAdminUser,)
    #     elif self.action == 'update':
    #         permission_classes = (IsAdminUser,)
    #     elif self.action == 'destroy':
    #         permission_classes = (IsAdminUser,)


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = (AllowAny,)


    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = (AllowAny,)
    #     elif self.action == 'retrieve':
    #         permission_classes = (AllowAny,)
    #     elif self.action == 'create':
    #         permission_classes = (IsAdminUser,)
    #     elif self.action == 'update':
    #         permission_classes = (IsAdminUser,)
    #     elif self.action == 'destroy':
    #         permission_classes = (IsAdminUser,)


