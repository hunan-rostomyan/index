import re
import string


STOPS_FILE = '../data/stop_words.txt'
STOP_WORDS = [line.strip() for line in open(STOPS_FILE)]


def remove_punctuation(text):
    regex = re.compile('[{}]'.format(re.escape(string.punctuation)))
    return regex.sub(' ', text)


def tokenize(text, exclude=STOP_WORDS):
    text = remove_punctuation(text).lower()
    lines = text.splitlines()
    for line_num, line in enumerate(lines):
        tokens = [word for word in line.split() if word not in STOP_WORDS]
        for token_num, token in enumerate(tokens):
            yield token, (line_num, token_num)
