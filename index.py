from os import listdir

from collections import defaultdict
import pprint


DOC_DIR = 'docs-bosh/'
DOC_EXT = '.html.md.erb'
STOPS_FILE = 'data/stop_words.txt'
STOP_WORDS = [line.strip() for line in open(STOPS_FILE)]


def getDocs(root=DOC_DIR, ext=DOC_EXT):
    for file in listdir(root):
        if file.endswith(ext):
            yield file


def getTitle(doc, root=DOC_DIR):
    with open(DOC_DIR + doc) as f:
        for i, line in enumerate(f):
            if i == 1:
                return [w.strip() for w in line.lower().split(':')][1]


def getWords(text, stops=STOP_WORDS):
    for word in text.split():
        if word not in STOP_WORDS:
            yield word


if __name__ == '__main__':
    index = defaultdict(set)

    for doc in getDocs():
        for word in getWords(getTitle(doc)):
            index[doc].add(word)

    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(index)
