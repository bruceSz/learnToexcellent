-module(sort).
-export([select_sort/1]).
%% find max
find_max(L)->
	H = hd(L),
	T = tl(L),

select_sort(L)->
	H = hd(L),
	T = tl(L),
	select_sort(L,[]).

select_sort(L,Result)->
	
