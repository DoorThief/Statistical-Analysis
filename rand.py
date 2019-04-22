import random as r
import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='A random number set generator.')
parser.add_argument('-s', '--size', type=int,
                    help='Required: Specify the amount of random numbers to generate.')
parser.add_argument('-r', '--range', type=int,
                    help='Required: Specify how large a random number can be.')
args = parser.parse_args()
try:
	for x in range(args.size):
		print(r.randint(1,(int(args.range-1))))
except TypeError:
	parser.print_help()
