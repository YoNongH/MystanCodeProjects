"""
File: caesar.py
Name: You Nong HUANG
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Decrypt input secret codes.
    """
    number = int(input('Secret number: '))
    code = input('What\'s the ciphered string? ')
    code = code.upper()
    new_alphabet = ALPHABET[len(ALPHABET)-number:]
    new_alphabet = new_alphabet + ALPHABET[:len(ALPHABET)-number]
    answer = ''
    for i in range(len(code)):
        if code[i].isalpha():
            if new_alphabet.find(code[i]) != -1:
                aaa = new_alphabet.find(code[i])
                # aaa is the index of the every letter of the in put code in the new_alphabet
                bbb = ALPHABET[aaa]
                # bbb is the letter which aaa means in the ALPHABET
                answer = answer + bbb
        else:
            answer += code[i]
            # The not word will not be change
    print('The deciphered string is: '+answer)



#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
