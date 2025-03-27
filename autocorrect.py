import numpy as np
from word_edits import edit_one_letter, edit_two_letters


def get_corrections(word, probs, vocab, n=2, verbose=False):
    suggestions = []
    n_best = []
    if word in vocab:
        if verbose:
            print("you entered a word that's already in the vocabulary.")
        suggestions = [word]
    else:
        suggestions = list(edit_one_letter(word))
        if not suggestions:
            suggestions = list(edit_two_letters(word))
        tmp_suggestions = []
        for l in suggestions:
            if l in vocab:
                tmp_suggestions.append(l)
        suggestions = tmp_suggestions
    if verbose:
        print(
            f"the suggestions after passing them through the vocabulary are: {suggestions}"
        )
    word_probs = {}
    for w in suggestions:
        word_probs[w] = probs[w]
    if verbose:
        print(f"word_probs = {word_probs}")
    sorted_words = sorted(word_probs.items(), key=lambda item: item[1], reverse=True)
    n_best = sorted_words[:n]
    if verbose:
        print(f"n_best = {n_best}")
    return n_best


def min_edit_distance(target, source, ins_cost=1, del_cost=1, sub_cost=2):
    m = len(target)
    n = len(source)
    D = np.zeros((m + 1, n + 1), dtype=int)
    for row in range(m + 1):
        D[row, 0] = row * del_cost
    for col in range(n + 1):
        D[0, col] = col * ins_cost
    for row in range(1, m + 1):
        for col in range(1, n + 1):
            r_cost = sub_cost
            if target[row - 1] == source[col - 1]:
                r_cost = 0
            D[row, col] = min(
                [
                    D[row - 1, col] + del_cost,
                    D[row, col - 1] + ins_cost,
                    D[row - 1, col - 1] + r_cost,
                ]
            )
    return D[m, n]
