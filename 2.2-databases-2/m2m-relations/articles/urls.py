from django.urls import path

from articles.views import articles_list, show_article

urlpatterns = [
    path('', articles_list, name='articles'),
    path('article/<int:article_id>/', show_article, name='article'),
]
