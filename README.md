# AutoCorrect

AutoCorrect is a spell-checking and correction tool that uses probabilistic methods to identify and correct misspelled words. It leverages a reference text corpus to compute word frequencies and suggests the most likely corrections for misspellings.

## Features

- **Spell Checking**: Identifies misspelled words in text.
- **Correction Suggestions**: Provides the most probable corrections based on word frequencies.
- **Customizable Corpus**: Uses a given text corpus (e.g., Shakespeare's works) to train the model.
- **Efficient Algorithm**: Implements multiple word-editing techniques to generate correction candidates.

## Installation

To install and use AutoCorrect, follow these steps:

```bash
git clone https://github.com/amirintech/autocorrect.git
cd autocorrect
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
```

## How It Works

### 1. Building the Vocabulary

The tool processes a given text corpus to extract words and build a vocabulary with word frequencies.

```python
def process_data(file_name):
    words = []
    with open(file_name, 'r') as file:
        text = file.read()
    rgx = re.compile(r'\w+')
    text = text.lower()
    words = rgx.findall(text)
    return words
```

A word count dictionary is then created:

```python
def get_count(word_l):
    return Counter(word_l)
```

And the probability of each word occurring is computed:

```python
def get_probs(word_count_dict):
    total = sum(word_count_dict.values())
    return {w: c/total for w, c in word_count_dict.items()}
```

### 2. Generating Possible Word Edits

To generate correction suggestions, AutoCorrect creates variations of a word using four basic operations:

- **Deletion**: Removing one character.
- **Switching**: Swapping adjacent characters.
- **Replacement**: Changing one character to another.
- **Insertion**: Adding a character.

### 3. Selecting the Best Correction

AutoCorrect first checks if a word exists in the vocabulary. If not, it generates possible edits and ranks them by probability:

```python
def get_corrections(word, probs, vocab, n=2):
    suggestions = [word] if word in vocab else list(edit_one_letter(word))
    suggestions = [w for w in suggestions if w in vocab]
    word_probs = {w: probs[w] for w in suggestions}
    return sorted(word_probs.items(), key=lambda item: item[1], reverse=True)[:n]
```

### 4. Computing Minimum Edit Distance

To evaluate how close two words are, the tool calculates the minimum edit distance using dynamic programming:

```python
def min_edit_distance(target, source, ins_cost=1, del_cost=1, sub_cost=2):
    m, n = len(target), len(source)
    D = np.zeros((m+1, n+1), dtype=int)
    for row in range(m+1):
        D[row, 0] = row * del_cost
    for col in range(n+1):
        D[0, col] = col * ins_cost
    for row in range(1, m+1):
        for col in range(1, n+1):
            cost = 0 if target[row-1] == source[col-1] else sub_cost
            D[row, col] = min(D[row-1, col] + del_cost, D[row, col-1] + ins_cost, D[row-1, col-1] + cost)
    return D[m, n]
```

## Example Usage

```python
my_word = 'famile'
corrections = get_corrections(my_word, probs, vocab, 2)
print(f"The suggestions for '{my_word}' are: {corrections}")
```

## File Structure

- `autocorrect.py` - Contains the main AutoCorrect functions.
- `preprocessing.py` - Handles text preprocessing and tokenization.
- `word_edits.py` - Implements functions for generating spelling variations.
- `main.py` - Entry script for running the spell checker.
- `data/shakespeare.txt` - Sample corpus file for building word probabilities.
