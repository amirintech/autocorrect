from preprocessing import process_data, get_count, get_probs
from word_edits import (
    delete_letter,
    switch_letter,
    replace_letter,
    insert_letter,
    edit_one_letter,
    edit_two_letters,
)
from autocorrect import get_corrections, min_edit_distance


# Data loading and preprocessing
word_l = process_data("./shakespeare.txt")
vocab = set(word_l)
print(f"the first ten words in the text are: \n{word_l[0:10]}")
print(f"there are {len(vocab)} unique words in the vocabulary.")

word_count_dict = get_count(word_l)
print(f"there are {len(word_count_dict)} key values pairs")
print(f"the count for the word 'thee' is {word_count_dict.get('thee',0)}")

probs = get_probs(word_count_dict)
print(f"length of probs is {len(probs)}")
print(f"p('thee') is {probs['thee']:.4f}")

# String manipulation examples
# delete_word_l = delete_letter(word="cans", verbose=True)
# print(f"number of outputs of delete_letter('at') is {len(delete_letter('at'))}")

# switch_word_l = switch_letter(word="eta", verbose=True)
# print(f"number of outputs of switch_letter('at') is {len(switch_letter('at'))}")

# replace_l = replace_letter(word="can", verbose=True)
# print(f"number of outputs of replace_letter('at') is {len(replace_letter('at'))}")

# insert_word_l = insert_letter(word="at", verbose=True)
# print(f"number of outputs of insert_letter('at') is {len(insert_letter('at'))}")

# Edits examples
# tmp_word = "at"
# tmp_edit_one_set = edit_one_letter(tmp_word)
# tmp_edit_one_l = sorted(list(tmp_edit_one_set))
# print(f"input word {tmp_word} \nedit_one_l \n{tmp_edit_one_l}\n")
# print(
#     f"the number of possible edits one letter away from 'at' is {len(edit_one_letter('at'))}"
# )

# tmp_edit_two_set = edit_two_letters(tmp_word)
# tmp_edit_two_l = sorted(list(tmp_edit_two_set))
# print(f"input word {tmp_word} \nedit_two_l \n{tmp_edit_two_l}\n")
# print(
#     f"the number of possible edits two letters away from 'at' is {len(edit_two_letters('at'))}"
# )
print("\n\n\n")
# Autocorrection example
my_word = "famile"
tmp_corrections = get_corrections(my_word, probs, vocab, 2, verbose=True)
print(f"the suggestions for '{my_word}' are: {tmp_corrections}")
print(f"the suggestions for 'cnde' are: {get_corrections('cnde', probs, vocab, 3)}")

print("\n\n\n")
# Minimum edit distance examples
example = min_edit_distance("cats", "cast")
print(f"min_edit_distance('cats', 'cast') = {example}")
example = min_edit_distance("intention", "execution")
print(f"min_edit_distance('intention', 'execution') = {example}")
example = min_edit_distance("write", "wring")
print(f"min_edit_distance('write', 'wring') = {example}")
