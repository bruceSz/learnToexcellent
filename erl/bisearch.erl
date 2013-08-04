-module(bisearch).
-export([bi_search/2,getMiddle/1,value/2,len/1]).

len([])->0;
len([N])->1+len(N-1).

head([])->null;
head([H|T])->H.

value(0,L)->
    if 
	L =:= [] ->
	    false;
	L =/= [] ->
	    head(L)
    end;
value(N,[H|T])->value(N-1,T).

getMiddle([H])->H;
getMiddle(L)->
    Loc=len(L) div 2,
    value(Loc,L).
    
bi_search(L,X)->
    Middle = getMiddle(L)
    if 
	Middle =:= false ->
	    false;
	Middle =:=X ->
	    true;
	Middle < X ->
	    Left = [E|E<-L,E>Middle],
	    bi_search(Left,X);
	Middle > X ->
	    Right = [E|E<-L,E<Middle],
	    bi_search(Right,X)
    end.

	

