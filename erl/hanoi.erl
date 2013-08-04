-module(hanoi).
-export([hanoi/1,move/4]).

hanoi(N)-> move(N,a,b,c).

move(1,A,B,C)->
    io:format("Move disk 1  from ~p to ~p.~n",[A,C]);
move(N,A,B,C)->
    move(N-1,A,C,B),
    io:format("Move disk ~p from ~p to ~p~n",[N,A,C]),
    move(N-1,B,A,C).
    
    
