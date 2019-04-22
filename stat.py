#!/usr/bin/python3
#Author: Nicholas Martin
#Description: Given a dataset via file, the script with calulate n, sum, mean, standard deviation & error, and perform a z-test of user defined expected value derived from null hypothesis.
#Github repo: https://github.com/DoorThief/Statistic-Analysis

from math import sqrt
from sys import argv
							#variable sanitation (if var += then previously defined/unknown value could leak into current session.)
_n = 0							#n	(+=)
_sum = 0						#sum	(+=)
_temp = 0						#temporary number for arithmatic evaluation	(+=)

try:
        dataset = argv[1]                               #try to use first argument as file
except IndexError:					#on error: IndexError - That means no arguments were proved
        dataset = input("File containing dataset: ")    #prompts user for dataset file

with open(dataset,'r') as data:				#With data (aka. the handler for open(dataset)
	for line in data:				#For iterate each line in data (every line in dataset)
		_n += 1					#Increment _n by 1
		_sum += float(line)			#Adds line (in float form ie. 1.0000) to _sum

	_avg = (_sum / _n)				#avg = sum / n

	data.seek(0)					#In preperation to use another for each line, we use seek(0) to go back to top of file
	for line in data:				#For iterate each line in data (every line in dataset)
		_temp += ((float(line) - _avg)**2)	#subtract line by avg, then square and add result to _temp

_sd = sqrt(_temp / _n)					#sd = square root of (_temp / n)
if _n < 30:
	_test = 't'
	_sdp = _sd * sqrt(_n/(_n-1))
	_sep = _sdp / sqrt(_n)
	print('n: {},  Sum: {}, Avg: {}, Std. Deviation+: {}, Std. Error+: {}'.format(_n, _sum, round(_avg, 2), round(_sdp,3), round(_sep, 3))) #Prints results using formatter and {} as placeholders. Round is used to round... duh.
else:
	_test = 'z'
	_se = _sd / sqrt(_n)				#se = se / square root of n
	print('n: {},  Sum: {}, Avg: {}, Std. Deviation: {}, Std. Error: {}'.format(_n, _sum, round(_avg, 2), round(_sd,3), round(_se, 3))) #Prints results using formatter and {} as placeholders. Round is used to round... duh.

usrEV = input("Define an EV (Null hypothesis): ")	#prompts user to define ev
_ev = float(usrEV)					#sanitation: usr inputs strings, must convert to a float

if _test == 'z':
	_score = (_avg - _ev) * _se			#z score = difference of avg and ev, mutiplied by se
elif _test == 't':
	_score = (_avg - _ev) / _sep

print('{}-test = {}'.format(_test, round(_score,3)))	#prints z-test = score (rounded to 3rd decimal)
