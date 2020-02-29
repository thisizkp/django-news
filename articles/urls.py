from django.urls import path

from .views import ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('<int:pk>/edit', ArticleUpdateView.as_view(), name='article-edit'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(),
         name='article-delete'),
    path('<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('', ArticleListView.as_view(), name='article-list')
]
