from rest_framework import serializers
from .models import Author, BlogPost, Comment


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = BlogPost
        fields = '__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'