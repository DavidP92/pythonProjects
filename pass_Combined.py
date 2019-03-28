"""
So a few things you are gonna get learned on.

	THINGS DAVID WILL LEARN TODAY:
		1. All data is essentially numbers
		2. All chacters are numbers
		3. How to create a generator function to speed of unnecessary bs programs.
		4. Default values
		5. Type hinting
		6. Unpacking of lists
"""

from random import choice
import sys

# The * causes the generator to unpack into the list
# Unicode utf-8 @ https://www.w3schools.com/html/html_charset.asp
special_chars = [*range(33, 47 + 1)] + [*range(58, 64 + 1)] + [*range(91, 96 + 1)] + [*range(123, 126 + 1)]
numbers = [*range(48, 57 + 1)]
chars = [*range(65, 90 + 1)] + [*range(97, 122 + 1)]


def _pwd_gen(length: int = 24, special_char: bool = False):
    """
    The above arguments each have a specific format to follow for type hinting in python
        3.4+
        (VAL): (TYPE)

        A default value can be set as well

    This function is a generator which means that it will continue to give results until it is exhausted.
    """
    default_encoding = sys.getdefaultencoding()
    if 'utf-8' == default_encoding:
        all_chars = special_chars + numbers + chars
        while length:
            yield chr(choice(all_chars))
            length -= 1
    else:
        return "Encoding is incorrect: {} used need 'utf-8'".format(default_encoding)


def pwd_gen(length: int = 24, special_char: bool = False):
    return "".join(_pwd_gen(length, special_char))


"""
Now the above employs some of the same techniques that you used, that being having a static area to define the 
character sheet to be used. This can be overridden just by using the numbers directly. I will let you figure that out
as a test to gain more experience.
"""

"""
The above can be used to create a simple dictionary attack as well. Watch this
"""

# First let us import and store the 1000 most common words of english
from most_common import common as words
from random import choice

pick = choice(words)


def crack_pick():
    n_common = words.copy()
    for _word in n_common:
        if _word is pick:
            return True, _word


if __name__ == "__main__":
    print(pwd_gen())
    print(pick)
    print(crack_pick())
