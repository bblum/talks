#!/bin/bash

while true; do
	echo -n "updating page count at "
	date
	./run.sh
	if [ "$?" = 0 ]; then
		./graph.py --out graph.png log.csv
		if [ "$?" = 0 ]; then
			mv graph.png /var/www/html/
		fi
	fi
	echo "(done)"
	sleep 5m
done
