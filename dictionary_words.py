import random
import sys

def make_sentence(words=1):

    file = open("words.txt", "r")
    random_words = file.read().split('\n')

    word_list = []

    while len(word_list) < words:
        word_list.append(random.choice(random_words))

    return(' '.join(word_list))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(make_sentence(int(sys.argv[1])))
    else:
        print(make_sentence())