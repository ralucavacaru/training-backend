from django.contrib import admin

from .models import Article
from .models import Tag
from .models import Author
from .models import Type

class ArticleAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'category', 'description']

class TagAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

class AuthorAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

class TypeAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Type, TypeAdmin)


