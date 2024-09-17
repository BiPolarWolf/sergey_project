from django.db import models
from .managers import TaskManager
from django.utils.translation import gettext_lazy as _



class Task(models.Model):


    class StatusChoice(models.TextChoices):
        COMPLETED = 'COMPLETE', _('Выполнено')
        IN_PROGRESS = 'IN_PROGRESS', _('В процессе')
        NOT_COMPLETED = 'NOT_COMPLETED', _('Не выполнено')


    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    status = models.CharField(max_length=15 ,choices=StatusChoice.choices, default=StatusChoice.NOT_COMPLETED)

    objects = TaskManager()
    


    def __str__(self) -> str:
        return self.title
    
    

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'