-module(my_lists).
-export([create_list/1]).

create_list(N)->
    if
	N=<0 ->
	    [];
	true ->
	    do_create_list(N,[])
    end.

do_create_list(0,R)->
    R;
do_create_list(N,R)->
    do_create_list(N-1,[N|R]).
    
