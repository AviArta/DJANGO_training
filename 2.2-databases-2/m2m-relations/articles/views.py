from django.http import HttpResponse
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.all()
    context = {'object_list': object_list}
    return render(request, template, context)

def show_article(request, article_id):
    return HttpResponse(f'Отображение статьи с id = {article_id}')