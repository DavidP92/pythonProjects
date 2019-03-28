from random import choice
import datetime
import sys
special_chars = [*range(33, 47 + 1)] + [*range(58, 64 + 1)] + [*range(91, 96 + 1)] + [*range(123, 126 + 1)]
numb = [*range(48, 57 + 1)]
chars = [*range(65, 90 + 1)] + [*range(97, 122 + 1)]
all_chars = chars

def _med(length: int= 16, special_char: bool = False):

    default_encoding = sys.getdefaultencoding()
    if 'utf-8' == default_encoding:
        all_chars = numb + chars
        while length:
            yield chr(choice(all_chars))
            length -= 1
    else:
        return"Encoding is incorrect: {} used need 'utf-8'".format(default_decoding)

def med(length: int = 2, special_char: bool = False):
        return"".join(_med(length,special_char))

def gen_guess(typeset: list):
    ts = typeset
    while True:
        yield chr(choice(ts))
        print(ts)


def crack(pwd: int, length: int, typeset: list):
    # pwd given is hashed
    start = datetime.datetime.now()
    guess = 1
    guesser = gen_guess(typeset)
    next(guesser)

    while hash(guess) != pwd:
        guess = "".join([next(guesser) for _ in range(length)])

    return guess, (datetime.datetime.now() - start).seconds


if __name__ == "__main__":
    pwd = hash(med())
    print(med())
    print(crack(hash(pwd), 2, all_chars))
