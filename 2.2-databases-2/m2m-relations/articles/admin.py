from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            data = form.cleaned_data
            is_main = data.get('is_main')
            if is_main:
                counter += 1
        if counter == 1:
            return super().clean()
        elif counter >= 1:
            raise ValidationError('Основным может быть только один раздел')
        elif counter == 0:
            raise ValidationError('Укажите главный тег')


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at', 'image']
    list_display_links = ('title',)
    search_fields = ('title', 'text')
    list_filter = ['tags']
    inlines = [ScopeInline,]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'tag']


