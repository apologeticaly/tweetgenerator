
import sys
import random
from random import randint
from histogram import listogram, clean

# Declare the source of knowledge
source_text = 'ht.txt'

corpus = clean(source_text)

# Declare the length of the source of knowledge
total = len(corpus)

listogram = listogram(corpus)



def simple():
    return random.choice(listogram)

def run():
    sentence = []
    while len(sentence) <= 7:
        sentence.append(simple()[0])
    return sentence