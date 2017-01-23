from util import tokenize


class Indexer(object):
    def __init__(self, repo):
        self.repo = repo
        self._index = []

    def lookup(self, term):
        return self._index.get(term)


# TODO: refactor
class ContentIndexer(Indexer):
    def index(self):
        for doc in self.repo.documents:
            contents = doc.contents
            tokens = sorted(tokenize(contents))
            title = contents.splitlines()[1].split(':')[1].strip()
            doc_name = self.repo.doc_id_to_name(doc.doc_id)
            keywords = []
            for token, (_line_num, _token_num) in tokens:
                if token not in keywords:
                    keywords.append(token)
            self._index.append({
                'entry': doc_name,
                'title': title,
                'keywords': keywords,
            })
        return self._index


# TODO: refactor
class TitleIndexer(Indexer):
    def index(self):
        for doc in self.repo.documents:
            contents = doc.contents
            tokens = sorted(tokenize(contents))
            title = contents.splitlines()[1].split(':')[1].strip()
            doc_name = self.repo.doc_id_to_name(doc.doc_id)
            keywords = []
            for token, (line_num, token_num) in tokens:
                if line_num == 1 and token_num >= 1:
                    if token not in keywords:
                        keywords.append(token)
            self._index.append({
                'entry': doc_name,
                'title': title,
                'keywords': keywords,
            })
        return self._index
