#!/usr/bin/python3

from math import sqrt

#variable sanitation (if var += then previously defined/unknown value could leak into current session.)
_n = 0		#n	(+=)
_sum = 0	#sum	(+=)
_test = 'z'	#currenly only z-test supported
_temp = 0	#temporary number for arithmatic evaluation	(+=)

dataset = input("File containing dataset: ")	#prompts user for dataset file

with open(dataset,'r') as data:		#With data (aka. the handler for open(dataset)
	for line in data:		#For iterate each line in data (every line in dataset)
		_n += 1			#Increment _n by 1
		_sum += float(line)	#Adds line (in float form ie. 1.0000) to _sum

	_avg = (_sum / _n)	#avg = sum / n

	data.seek(0)		#In preperation to use another for each line, we use seek(0) to go back to top of file
	for line in data:	##For iterate each line in data (every line in dataset)
		_temp += ((float(line) - _avg)**2)	#subtract line by avg, then square and add result to _temp

_sd = sqrt(_temp / _n)	#sd = square root of (_temp / n)
_se = _sd / sqrt(_n)	#se = se / square root of n

print('n: {},  Sum: {}, Avg: {}, Std. Deviation: {}, Std. Error: {}'.format(_n, _sum, round(_avg, 2), round(_sd,3), round(_se, 3))) #Prints results using formatter and {} as placeholders. Round is used to round... duh.
usrEV = input("Define an EV (Null hypothesis): ")	#prompts user to define ev
_ev = float(usrEV)	#sanitation: usr inputs strings, must convert to a float

_score = (_avg - _ev) / sqrt(_n)	#z score = difference of avg and ev, divided by square root of n

print('{}-test = {}'.format(_test, _score))	#prints z-test = score
