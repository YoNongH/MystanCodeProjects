"""
File: largest_digit.py
Name: Noah Huang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	if n > 0:
		return helper(n, 0)
	return helper(-n, 0)


def helper(n, small_one):
	if n == 0:
		return small_one
	else:
		num = n % 10
		if num > small_one:
			small_one = num
		return helper(n//10, small_one)


if __name__ == '__main__':
	main()
