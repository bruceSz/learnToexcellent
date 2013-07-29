-module(tut17).
-export([start_ping/1,start_pong/0]).

ping(0,Node)->
    {pong,Node} ! finished,
    io:format("ping finished~n",[]);

ping(N,Node)->
    % assume default pong name is "pong". 
    {pong,Node} ! {ping,self()},
    receive 
	pong ->
	    io:format("ping received pong ~n",[])
    end,
    ping(N-1,Node).

pong()->
    receive
	finished ->
	    io:format("pong finished ~n",[]);
	{ping,Ping_PID} ->
	    io:format("pong received ping ~n",[]),
	    Ping_PID ! pong,
	    pong()
    end.

start_pong()->
    register(pong,spawn(tut16,pong,[])).

start_ping(Node)->
    ping(3,Node).
    
