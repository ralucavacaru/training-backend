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
	tag_list = tags.split('&')
	# print 'Tags: ', tags, '\nTag list: ', tag_list
	category_list = category.split('&')
	if (tags == ''):
		articles_by_tags = Article.objects.all()
	else:
		articles_by_tags = [x for x in Article.objects.all() if (set([y.id for y in x.tags.all()]) & set(tag_list))]
	if (category_list == ''):
		articles = articles_by_tags
	else:
		articles = [x for x in articles_by_tags if x.get_category_display().lower() in category_list]
	return render(request, 'tplatform/filter_detail.html', {
		'articles': articles,
	})

def browse(request):
	articles = Article.objects.all()
	tags = Tag.objects.all()

	if request.method == 'POST':
		form = AdvancedBrowse(request.POST)
		if form.is_valid():
			tags = form.cleaned_data.get('tags')
	else:
		form = AdvancedBrowse

	return render(request, 'tplatform/browse.html', {
		'articles': articles,
		'tags': tags,
		'form': form,
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
