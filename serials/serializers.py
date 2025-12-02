from rest_framework import serializers
from .models import Author, BlogPost, Comment


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        
class BlogPostSerializer(serializers.ModelSerializer):
    #basically create another field called author_name 
    author_name = serializers.CharField(source='author.name', read_only=True)
    
    #overide the author field to return the author name
      # author = serializers.CharField(source='authors.name', read_only=True)
   
   #return the complete author objects ie nesting 
    author = AuthorSerializer(read_only=True)
    
    class Meta: 
        model = BlogPost
        fields = '__all__'

        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1
        
