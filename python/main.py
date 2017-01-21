import json

from core.indexer import Indexer
from core.repo import LocalRepository


if __name__ == '__main__':
    repo = LocalRepository('../docs-bosh/')
    documents = list(repo.collect('(.*).html.md.erb'))
    indexer = Indexer(repo)
    with open('index.json', 'w') as f:
        json.dump(indexer.index, f, sort_keys=True, indent=2)
