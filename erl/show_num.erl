-module(show_num).
-export([print/1,print/2,print_even/1,print_even/2]).

print(N)->
    io:format("Number:"),
    print(1,N)

print(N,N)->
    io:format("~p~n",[N]);
print(M,N)->
    io:format("~p~n",[M]);
    print(M+1,N).

    
print_even(N)->
    io:format("Even number:"),
    print_even(2,N).
    
print_even2(M,N) when M =>N ->
    print_even(N,N);
print_even2(M,N)->
    if
	M rem 2 =:= 1 ->
	    print_even2(M+1,N);
	true ->
	    io:format("~p~n",[M]),print_even2(M+2,N)
    end.

print_even(N,N)->
    if 
	N rem 2 =:= 0 ->
	    io:format("~p~n",[N]);
	N rem 2 =:= 1 ->
	    io:format("End~n")
    end;
print_even(M,N)->
    if 
	M rem 2 =:= 0 ->
	    io:format("~p~n",[M]),print_even(M+1,N);
	M rem 2 =:= 1 ->
	    print_even(M+1,N)
    end.
	
