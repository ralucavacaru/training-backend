from django.shortcuts import render
from django.http import Http404

from tplatform.models import Article

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

def browse(request):
	articles = Article.objects.all()
	return render(request, 'tplatform/browse.html', {
		'articles': articles,
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
