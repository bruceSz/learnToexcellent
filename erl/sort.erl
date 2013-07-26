-module(sort).
-export([find_max/1,select_sort/1]).

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

select_sort(L)->
	do_select_sort(L,[]).

do_select_sort([],R)->
	R;
do_select_sort(L,R)->
	{Max,T}=find_max(L),	
	io:format("|~w|",[Max]),
	do_select_sort(T,[Max|R]).


	
	
