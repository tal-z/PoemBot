from nltk.corpus import gutenberg
from nltk import pos_tag
from nltk.corpus import brown
import numpy as np
from nltk.tokenize.treebank import TreebankWordDetokenizer
import re


"""Step 1: Build dictionary of tagged words"""
tagged_words = brown.tagged_words()
tagged_words_dict = {}
for tup in tagged_words:
    if tup[1] in tagged_words_dict:
        tagged_words_dict[tup[1]].append(tup[0].lower())
    else:
        tagged_words_dict[tup[1]] = []
        tagged_words_dict[tup[1]].append(tup[0].lower())

'''Uncomment the following two lines if we just want to use the brown corpus's vocabulary, and ignore word frequency.'''
for k,v in tagged_words_dict.items():
    tagged_words_dict[k] = list(set(v))

"""Step 2: Choose a work, identify the author, and choose a sentence."""
work = gutenberg.fileids()[np.random.randint(len(gutenberg.fileids()))]
author = re.findall('(\w+)-',work)[0].title()

sentences = gutenberg.sents(work)

rndm_sentence = sentences[np.random.randint(len(sentences))]

tagged_rndm_sentence = pos_tag(rndm_sentence)


new_sentence = []
for tup in tagged_rndm_sentence:
    if tup[0].isalpha():
        if tup[1] in tagged_words_dict:
            rndm_num = np.random.randint(len(tagged_words_dict[tup[1]]))
            rndm_word = tagged_words_dict[tup[1]][rndm_num]
            if rndm_word.isalpha():
                new_word = rndm_word
            else:
                new_word = tup[0]
        else:
            new_word = tup[0]
    else:
        new_word = tup[0]
    new_sentence.append(new_word)


new_sentence = str(TreebankWordDetokenizer().detokenize(new_sentence))
new_sentence = new_sentence[0].upper() + new_sentence[1:]
if  new_sentence[-1].isalnum():
    new_sentence = new_sentence+'.'

print(f"{author}:", tagged_rndm_sentence)
print(f"{author}:", new_sentence)



