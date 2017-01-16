import json

from config import config
from util import docs_from_dir
from util import lines_from_file
from util import words_from_text


def inferTitle(doc_lines):
    """Given lines from a document, infer its title.

    Assumes the lines are pairs (i, line) where i
    is a 0-indexed indicator of the line number and
    line is the text of that line.

    Assumes titles are on the second line (i = 1) and
    that they contain a unique colon (':') to the right
    of which the title is located. Example:

        title: This is an example title

    Returns the title (string).
    """
    for i, line in doc_lines:
        if i == 1:
            try:
                title = line.lower().split(':')[1]
                return title.strip()
            except IndexError:
                raise ValueError('Document has the wrong format.')


def buildIndex(contentFilter=inferTitle):
    index = {}
    for doc in docs_from_dir():
        doc_lines = lines_from_file(config['DOC_DIR'] + doc)
        contents = contentFilter(doc_lines)
        for word in words_from_text(contents):
            if word not in index:
                index[word] = []
            if doc not in index[word]:
                index[word].append(doc)
    return index


if __name__ == '__main__':
    index = buildIndex()
    with open(config['OUTPUT_FILE'], 'w') as f:
        json.dump(index, f, sort_keys=True, indent=2)
