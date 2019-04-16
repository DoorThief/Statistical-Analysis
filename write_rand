#!/bin/bash

help() {
	echo "Specify # of random data points
Usage:
	-o|--out	Specify output
	-s|--size	Size of dataset to generate
	-r|--range	How large the number a data point can be"
}

write() {
	while [[ $i -gt 0 ]]; do
		echo $(( 1 + $RANDOM % $r )) >> $o
		i=$(( $i - 1 ))
	done
}

if [[ -z $1 ]]; then
		help
		exit 1
	else
        while [[ $# -gt 0 ]]; do        # $# means total arguments
                case "$1" in
                        -o|--out)	o=$2	# Output file
			;;
			-s|--size)	i=$2	# Decrementor
			;;
			-r|--range)	r=$2	# Devisor
			;;
                        *)      echo "Error: $1 - is not a valid option"
				help
				exit 1
                        ;;
                esac
                shift 2
        done
	if [[ -f $o ]]; then
		read -p "$o exists! Remove it? (y/n) " yn
		if [[ $yn = y ]]; then rm $o; fi
	fi
	write
	echo $o
fi
