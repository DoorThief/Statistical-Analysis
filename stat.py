#!/usr/bin/python3
from math import sqrt

ds_n = 0	#n
ds_sum = 0	#sum
ds_avg = 0	#avg
ds_sd = 0	#std. deviation
ds_se = 0	#std. error
ds_score = 0	#score from z or t test
ds_test	= 'z'
temp = 0	#temporary number for arithmatic evaluation

dataset = input("File containing dataset: ")	#User defined file {dataset}
usrEV = input("Define an EV (Null hypothesis): ")
ev = int(usrEV)

with open(dataset,'r') as data:
	for line in data:
		ds_n = ds_n + 1
		try:
			ds_sum += float(line)
			temp = temp + ((float(line) - ev)**2 / ds_n)

		except ValueError:
			print('{} is not a number!'.format(line))

ds_avg = (ds_sum / ds_n)
ds_sd = sqrt(temp)
ds_se = ds_sd / sqrt(ds_n)

print('n: {},  Sum: {}, Avg: {}, Std. Deviation: {}, Std. Error: {}, {}-score: {}'.format(ds_n, ds_sum, round(ds_avg, 2), round(ds_sd,3), ds_se, ds_test, ds_score))
