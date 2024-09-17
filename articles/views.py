from rest_framework.permissions import IsAuthenticated

from articles.serializers import ArticleSerializer
from .models import Article
from rest_framework.viewsets import ModelViewSet
from tasks.permissions import IsOwner

class ArticleViewSet(ModelViewSet): 
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsOwner,IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


    def get_queryset(self):
        if self.request.user.is_authenticated:
            return super().get_queryset().filter(owner = self.request.user)
        
    