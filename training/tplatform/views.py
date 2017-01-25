from django.shortcuts import render
from django.http import Http404

from tplatform.models import Article
from tplatform.models import Tag
from tplatform.forms import AdvancedBrowse

def index(request):
	articles = Article.objects.all()
	return render(request, 'tplatform/index.html', {
		'articles': articles,
	})

def article_detail(request, id):
	try:
		article = Article.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This article does not exist')
	# Dummy related algorithm, will be relplaced once tagging is implemented
	related = Article.objects.all()[:5]
	return render(request, 'tplatform/article_detail.html', {
		'article': article,
		'related': related,
	})

def filter_detail(request, category, tags):
	category_list = category.split('&')
	if (tags == ''):
		articles_by_tags = Article.objects.all()
	else:
		tag_list = [int(i) for i in tags.split('&')]
		articles_by_tags = [x for x in Article.objects.all() if (set([y.id for y in x.tags.all()]) & set(tag_list))]
	if (category_list == ''):
		articles = articles_by_tags
	else:
		articles = [x for x in articles_by_tags if x.get_category_display().lower() in category_list]
	all_tags = Tag.objects.all()
	return render(request, 'tplatform/filter_detail.html', {
		'articles': articles,
		'tags': all_tags,
	})

def browse(request):
	articles = Article.objects.all()
	tags = Tag.objects.all()

	return render(request, 'tplatform/browse.html', {
		'articles': articles,
		'tags': tags,
	})

def about(request):
	return render(request, 'tplatform/about.html', {})

def strategy(request):
	articles = Article.objects.filter(category=Article.STRATEGY)
	return render(request, 'tplatform/strategy.html', {
		'articles': articles,
	})

def content(request):
	articles = Article.objects.filter(category=Article.CONTENT)
	return render(request, 'tplatform/content.html', {
		'articles': articles,
	})

def misc(request):
	articles = Article.objects.filter(category=Article.MISC)
	return render(request, 'tplatform/misc.html', {
		'articles': articles,
	})
