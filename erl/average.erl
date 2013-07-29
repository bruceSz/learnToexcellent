-module(average).
-export([num]/1,sum/1,count_average/1]).
num([]) -> 0;
num([H|T])-> 1 + num(T).

sum([]) -> 0;
sum([H|T]) -> H + sum(T).

count_average([]) -> 0;
count_average(L)-> sum(L)/num(L)

