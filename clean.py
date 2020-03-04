import re
def clean(corpus):
    with open(corpus, 'r') as file:
        corpus = file.read()
        scrubbed_words = re.sub(r'[^a-zA-Z\s]', '', corpus).lower().split()
        return scrubbed_words