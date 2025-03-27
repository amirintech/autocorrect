def delete_letter(word, verbose=False):
    delete_l = []
    split_l = [(word[:i], word[i:]) for i in range(len(word))]
    delete_l = [L + R[1:] for L, R in split_l if R]
    if verbose:
        print(f"input word {word}, \nsplit_l = {split_l}, \ndelete_l = {delete_l}")
    return delete_l


def switch_letter(word, verbose=False):
    switch_l = []
    split_l = [(word[:i], word[i:]) for i in range(len(word))]
    switch_l = [L + R[1] + R[0] + R[2:] for L, R in split_l if len(R) > 1]
    if verbose:
        print(f"input word = {word} \nsplit_l = {split_l} \nswitch_l = {switch_l}")
    return switch_l


def replace_letter(word, verbose=False):
    letters = "abcdefghijklmnopqrstuvwxyz"
    replace_l = []
    split_l = [(word[:i], word[i:]) for i in range(len(word))]
    replace_l = [
        L + l + (R[1:] if len(R) > 1 else "")
        for L, R in split_l
        if R
        for l in letters
        if l != R[0]
    ]
    replace_l = sorted(replace_l)
    if verbose:
        print(f"input word = {word} \nsplit_l = {split_l} \nreplace_l {replace_l}")
    return replace_l


def insert_letter(word, verbose=False):
    letters = "abcdefghijklmnopqrstuvwxyz"
    insert_l = []
    split_l = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    insert_l = [L + l + R for L, R in split_l for l in letters]
    if verbose:
        print(f"input word = {word} \nsplit_l = {split_l} \ninsert_l = {insert_l}")
    return insert_l


def edit_one_letter(word, allow_switches=True):
    edit_one_set = set()
    edit_one_set.update(delete_letter(word))
    if allow_switches:
        edit_one_set.update(switch_letter(word))
    edit_one_set.update(replace_letter(word))
    edit_one_set.update(insert_letter(word))
    return edit_one_set


def edit_two_letters(word, allow_switches=True):
    edit_two_set = set()
    one_edit = edit_one_letter(word, allow_switches=allow_switches)
    for w in one_edit:
        if w:
            edit_two = edit_one_letter(w, allow_switches=allow_switches)
            edit_two_set.update(edit_two)
    return edit_two_set
