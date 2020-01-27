import sys
import random

sentence = sys.argv[1:]

random.shuffle(sentence)

print(' '.join(sentence))