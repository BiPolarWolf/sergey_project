from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskListCreateView.as_view(),name='tasks-list'),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroyView.as_view(),name='tasks-detail'),
]
