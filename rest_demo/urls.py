from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateAPIView

urlpatterns = [
    path('api/books/',BookListCreateAPIView.as_view(), name = 'book_list_create'),
    path('api/books/<int:pk>/update/',BookRetrieveUpdateAPIView.as_view(), name= 'book_item_update'),
]