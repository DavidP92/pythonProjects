from random import choice
import sys

# Unicode utf-8 @ https://www.w3schools.com/html/html_charset.asp
user = [ 'med', 'high']

special_chara = [*range(33, 47+1)]+[*range(58,64+1)]+[*range(91,96+1)]+[*range(123,126+1)]
numb = [*range(48,57+1)]
chars = [*range(65,90+1)]+[*range(97,122+1)]

def _med(length: int= 16, special_char: bool = False):

    default_encoding = sys.getdefaultencoding()
    if 'utf-8' == default_encoding:
        all_chars = numb + chars
        while length:
            yield chr(choice(all_chars))
            length -= 1
            
def _high(length: int = 28, special_char: bool = False):

    default_decoding = sys.getdefaultencoding()
    if 'utf-8' == default_decoding:
        all_chars1 = numb + chars + special_chara
        while length:
            yield chr(choice(all_chars1))
            length -= 1
    else:
        return"Encoding is incorrect: {} used need 'utf-8'".format(default_decoding)

def med(length: int = 10, special_char: bool = False):
        return"".join(_med(length,special_char))

def high(length: int = 20 ,special_char: bool= False):
        return"".join(_high(length,special_char))


    


if __name__ == "__main__":

    diff = input("Do you want your password to be med or high?\n")

    if diff == user[0]:
        print(med())

    if diff == user[1]:
        print(high())

