"""
File: quadratic_solver.py
Name: You-Nong Huang
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	To solver the roots of the math question ax^2+bx+c.
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	# D means discriminant.
	D = d(a, b, c)
	if D > 0:
		roots = Two_roots(a, b, c)
		print('Two roots:', roots)
	elif D == 0:
		root = One_root(a, b)
		print('One root:', root)
	elif D < 0:
		print('No real roots')


# For b^2-4ac = 0, one root
def One_root(a, b):
	return -b/(2*a)


# For b^2-4ac > 0, two roots
def Two_roots(a, b, c):
	return (-b+math.sqrt(b*b-4*a*c))/(2*a), (-b-math.sqrt(b*b-4*a*c))/(2*a)


# Count b^2-4ac, discriminant
def d(a,b,c):
	return b*b-4*a*c


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
