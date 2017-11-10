from django import template

register = template.Library()

@register.filter
def sort_alphabetically(values, field):
	return sorted(values, key=lambda item: getattr(item, field).lower())