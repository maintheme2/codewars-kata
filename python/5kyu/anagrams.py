from itertools import *
import re

def anagrams(word, words):
    output = []
    l = list(permutations(word))
    l = [", ".join(wrd) for wrd in l]
    l = [re.sub(",", "", wrd) for wrd in l]
    l = [re.sub(" ", "", wrd) for wrd in l]
    print(l[0])
    for wrd in words:
        if wrd in l:
            output.append(wrd)
    return output
    
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))