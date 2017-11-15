from django.shortcuts import render
from django.http import Http404
from django.template import RequestContext
from tplatform.forms import *
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template

from tplatform.models import Article
from tplatform.models import Tag
from tplatform.models import Author
from tplatform.models import Type

def index(request):
	# articles = Article.objects.all()
	return render(request, 'tplatform/index.html', {})

def article_detail(request, id):
	try:
		article = Article.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This article does not exist')
	related = article.related_articles.all()
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
	
	return render(request, 'tplatform/filter_detail.html', {
		'articles': articles,
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
	return render(request, 'tplatform/contact_us.html', {
		})

# Setting up email server: https://hellowebbooks.com/news/tutorial-setting-up-a-contact-form-with-django/
def request_training(request):
	form_class = RequestTrainingForm

	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get(
				'contact_name'
			, '')
			contact_email = request.POST.get(
				'contact_email'
			, '')
			institution = request.POST.get(
				'institution'
			, '')
			country = request.POST.get(
				'country'
			, '')
			form_content = request.POST.get('content', '')

			# Email the profile with the 
			# contact information
			template = get_template('contact_template.txt')
			context = {
				'contact_name': contact_name,
				'contact_email': contact_email,
				'institution': institution,
				'country': country,
				'form_content': form_content,
			}
			content = template.render(context)

			send_mail('Training Request', content, 'ralucavacaru05@gmail.com', ['ca@scottisheudc2018.com'], fail_silently=False)
			return redirect('contact')

	return render(request, 'tplatform/request_training.html', {
		'form': form_class,
	})

def request_resources(request):
	form_class = RequestResourcesForm

	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get(
				'contact_name'
			, '')
			contact_email = request.POST.get(
				'contact_email'
			, '')
			institution = request.POST.get(
				'institution'
			, '')
			country = request.POST.get(
				'country'
			, '')
			form_content = request.POST.get('content', '')

			# Email the profile with the 
			# contact information
			template = get_template('contact_template.txt')
			context = {
                                'contact_name': contact_name,
                                'contact_email': contact_email,
                                'institution': institution,
                                'country': country,
                                'form_content': form_content,
                        }
                        content = template.render(context)

                        send_mail('Resource Request', content, 'ralucavacaru05@gmail.com', ['ca@scottisheudc2018.com'], fail_silently=False)
                        return redirect('contact')

	return render(request, 'tplatform/request_resources.html', {
		'form': form_class,
	})

def send_feedback(request):
	form_class = FeedbackForm

	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get(
				'contact_name'
			, '')
			contact_email = request.POST.get(
				'contact_email'
			, '')
			institution = request.POST.get(
				'institution'
			, '')
			country = request.POST.get(
				'country'
			, '')
			form_content = request.POST.get('content', '')

			# Email the profile with the 
			# contact information
			template = get_template('contact_template.txt')

			context = {
                                'contact_name': contact_name,
                                'contact_email': contact_email,
                                'institution': institution,
                                'country': country,
                                'form_content': form_content,
                        }
                        content = template.render(context)

                        send_mail('Training Feedback', content, 'ralucavacaru05@gmail.com', ['ca@scottisheudc2018.com'], fail_silently=False)
                        return redirect('contact')

	return render(request, 'tplatform/send_feedback.html', {
		'form': form_class,
	})

def join_team(request):
	form_class = JoinForm

	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get(
				'contact_name'
			, '')
			contact_email = request.POST.get(
				'contact_email'
			, '')
			institution = request.POST.get(
				'institution'
			, '')
			country = request.POST.get(
				'country'
			, '')
			form_content = request.POST.get('content', '')

			# Email the profile with the 
			# contact information
			template = get_template('contact_template.txt')
			context = {
                                'contact_name': contact_name,
                                'contact_email': contact_email,
                                'institution': institution,
                                'country': country,
                                'form_content': form_content,
                        }
                        content = template.render(context)

                        send_mail('Training Application', content, 'ralucavacaru05@gmail.com', ['ca@scottisheudc2018.com'], fail_silently=False)
                        return redirect('contact')

	return render(request, 'tplatform/join_team.html', {
		'form': form_class,
	})
