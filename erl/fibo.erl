-module(fibo).
-export([fibo_list/1]).


%% the nth fibo number.
fibo(0) ->
	1;
fibo(1) ->
	1;
fibo(N) ->
	fibo(N-1)+fibo(N-2).

%% reverse a list

reverse([Head|Rest]) ->
	[reverse(Rest)|Head].

	

%% first n fibo number.
fibo_list(0) ->
	[];

fibo_list(1)->
	[1];

fibo_list(2)->
	[1,1];

fibo_list(N)->
	reverse([fibo(N)|fibo_list(N-1)]).

	
	
	
