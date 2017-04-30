from django.test import TestCase

import datetime
from django.utils import timezone
from tplatform.models import Article, Author, Tag, Type
from django.core.urlresolvers import reverse

class DataSetUp(TestCase):
	@classmethod
	def setUpTestData(cls):
		# Tags and Types
		Tag.objects.create(name = 'someTag')
		Tag.objects.create(name = 'someOtherTag')
		Type.objects.create(name = 'someType', picture_handle = 'someHandle')
		Type.objects.create(name = 'someOtherType', picture_handle = 'someOtherHandle')

		# Authors
		Author.objects.create( \
							name = 'someName', \
							description = 'someDescription', \
							picture_handle = 'someAuthorHandle', \
							status = 1)
		Author.objects.create( \
							name = 'someOtherName', \
							description = 'someOtherDescription', \
							picture_handle = 'someOtherAuthorHandle', \
							status = 3)

		# Articles
		number_of_articles = 5
		for num in range(number_of_articles):
			article = Article.objects.create( \
							title = 'Title %s' % num, \
							description = 'Description %s' % num, \
							date_added = timezone.now(), \
							content = 'Content %s' % num, \
							category = num % 3 + 1)
			article.save()
			article.authors.add(Author.objects.get(pk = num%2 + 1))
			article.tags.add(Tag.objects.get(pk = num%2 + 1))
			article.types.add(Type.objects.get(pk = num%2 + 1))
			article.save()


class IndexViewTest(DataSetUp):
	def test_view_url_by_name(self):
		resp = self.client.get(reverse('index'))
		self.assertEqual(resp.status_code, 200)

	def test_view_uses_correct_template(self):
		resp = self.client.get(reverse('index'))
		self.assertTemplateUsed(resp, 'tplatform/index.html')

class ArticleDetailViewTest(DataSetUp):
	def test_view_url_by_name(self):
		resp = self.client.get(reverse('browse.article_detail', args=[1]))
		self.assertEqual(resp.status_code, 200)

	def test_view_uses_correct_template(self):
		resp = self.client.get(reverse('browse.article_detail', args=[1]))
		self.assertTemplateUsed(resp, 'tplatform/article_detail.html')

	def test_view_returns_correct_context(self):
		resp = self.client.get(reverse('browse.article_detail', args=[1]))
		self.assertEqual(resp.context['article'].id, 1)


class FilterDetailViewTest(DataSetUp):
	def test_view_url_by_name(self):
		resp = self.client.get(reverse('browse.filter_detail', args=['1', '1', '1', '1']))
		self.assertEqual(resp.status_code, 200);

	def test_view_uses_correct_template(self):
		resp = self.client.get(reverse('browse.filter_detail', args=['1', '1', '1', '1']))
		self.assertTemplateUsed(resp, 'tplatform/filter_detail.html')


class TrainersViewTest(DataSetUp):
	def test_view_url_by_name(self):
		resp = self.client.get(reverse('trainers'))
		self.assertEqual(resp.status_code, 200);

	def test_view_uses_correct_template(self):
		resp = self.client.get(reverse('trainers'))
		self.assertTemplateUsed(resp, 'tplatform/trainers.html')

	def test_view_returns_correct_context(self):
		resp = self.client.get(reverse('trainers'))
		expected_trainers = Author.objects.all()
		self.assertQuerysetEqual(resp.context['trainers'], [repr(x) for x in expected_trainers])


class TrainerDetailViewTest(DataSetUp):
	def test_view_url_by_name(self):
		resp = self.client.get(reverse('trainers.trainer_detail', args=[1]))
		self.assertEqual(resp.status_code, 200)

	def test_view_uses_correct_template(self):
		resp = self.client.get(reverse('trainers.trainer_detail', args=[1]))
		self.assertTemplateUsed(resp, 'tplatform/trainer_detail.html')

	def test_view_returns_correct_context(self):
		resp = self.client.get(reverse('trainers.trainer_detail', args=[1]))
		self.assertEqual(resp.context['trainer'].id, 1)


class ContactViewTest(DataSetUp):
	def test_view_url_by_name(self):
		resp = self.client.get(reverse('contact'))
		self.assertEqual(resp.status_code, 200)

	def test_view_uses_correct_template(self):
		resp = self.client.get(reverse('contact'))
		self.assertTemplateUsed(resp, 'tplatform/contact_us.html')


