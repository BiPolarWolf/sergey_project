from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Article
from django.contrib.auth.models import User

class ArticleSerializer(HyperlinkedModelSerializer):
    

    class Meta:
        model = Article
        fields = ['url','title','description','created_date']


