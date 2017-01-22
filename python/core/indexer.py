from util import tokenize


class Indexer(object):
    def __init__(self, repo):
        self.repo = repo
        self._index = {}

    def lookup(self, term):
        return self._index.get(term)


class ContentIndexer(Indexer):
    def index(self):
        for doc in self.repo.documents:
            tokens = sorted(tokenize(doc.contents))
            for token, (_line_num, _token_num) in tokens:
                if token not in self._index:
                    self._index[token] = []
                doc_name = self.repo.doc_id_to_name(doc.doc_id)
                if doc_name not in self._index[token]:
                    self._index[token].append(doc_name)
        return self._index


class TitleIndexer(Indexer):
    def index(self):
        for doc in self.repo.documents:
            tokens = sorted(tokenize(doc.contents))
            for token, (line_num, token_num) in tokens:
                if line_num == 1 and token_num >= 1:
                    if token not in self._index:
                        self._index[token] = []
                    doc_name = self.repo.doc_id_to_name(doc.doc_id)
                    if doc_name not in self._index[token]:
                        self._index[token].append(doc_name)
        return self._index