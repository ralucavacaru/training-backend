from django.contrib import admin

from .models import Article
from .models import Tag

class ArticleAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'author']

class TagAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)

