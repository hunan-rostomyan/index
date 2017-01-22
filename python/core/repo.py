import os.path
import re

from os import listdir

from .document import Document


class Repository(object):
    def __init__(self, root):
        self.root = root
        self.doc_names = {}
        self.documents = []

    def collect(self, pattern):
        pattern = re.compile(pattern)
        ordinal = 0
        for filename, content in self.crawl(self.root):
            if pattern.match(filename):
                doc = Document(ordinal, filename, content)
                self.documents.append(doc)
                self.doc_names[ordinal] = filename
                ordinal += 1 

    def doc_id_to_name(self, doc_id):
        return self.doc_names.get(
            doc_id, 'No document with id {}'.format(doc_id))


class LocalRepository(Repository):
    def crawl(self, root):
        for filename in listdir(root):
            path = os.path.join(root, filename)
            if not os.path.isdir(path):
                with open(path) as fp:
                    yield filename, fp.read()
