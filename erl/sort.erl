-module(sort).
-export([find_max/1,select_sort/1]).

%%find max
%%assume the L is non empty.

do_find_max(Max,[])->
    Max;
do_find_max(Max,[H|T]) when Max<H ->
    do_find_max(H,T);
do_find_max(Max,[H|T]) when Max>=H ->
    do_find_max(Max,T).
    
%% find max
find_max(L)->
	H = hd(L),
	T = tl(L),
	do_find_max(H,T,[]).

do_find_max(Max,[],L)->
	{Max,L};

do_find_max(Max,[H|T],L) when Max>=H ->
	do_find_max(Max,T,[H|L]);

do_find_max(Max,[H|T],L) when Max<H ->
	do_find_max(H,T,[Max|L]).

%% select sort
select_sort(L)->
	do_select_sort(L,[]).

do_select_sort([],R)->
	R;
do_select_sort(L,R)->
	
	{Max,T}=find_max(L),	
	%io:format("|~w|",[Max]),
	do_select_sort(T,[Max|R]).

%% bubble sort
%% the bubble here switch max into list tail.

bubble_sort(L)->
    do_bubble_sort(L,[]).

do_bubble_sort([],R)->
    L;
do_bubbke_sort(L,R)->
    B = bubble(L),
    T = tail(B),
    Rest = delete(B,T),
    do_bubble_sort(Rest,[T|R]).
    
