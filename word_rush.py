''' take input of a jumbled up word and output
 all the possible real word made using those letters'''

from spellchecker import SpellChecker
from nltk.corpus import words
from itertools import permutations
spell = SpellChecker()
input_string = input("Enter an anagram of a word\n")
stuff = [''.join(a) for a in permutations(input_string)]
possiblities = spell.known(stuff)
print("The possible real word/words are:")
for i in possiblities:
    if i in words.words():
        print(i)
