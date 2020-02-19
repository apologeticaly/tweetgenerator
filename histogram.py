import re
import sys

corpus = "paragraph.txt"
filehandle = open(corpus, "r")

def clean(corpus):
    with open(corpus, 'r') as file:
        corpus = file.read()
        scrubbed_words = re.sub(r'[^a-zA-Z\s]', '', corpus).lower().split()
        return scrubbed_words

dicto = {}
histo_tuplo  = []
histo_listo = []

text = clean(corpus)

def dictogram(text):
    for word in text:           
        if word in dicto: 
            dicto[word] += 1
        else: 
            dicto[word] = 1

    return dicto

def listogram(text):
    for word in text:
        counter = [word, 0]

        for word2 in text:
            if word == word2:
                counter[1] += 1
        if counter not in histo_listo:
            histo_listo.append(counter)

    return histo_listo

def tuplogram():
    source = listogram(text)

    for item in source:
        histo_tuplo.append(tuple(item))

    return histo_tuplo

def unique():
    used_words = []
    unique_words = 1

    for word in clean(corpus):
        if word not in used_words:
            unique_words = unique_words + 1
            used_words.append(word)

    return 'There are ' + str(unique_words) + ' unique words in this list!'


def frequency(search):
    if search in dictogram(text):
        return 'The word ' + str(search) + ' occurs ' + str(dicto[search]) + ' times!'
    else:
        return 'Word does not occur'

if __name__ == '__main__':
    # print(clean(corpus))
    # print(histogram)
    for word in dictogram(text):
       print(word, dicto[word])

    # print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

    # print(unique())

    # print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

    # print(frequency(sys.argv[1]))

    print(dictogram(text))
    print(listogram(text))
    print(tuplogram())