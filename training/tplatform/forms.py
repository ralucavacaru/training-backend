from django import forms

from tplatform.models import Tag

class AdvancedBrowse(forms.Form):
	tag_ids = (tag.id for tag in Tag.objects.all())
	tag_names = (tag.name for tag in Tag.objects.all())
	CHOICES = zip(tag_ids, tag_names)
	tags = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())
	tags.widget.attrs.update({'id' : 'advanced-browse-element'})