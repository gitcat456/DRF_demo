from django.shortcuts import render
from rest_framework import viewsets
from .models import Author, Comment, BlogPost
from .serializers import BlogPostSerializer, CommentSerializer, AuthorSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
          
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        queryset=self.queryset
        post_filter=self.request.query_params.get('post_id')
        
        if post_filter:
            queryset=queryset.filter(post=post_filter)
            
        return queryset


