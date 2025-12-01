from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, AuthorViewSet, CommentViewSet

router = DefaultRouter()

router.register(r'author', AuthorViewSet)
router.register(r'blog', BlogPostViewSet)
router.register(r'comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]