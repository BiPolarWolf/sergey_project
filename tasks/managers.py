from django.db import models


class TaskManager(models.Manager):

    def for_user(self,user):
        return self.get_queryset().filter(owner=user)

