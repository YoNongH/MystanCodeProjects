"""
File: boggle.py
Name:
----------------------------------------
This program simulates a classic game, boggle.
In the beginning, we allow users to input the
combination of sixteen letters (4x4). Then,
we will find out all the answers recursively.
During the process of searching, as soon as a
word is found, it will print "Found: 'word'"
in the Python console. After finding out all
the possible answers, this program will show
how long the searching process is and terminate
the program.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    """
    This program simulates the boggle game. First, user has to input the
    4x4 combination of letters as the base of game. Next, the program
    will start to look for all the possible answers in the base. While
    searching, it will let user know the words which have been found at
    the present by printing 'Found: word' in the Python console. The program
    also calculates the time needed by the searching process, and show the
    time right after the possible words are found. At the same time, print
    how many words exist in this boggle game. Notice that if the input by
    the user does not meet the requirement, the program will be terminated
    right away.
    """
    letter_d = {}
    letter_set = set()
    if not store_input(letter_d, letter_set):  # for illegal input situation
        return
    start = time.time()
    d = read_dictionary(letter_set)
    word_list = []
    for i in range(4):  # loop over the sixteen letters by their coordinates
        for j in range(4):
            row = i
            col = j
            word_found = letter_d[(row, col)]  # first letter of a word
            find_words(row, col, word_found, d, letter_d, word_list, [(row, col)])
    print('There are', len(word_list), 'words in total.')
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_words(row, col, word_found, d, letter_d, word_list, used_coordinate):
    """
    This function will recursively find out all the answers of boggle by checking
    all the possible combination of words. The recursion skill, early-stopping,
    back-tracking, and the nearest neighbors algorithm are adopted in this process.
    Here gives some descriptions below,

    1) recursion: exploring all the possible combination of the letters
    2) early-stopping: prevent unnecessary exploration by checking if the sub_s is
                       possible to turn into a real word
    3) back-tracking: go back to the previous letter combination after meeting the
                      base case
    4) nearest neighbors algo: nested for loop is used to loop over the eight neighbors
                               of the center letter

    :param row: int, the row coordinate of current center letter
    :param col: int, the column coordinate of current center letter
    :param word_found: str, storing the current combination of letters
    :param d: dict, storing the possible words and will be looked up
    :param letter_d: dict, storing the letter combination input by user
    :param word_list: lst, storing the words which have been found
    :param used_coordinate: lst, storing the coordinates that have been explored
    """
    if len(word_found) >= 4:  # base case
        if word_found in d[word_found[0]] and word_found not in word_list:
            word_list.append(word_found)
            print('Found \"' + word_found + '\"')
    for i in range(-1, 2):  # nearest neighbors algorithm
        for j in range(-1, 2):
            new_row = row + i  # re-assign the coordinate
            new_col = col + j
            # choose
            if (new_row, new_col) not in used_coordinate:
                if 0 <= new_row <= 3 and 0 <= new_col <= 3:
                    word_found += letter_d[(new_row, new_col)]
                    used_coordinate.append((new_row, new_col))
                    # explore
                    if has_prefix(word_found, d):  # early-stopping
                        find_words(new_row, new_col, word_found, d, letter_d, word_list, used_coordinate)
                    # un-choose
                    used_coordinate.pop()  # back-tracking
                    word_found = word_found[:len(word_found) - 1]


def store_input(letter_d, letter_set):
    """
    The function will let user to input sixteen letters in the form of 4x4 grid,
    and the letters and their coordinates on the 4x4 gird will be stored in a
    dictionary. The dict will look like {(row, col): 'letter'}. Additionally, a
    set will be prepared to store the letters, and look like {'letter'}.

    :param letter_d: dict, storing the letters input by user and their coordinates
    :param letter_set: set, storing the letters input by user
    :return None/True: None is for the situations of illegal input, and if there is
                       no illegal input, then return True.
    """
    for i in range(4):
        # case insensitive, remove '\n', get the letters from the row
        data = input(str(i+1) + ' row of letters: ').lower().strip().split(' ')
        if len(data) != 4:
            print('Illegal input')
            return
        for ch in data:
            if len(ch) != 1:  # make only a letter
                print('Illegal input')
                return
        for j in range(4):
            letter_set.add(data[j])
            letter_d[(i, j)] = data[j]  # (row, col)
    return True


def read_dictionary(letter_set):
    """
    This function reads file "dictionary.txt" stored in FILE and there are
    several procedures will be followed to filter the words in file, and finally
    a dictionary will be made.

    1) check whether the words start with a letter that exists in letter_set.
    2) check the length of the words, the maximum length is 16 (4x4), and the
       minimum length is 4.
    3) classify the words with their first letters, the first letter will be the
       key in d, and the value will be the words which are stored in a set.

    Thus, the dictionary will look like {'first letter': {words}}.

    :param letter_set: set, storing the letters input by user
    :return d: dict, storing the possible words from the file, and will be looked up
    """
    d = {}
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()  # Remove '\n'
            if line[0] in letter_set:
                if 16 >= len(line) >= 4:
                    if line[0] in d:
                        d[line[0]].add(line)
                    else:
                        d[line[0]] = set(line)
    return d


def has_prefix(sub_s, d):
    """
    The function is created to prune the recursion, find_words() by checking whether
    the current combination of letters is possible to turn into a real word by the
    following exploration. If we find that there is a real word starts with the sub_s
    at the present, then return True. If we look up all the real words in dictionary,
    still cannot find a word starts with the sub_s, then return False.

    :param sub_s: str, a substring that is constructed by neighboring letters on a
                  4x4 square grid
    :param d: dict, a dict that storing the possible words and will be looked up
    :return True/False: bool, if there is any words with prefix stored in sub_s
    """
    for word in d[sub_s[0]]:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
