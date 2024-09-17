from django.db import models

# Create your models here.
class Article(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    
    def __str__(self) -> str:
        return self.title