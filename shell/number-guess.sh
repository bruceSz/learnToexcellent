#!/bin/sh
# number gussing game
biggest = 100
guess = 0
guesses = 0
number = $(($$ % $biggest))
while [ $guess -ne  $number ];do
    echo -n "guess? ";read answer
    if [ "$guess" -lt $answer ];then
	echo "... bigger!"
    elif [ "$guess" -gt $number ];then
	echo "... smaller!"
    fi
    guesses = $(($guesses + 1))
done
echo "right!! guessed $number in $guess guesses"
exit 0
