"""
File: weather_master.py
Name: You-Nong Huang
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -100

def main():
	"""
	Calculate and analysis the temperature which is input to the python.
	"""
	print('stanCode \"Weather Master 4.0\"!')
	data = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
	if data == EXIT:
		print('No temperatures were entered.')
	else:
		maximum = data
		minimum = data
		# The sum of the input data.
		temperature = data
		# The number of times input data.
		days = 1
		# The number of the days of the temperature down 16 degree C
		cold = 0
		if data < 16:
			cold = cold + 1
		while True:
			data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			if data == EXIT:
				break
			temperature = temperature + data
			days = days + 1
			if data < 16:
				cold = cold + 1
			if data > maximum:
				maximum = data
			elif data < minimum:
				minimum = data
		average = temperature / days
		print('Highest temperature =', maximum)
		print('Lowest temperature =', minimum)
		print('Average = ', average)
		print(cold, 'cold day(s)')







###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
