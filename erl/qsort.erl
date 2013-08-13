-module(qsort).
-export([qsort/1]).

qsort([])->[];
qsort([Pivot|Rest])->
	{Smaller,Bigger} = split(Pivot,Rest),
	lists:append(qsort(Smaller),[Pivot|qsort(Bigger)]).

split(Pivot,L)->
	split(Pivot,L,[],[]).

split(Pivot,[],Smaller,Bigger)->
	{Smaller,Bigger};
split(Pivot,[H|T],Smaller,Bigger)->
	if
		H<Pivot ->
			split(Pivot,T,[H|Smaller],Bigger);
		H >=Pivot ->
			split(Pivot,T,Smaller,[H|Bigger])
	end.

		
