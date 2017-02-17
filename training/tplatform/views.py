from django.shortcuts import render
from django.http import Http404

from tplatform.models import Article
from tplatform.models import Tag
from tplatform.models import Author
from tplatform.models import Type
from tplatform.forms import AdvancedBrowse

def index(request):
	articles = Article.objects.all()
	return render(request, 'tplatform/index.html')

def article_detail(request, id):
	try:
		article = Article.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This article does not exist')
	# Dummy related algorithm, will be relplaced with manual related when I introduce the data
	related = Article.objects.all()[:5]
	return render(request, 'tplatform/article_detail.html', {
		'article': article,
		'related': related,
	})

def filter_detail(request, category, tags, types, authors):
	all_articles = Article.objects.all().order_by('date_added').reverse()
	# By tags:
	if (tags == ''):
		articles = all_articles
	else:
		tag_list = [int(i) for i in tags.split('&')]
		articles = [x for x in all_articles if (set([y.id for y in x.tags.all()]) & set(tag_list))]
	
	# By category:
	if (category != ''):
		aux = articles
		category_list = category.split('&')
		articles = [x for x in aux if x.get_category_display().lower() in category_list]
	
	# By type:
	if (types != ''):
		aux = articles
		types_list = [int(i) for i in types.split('&')]
		articles = [x for x in aux if (set([y.id for y in x.types.all()]) & set(types_list))]
	
	# By author:
	if (authors != ''):
		aux = articles
		authors_list = [int(i) for i in authors.split('&')]
		articles = [x for x in aux if (set([y.id for y in x.authors.all()]) & set(authors_list))]
	
	all_tags = Tag.objects.all()
	all_authors = Author.objects.all()
	all_types = Type.objects.all();
	return render(request, 'tplatform/filter_detail.html', {
		'articles': articles,
		'tags': all_tags,
		'authors': all_authors,
		'types': all_types,
	})

def browse(request):
	articles = Article.objects.all()
	tags = Tag.objects.all()

	return render(request, 'tplatform/browse.html', {
		'articles': articles,
		'tags': tags,
	})

def trainers(request):
	trainers = Author.objects.order_by('name')
	return render(request, 'tplatform/trainers.html', {
		'trainers': trainers,
	})

def trainer_detail(request, id):
	try:
		trainer = Author.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This trainer does not exist')

	articles = trainer.article_set.all()
	return render(request, 'tplatform/trainer_detail.html', {
		'trainer': trainer,
		'articles': articles,
	})

def contact(request):
	return render(request, 'tplatform/contact_us.html')