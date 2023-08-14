"""
File: similarity.py
Name: You Nong HUANG
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    Input a long sequence and a short sequence.
    We'll find out that the most similarity part of the short one in long one.
    """
    long_sequence = input('Please give me a DNA sequence to search: ')
    long_sequence = long_sequence.upper()
    short_sequence = input('What DNA sequence would you like to match? ')
    short_sequence = short_sequence.upper()
    count = 0
    max_count = 0
    match_s = ''
    best_match_s = ''
    for i in range(len(long_sequence)-len(short_sequence)+1):
        count = 0
        match_s = long_sequence[i:i+len(short_sequence)]
        for j in range(len(short_sequence)):
            ma = long_sequence[i+j]
            if ma == short_sequence[j]:
                count += 1
        if count > max_count:
            max_count = count
            best_match_s = match_s
    print('The best match is '+best_match_s)









    pass


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
