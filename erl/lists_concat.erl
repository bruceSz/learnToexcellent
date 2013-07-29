-module(lists_concat).
-export([concat/2,reverse/2,concatenate/2]).

%% reverse a list
reverse(L,[])->L;
reverse(L,[H|T])->reverse([H|L],T).

%% concatenate two list
concatenate(L1,L2)->concat(L1,reverse([],L2)).

concat(L,[])->L;
concat(L,[H|T])->concat([H|L],T).
