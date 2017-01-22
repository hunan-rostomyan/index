from core.indexer import ContentIndexer
from core.indexer import TitleIndexer
from core.repo import LocalRepository
from util import dict_to_json


if __name__ == '__main__':
    repo = LocalRepository('../docs-bosh/')
    repo.collect('(.*).html.md.erb')

    index_title = TitleIndexer(repo).index()
    dict_to_json(index_title, 'index_title.json')

    index_content = ContentIndexer(repo).index()
    dict_to_json(index_content, 'index_content.json')
