from random import randint, choice

my_file = open("words.txt", "r")

lines = my_file.readlines()

rnd = randint(0, len(lines)-1)

print(lines[rnd])