"""
File: anagram.py
Name: Noah Huang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global Variable
dictionary = []


def main():
    """
    TODO:
    """
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    read_dictionary()
    while True:
        word = input("Find anagrams for: ")
        start = time.time()
        if word == EXIT:
            break
        find_anagrams(word)
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    global dictionary
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            dictionary.append(word)


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    global dictionary
    current_s = ''
    ans_lst = []
    print("Searching...")
    find_anagrams_helper(s, current_s, ans_lst, dictionary)
    print(len(ans_lst), "anagrams: ", ans_lst)


def find_anagrams_helper(s, current_s, ans_lst, dictionary_list):
    if len(s) == 0:
        if current_s not in ans_lst and current_s in dictionary_list:
            ans_lst.append(current_s)
            print("Found: ", current_s)
            print("Searching...")
    else:
        for i in range(len(s)):
            # choose
            letter = s[i]
            current_s += letter
            s = s[:i] + s[i+1:]

            # Explore
            if has_prefix(current_s):
                find_anagrams_helper(s, current_s, ans_lst, dictionary_list)

            # Un-choose
            current_s = current_s[:-1]
            s = s[:i] + letter + s[i:]


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    global dictionary
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
