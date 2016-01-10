#!/bin/bash
./powerballcheck.py > results.txt
cat results.txt |grep "prize for ticket" |grep -v "\$0"
buff=0
for line in $(cat results.txt |grep "prize for ticket" |grep -v "\$0" |awk '{print $7}' |sed 's/\$//'); do 
	buff=$(expr $buff + $line); 
done

echo "Grand total winnings are \$$buff"
rm results.txt
