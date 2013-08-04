-module(cross_arith).
-export([add/1,add/2,element/1]).

element(1) -> 1;
element(N) -> element(N-1) + 1.

add(N) -> add(N,0).

add(1,Sum)-> Sum + 1;

add(N,Sum)->
    A = element(N),
    if 
	A rem 2 =:= 0 ->
	    add(N-1,Sum-element(N));
	A rem 2 =:= 1 ->
	    add(N-1,Sum+element(N))
    end.
    
