import re

corpus = "paragraph.txt"
filehandle = open(corpus, "r")

def clean(corpus):
    with open(corpus, 'r') as file:
        corpus = file.read()
        scrubbed_words = re.sub(r'[^a-zA-Z\s]', '', corpus).lower().split()
        return scrubbed_words

histogram = {}

for word in clean(corpus):           
    if word in histogram: 
        histogram[word] += 1
    else: 
        histogram[word] = 1

if __name__ == '__main__':
    # print(clean(corpus))
    # print(histogram)
    for word in histogram:
        print(word, histogram[word])