import re
import string


STOPS_FILE = '../data/stop_words.txt'
STOP_WORDS = [line.strip() for line in open(STOPS_FILE)]


def lines_from_file(path):
    with open(path) as f:
        for i, line in enumerate(f):
            yield i, line


def remove_punctuation(text):
    regex = re.compile('[{}]'.format(re.escape(string.punctuation)))
    return regex.sub('', text)


def words_from_text(text, exclude=STOP_WORDS):
    text = remove_punctuation(text)
    for word in text.split():
        if word not in STOP_WORDS:
            yield word
