from math import sqrt
import argparse

parser = argparse.ArgumentParser(description='A rudimentary statistical analysis program.')
parser.add_argument('-f1', '--file1', type=str,
	help='Required: Specify file')
parser.add_argument('-f2', '--file2', type=str,
	help='Optional: Specify file')
args = parser.parse_args()

def get_math(dataset):

	n = 0
	sum = 0
	temp = 0
	try:
		with open(dataset,'r') as data:
			for line in data:
				n += 1
				sum += float(line)

			avg = (sum / n)
			get_math.avg = avg

			data.seek(0)
			for line in data:
				temp += ((float(line) - avg)**2)
	except:
		parser.print_help()
		exit(1)

	sd = sqrt(temp / n)
	if n < 30:
		test = 't'
		get_math.test = test
		sdp = sd * sqrt(n/(n-1))
		sep = sdp / sqrt(n)
		get_math.sep = sep
		print('n: {},  Sum: {}, Avg: {}, Std. Deviation+: {}, Std. Error+: {}'.format(n, sum, round(avg, 2), round(sdp,3), round(sep, 3)))
	else:
		test = 'z'
		get_math.test = test
		se = sd / sqrt(n)
		get_math.se = se
		print('n: {},  Sum: {}, Avg: {}, Std. Deviation: {}, Std. Error: {}'.format(n, sum, round(avg, 2), round(sd,3), round(se, 3)))

if args.file1 and args.file2:
	try:
		get_math(args.file1)
		if get_math.test == 'z':
			f1_avg =  get_math.avg
			f1_se = get_math.se
		else:
			print('Error: Sample size too small.')
			exit(0)
		get_math(args.file2)
		if get_math.test == 'z':
			f2_avg =  get_math.avg
			f2_se = get_math.se
		else:
			print('Error: Sample size too small.')
			exit(0)
		z_avgdif = f1_avg - f2_avg
		z_sedif = sqrt(f1_se**2 + f2_se**2)
		print('Null hypothesis for 2 Sample Z-Test is usually: "There is no difference ie. EV = 0"')
		ev = input("Define an EV: ")
		z = (z_avgdif - float(ev)) / z_sedif
		print('2 Sample Z-Test score: {}'.format(round(z, 3)))
	except:
		print('Error: Cannot use 2 Sample Z-Test.')
		exit(1)
else:
	get_math(args.file1)
	usrEV = input("Define an EV (Null hypothesis): ")
	ev = float(usrEV)
	test = get_math.test
	avg = get_math.avg
	if test == 'z':
		se = get_math.se
		score = (avg - ev) * se
	elif test == 't':
		sep = get_math.sep
		score = (avg - ev) / sep

	print('{}-test = {}'.format(test, round(score,3)))
