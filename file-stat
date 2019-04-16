#!/bin/bash
file=$1

#Func
getb() {	#n sum avg
if [[ -z $file ]]; then
	echo "Usage: <filename>"
	exit 1
elif [[ -f $file  ]]; then
	n=0
	sum=0
	for line in $(cat $file); do
		sum=$(echo "$sum + $line" | bc -l)
		n=$(($n+1))
	done
	avg=$(echo "$sum / $n" | bc -l)
else
	echo "Error: $file - Is not a file"
	exit -1
fi
}

getsd() {
sd=0
	for i in $(cat $file); do
		sd=$(echo "$sd + ($i - $avg)^2" | bc -l)
	done
	sd=$(echo "sqrt($sd / $n)" | bc -l)
}

getse() {
se=0
	if [[ $n -ge 30 ]]; then
		se=$(echo "$sd / sqrt($n)" | bc -l)
	elif [[ $n -lt 30 ]]; then
		sdp=$(echo "$sd * sqrt($n / ($n - 1))" | bc -l)
		sep=$(echo "$sdp / sqrt($n)" | bc -l)
	fi
}

ttest() {
	score=$(echo "($avg - $ev) / $sep" | bc -l)
}

ztest() {
	score=$(echo "($avg - $ev) * $se" | bc -l)
}

getb
getsd
getse

echo "Dataset:"; column $file

if [[ $n -lt 30 ]]; then
	echo "n: $n, Avg: "$(printf "%0.2f" $avg)", Std. SD+: "$(printf "%0.3f" $sdp)", Std. Err+: "$(printf "%0.3f" $sep)", DOF: "$(($n - 1))
elif [[ $n -ge 30  ]]; then
	echo "n: $n, Avg: "$(printf "%0.2f" $avg)", Std. SD: "$(printf "%0.3f" $sd)", Std. Err: "$(printf "%0.3f" $se)
fi

ev=0
while [ 1 ]; do
read -p "Expected Value (aka Null Hypothesis): " ev
if [[ $ev ]]; then
	if [[ $n -lt 30 ]]; then
		m="t"
		ttest
	else
		m="z"
		ztest
	fi
	echo "$m-test: "$(printf "%0.3f" $score)
else
	echo "No input, try again."
fi
done
