"""
File: hailstone.py
Name: You-Nong Huang
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    print('This program computes Hailstone sequences.')
    print()
    N = int(input('Enter a number: '))
    step = 0
    if N == 1:
        print('It took 0 step to reach 1.')
    else:
        while N != 1:
            if N % 2 == 0:
                print(N, 'is even, so I take half:', N//2)
                N = N // 2
                step = step + 1
            else:
                print(N, 'is odd, so I make 3n+1:', 3*N+1)
                N = 3 * N + 1
                step = step + 1
        print('It took',step,'steps to reach 1.')









###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
