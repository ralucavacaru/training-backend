from tplatform.models import Tag
from tplatform.models import Author
from tplatform.models import Type

def getcustomoptions(request):	
	all_tags = [x for x in Tag.objects.all().order_by('name') if x.article_set.all().exists()]
	all_authors = [x for x in Author.objects.all().order_by('name') if x.article_set.all().exists()]
	all_types = Type.objects.all().order_by('name');
	return {
		'tags': all_tags,
		'authors': all_authors,
		'types': all_types,
	}