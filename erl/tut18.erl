-module(tut18).
-export([start/1,ping/2,pong/0]).

ping(0,Node)->
    {pong,Node} ! finished,
    io:format("ping finished ~n",[]);
ping(N,Node)->
    {pong,Node} ! {ping,self()},
    receive 
	pong ->
	    io:format("ping received pong ~n",[])
    end,
    ping(N-1,Node).

pong()->
    receive 
	finished -> 
	    io:format("pong finished~n",[]);
	{ping,Ping_PID}->
	    io:format("pong received~n",[]),
	    Ping_PID ! pong,
	    pong()
    end.

start(Node)->
    register(pong,spawn(tut18,pong,[])),
    spawn(Node,tut18,ping,[3,node()]).


