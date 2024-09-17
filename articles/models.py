from django.db import models

# Create your models here.
class Article(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE,db_column='author_id')

    
    def __str__(self) -> str:
        return self.title