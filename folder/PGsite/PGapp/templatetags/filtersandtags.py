from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='monthly_currency')
@stringfilter
def monthly_currency(value, name):
	return f'monthly pay: {value} {name}'


@register.filter(name='monthly_currency_3')
@stringfilter
def monthly_currency_3(value, name):
	value = int(value)*3
	return f'3-months pay: {value} {name}'


@register.filter(name='monthly_currency_6')
@stringfilter
def monthly_currency_6(value, name):
	value = int(value)*6
	return f'6-months pay: {value} {name}'


@register.filter(name='monthly_currency_12')
@stringfilter
def monthly_currency_12(value, name):
	value = int(value)*12
	return f'12-months pay: {value} {name}'
