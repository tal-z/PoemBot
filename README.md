# PoemBot

## About
This repo is for files related to composing poems by algorithm.

## Guide
#### SentenceWriter.py:
1) Grab a random sentence from a random work in the Project Gutenberg corpus that comes packaged with NLTK. 
2) POS-tag every word in the sentence.
3) Read already-POS-tagged-words from the Brown corpus into a dictionary, such that the POS-tag is the key and the value is a de-duped list of all the words in the corpus with that tag.
4) Iterate through the tagged sentence from step two, and for each word:    Check if the word is purely alphabetical (this stops me from fucking up the punctuation too badly).         If the word is purely alphabetical, check if its POS-tag is contained in the tagged-words dict from step 3.             If both conditions are met, select a word at random from the respective dictionary entry, and add it to a list.     If any of the above conditions are not met, add the original word from the random sentence in step 1 to the list instead.
5) Detokenize the list of words into a sentence. 
6) Print out the name of the author and the sentence.

## Use
Simply import and deploy the only function in the SentenceWriter module as follows:

    from SentenceWriter import write_sentence()

    write_sentence()
This will return a tuple length 2, with the author's surname in the first position and the randomly-generated sentence that imitates their style in the second position. Like the following example:

`('Edgeworth', 'The non-western batten inter Somerville, following Ireland, multiplies, by these unmodified monuments, cast the understanding or hydrous glove past an jealous war.')`



Here are some random outputs:

-('Bryant', 'Plasticity Oh, particle, toleration propriety, beware me a stagecoach, dimensionally!')
-('Austen', "The output-axis persists legitimately outwit t' bat, & exacts its bookshelf tarpon.")
-('Shakespeare', 'He need my Lord atop interstitial, completed unofficial poems unlike his linguistics to me.')
-('Chesterton', "The middle-sized maget deemed his congenital magnetism tactically 'round the lapel sonogram, besides complimenting it.")


