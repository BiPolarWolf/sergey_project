from django.urls import path

urlpatterns = [
    path('articles/', views.ArticleListCreateView.as_view(),name='articles-list'),
]
