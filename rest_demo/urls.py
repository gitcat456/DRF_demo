from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BookListCreateAPIView, BookRetrieveUpdateAPIView, BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api/books/',BookListCreateAPIView.as_view(), name = 'book_list_create'),
    path('api/books/<int:pk>/update/',BookRetrieveUpdateAPIView.as_view(), name= 'book_item_update'),
    path('viewset/', include(router.urls))
]