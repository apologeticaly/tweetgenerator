import re
import sys

corpus = "paragraph.txt"
filehandle = open(corpus, "r")

def clean(corpus):
    with open(corpus, 'r') as file:
        corpus = file.read()
        scrubbed_words = re.sub(r'[^a-zA-Z\s]', '', corpus).lower().split()
        return scrubbed_words

histo = {}

def histogram():
    for word in clean(corpus):           
        if word in histo: 
            histo[word] += 1
        else: 
            histo[word] = 1

    return histo

def unique():
    used_words = []
    unique_words = 1

    for word in clean(corpus):
        if word not in used_words:
            unique_words = unique_words + 1
            used_words.append(word)

    return unique_words


def frequency(search):
    if search in histo:
        return 'The word ' + str(search) + ' occurs ' + str(histo[search]) + ' times!'
    else:
        return 'Word does not occur'

if __name__ == '__main__':
    # print(clean(corpus))
    # print(histogram)
    for word in histogram():
        print(word, histo[word])

    print(unique())
    print(frequency(sys.argv[1]))
    