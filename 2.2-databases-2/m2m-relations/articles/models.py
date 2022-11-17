from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=300, verbose_name='Тег')
    # scopes

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tag, related_name='article_tags', through='Scope')
    # scopes

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    # функция "показать на сайте" в админ-панели
    def get_absolute_url(self):
        return reverse('article', kwargs={'article_id': self.pk})


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField()

    class Meta:
        verbose_name = 'Статья-теги'
        verbose_name_plural = 'Статьи-теги'