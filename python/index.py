from os import listdir
import json


DOC_DIR = '../docs-bosh/'
DOC_EXT = '.html.md.erb'
OUTPUT_FILE = 'index.json'
STOPS_FILE = '../data/stop_words.txt'
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


def buildIndex(contentFilter=getTitle):
    index = {}
    for doc in getDocs():
        contents = contentFilter(doc)
        for word in getWords(contents):
            if word not in index:
                index[word] = []
            if doc not in index[word]:
                index[word].append(doc)
    return index


if __name__ == '__main__':
    index = buildIndex()
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(index, f, sort_keys=True, indent=2)
