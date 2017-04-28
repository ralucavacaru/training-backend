from django.test import TestCase
from tplatform.models import Tag
from tplatform.models import Type
from tplatform.models import Author
from tplatform.models import Article

class TagModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Tag.objects.create(name='someTag')

	def test_unicode_representation(self):
		tag = Tag.objects.get(id=1)
		expected_unicode = tag.name
		self.assertEquals(expected_unicode, unicode(tag))

class TypeModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Type.objects.create(name='someType', picture_handle='picHandle')

	def test_unicode_representation(self):
		atype = Type.objects.get(id=1)
		expected_unicode = atype.name
		self.assertEquals(expected_unicode, unicode(atype))

class AuthorModelTest(TestCase):
	@classmethod 
	def setUpTestData(cls):
		Author.objects.create(name='someTrainer', description='someDescription', \
								picture_handle='someHandle', status=3)

	def test_unicode_representation(self):
		author = Author.objects.get(id=1)
		expected_unicode = author.name
		self.assertEquals(expected_unicode, unicode(author))
