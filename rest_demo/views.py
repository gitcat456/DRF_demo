from rest_framework import generics, viewsets
from .models import Book 
from .serializers import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_queryset(self):
        queryset = self.queryset
        author_filter = self.request.query_params.get('author')
        year_filter = self.request.query_params.get('published_date')
        
        if author_filter:
            queryset = queryset.filter(author__icontains=author_filter)
        
        if year_filter:
            queryset = queryset.filter(published_date__year=year_filter)
        
        return queryset
            
    
class BookRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects. all()
    serializer_class = BookSerializer
    
    def get_queryset(self):
        queryset = self.queryset
        author_filter = self.request.query_params.get('author', None)
        if author_filter is not None:
             queryset = queryset.filter(author__icontains=author_filter)
        return queryset
        
    
    
    
