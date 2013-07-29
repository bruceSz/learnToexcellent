-module(list_length).
-export([flat_length/1]).

flat_length(List)->
	flat_length(List,0).

flat_length([H|T],N) when list(H)->
	flat_length(H,flat_length(T,N));
flat_length([H|T],N) ->
	flat_length(T,N+1);
flat_length([],N) ->
	N.
