-module(tut4).
-export([list_length/1]).

list_length([]) ->
	0;
list_length([X]) ->
        1;
list_length([F|Rest]) ->
	list_length(F) +list_length(Rest).

