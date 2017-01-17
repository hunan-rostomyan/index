import json

from django.shortcuts import redirect
from django.shortcuts import render

from search.config import DOCS_URL
from web.settings import get_data


def home(request):
	return redirect('search', query='aws cloud upload')


def search(request, query):
	terms = [t.strip() for t in query.strip().split()]
	index = json.load(open(get_data('index.json')))

	docs = []
	for key, values in index.items():
		if any(term in key for term in terms):
			docs.append((key, values))

	context = {
		'query': query,
		'docs': docs,
		'URL': {
			'DOCS': DOCS_URL,
		}
	}
	return render(request, 'results.html', context)
