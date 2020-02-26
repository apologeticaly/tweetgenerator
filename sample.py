
import sys
import random
from random import randint
from histogram import dictogram, clean

# Declare the source of knowledge
source_text = 'hardtimes.txt'

corpus = clean(source_text)

# Declare the length of the source of knowledge
total = len(corpus)

dictogram = dictogram(corpus)

# Function for regular use; will return one word
def sample():
    total = len(dictogram.keys())
    rand_val = random.randint(1, total)

    total = 0

    for key, value in dictogram.items():
        total += value
        
        if rand_val < total:
            return key

def run():
    sentence = []
    while len(sentence) <= 7:
        sentence.append(sample())
    return sentence
# for _ in range(100):
sample()