import re


def endswith(suffix):
	return '(.*){}$'.format(suffix)
