from util import tokenize


class Indexer:
    def __init__(self, repo):
        self.index = {}
        for doc in repo.documents:
            tokens = sorted(tokenize(doc.contents))
            for token, (_line_num, _token_num) in tokens:
                if token not in self.index:
                    self.index[token] = []
                doc_name = repo.doc_id_to_name(doc.doc_id)
                if doc_name not in self.index[token]:
                    self.index[token].append(doc_name)

    def lookup(self, term):
        return self.index.get(term)