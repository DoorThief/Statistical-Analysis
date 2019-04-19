#!/usr/bin/python3

from math import sqrt

_n = 0			#n
_sum = 0	#sum
_avg = 0	#avg
_sd = 0		#std. deviation
_se = 0		#std. error
_ev = 0		#ev/H0
_score = 0	#score from z or t test
_test	= 'z'	#currenly only z-test supported
temp = 0	#temporary number for arithmatic evaluation

dataset = input("File containing dataset: ")	#User defined file {dataset}

with open(dataset,'r') as data:
	for line in data:
		_n += 1
		_sum += float(line)

	_avg = (_sum / _n)

	data.seek(0)
	for line in data:
		temp += ((float(line) - _avg)**2)

_sd = sqrt(temp / _n)
_se = _sd / sqrt(_n)

print('n: {},  Sum: {}, Avg: {}, Std. Deviation: {}, Std. Error: {}'.format(_n, _sum, round(_avg, 2), round(_sd,3), round(_se, 3)))
usrEV = input("Define an EV (Null hypothesis): ")
_ev = int(usrEV)

_score = (_avg - _ev) / sqrt(_n)

print('{}-test = {}'.format(_test, _score))
