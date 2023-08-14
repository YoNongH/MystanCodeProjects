"""
File: complement.py
Name: You Nong HUANG
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    Turn the input DNA sequence to complement DNA sequence.
    """
    dna = input('DNA: ')
    dna = dna.upper()
    new_dna = build_complement(dna)
    print(new_dna)

def build_complement(dna):
    ans = ''
    for base in dna:
        # The whole bases in the DNA need to be change, so here we use <for each loop>.
        if base == 'C':
            ans += 'G'
        elif base == 'G':
            ans += 'C'
        elif base == 'A':
            ans += 'T'
        elif base == 'T':
            ans += 'A'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
