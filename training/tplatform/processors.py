from tplatform.models import Tag
from tplatform.models import Author
from tplatform.models import Type

def getcustomoptions(request):	
	all_tags = Tag.objects.all()
	all_authors = Author.objects.all()
	all_types = Type.objects.all();
	return {
		'tags': all_tags,
		'authors': all_authors,
		'types': all_types,
	}