from rest_framework.permissions import BasePermission
from rest_framework.response import Response

class IsOwner(BasePermission):
    message = 'Это не ваш объект. Доступ запрещён.'

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
    
    
