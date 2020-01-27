from random import randint, choice

quotes = ('"The oppressed are allowed once every few years to decide which particular representatives of the oppressing class are to represent and repress them."', '"Surround yourself with people who make you happy. People who make you laugh, who help you when you’re in need. People who genuinely care. They are the ones worth keeping in your life. Everyone else is just passing through."','"The last capitalist we hang shall be the one who sold us the rope."')


def random_quote():
    rnd = randint(0, len(quotes)-1)
    return quotes[rnd]

if __name__ == '__main__':
    print(random_quote())