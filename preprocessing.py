import re
from collections import Counter


def process_data(file_name):
    words = []
    with open(file_name, "r") as file:
        text = file.read()
    rgx = re.compile(r"\w+")
    text = text.lower()
    words = rgx.findall(text)
    return words


def get_count(word_l):
    word_count_dict = Counter(word_l)
    return word_count_dict


def get_probs(word_count_dict):
    total = sum(word_count_dict.values())
    probs = {w: c / total for w, c in word_count_dict.items()}
    return probs
