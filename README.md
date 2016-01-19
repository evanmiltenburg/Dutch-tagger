# Dutch tagger

This repository contains a trained part-of-speech tagger for Dutch, as well as the code used to train it.
(The file `cowparser.py` comes from [this](https://github.com/evanmiltenburg/cowparser_dutch) repository.)

Requirements: NLTK version 3.1

**Key facts**:

* The tagger was trained on the NLCOW14 corpus (which in turn was tagged using TreeTagger).
* The accuracy is about 97% on held-out data from the same corpus. 
* The small model is trained on 2 million tokens, while the larger model is trained on 10 million tokens.
* The accuracy of the larger model is slightly better than the smaller model, but the larger model is over three times as large.

### How to use the tagger.
First run `bash create_models.sh`. This will create the models for you. Then use the following code.

```python
from nltk.tag.perceptron import PerceptronTagger

# This may take a few minutes. (But once loaded, the tagger is really fast!)
tagger = PerceptronTagger(load=False)
tagger.load('model.perc.dutch_tagger_small')

# Tag a sentence.
tagger.tag('Alle vogels zijn nesten begonnen , behalve ik en jij .'.split())
```
Result:

```python
[('Alle', 'det__indef'), ('vogels', 'nounpl'), ('zijn', 'verbprespl'), ('nesten', 'nounpl'), ('begonnen', 'verbpapa'), (',', 'punc'), ('behalve', 'conjsubo'), ('ik', 'pronpers'), ('en', 'conjcoord'), ('jij', 'pronpers'), ('.', '$.')]
```

If the text is not tokenized yet, you can use the built-in tokenizer from the NLTK
(be sure to download the NLTK data):

```python
import nltk.data
from nltk.tokenize import word_tokenize

sent_tokenizer = nltk.data.load('tokenizers/punkt/dutch.pickle')
    
def tokenize(text):
    for sentence in sent_tokenizer.tokenize(text):
        yield word_tokenize(sentence)

sentences = tokenize('Alle vogels zijn nesten begonnen, behalve ik en jij. Waar wachten wij nu op?')

for sentence in sentences:
    print(tagger.tag(sentence))
```

Result:
```python
[('Alle', 'det__indef'), ('vogels', 'nounpl'), ('zijn', 'verbprespl'), ('nesten', 'nounpl'), ('begonnen', 'verbpapa'), (',', 'punc'), ('behalve', 'conjsubo'), ('ik', 'pronpers'), ('en', 'conjcoord'), ('jij', 'pronpers'), ('.', '$.')]
[('Waar', 'pronadv'), ('wachten', 'verbprespl'), ('wij', 'pronpers'), ('nu', 'adv'), ('op', 'adv'), ('?', '$.')]
```
