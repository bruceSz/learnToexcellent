-module(tut19).
-export([start_ping/1,start_pong/0,ping/2,pong/0]).

ping(0,Node)->
    io:format("ping finished ~n",[]);
ping(N,Node)->
    {pong,Node} ! {ping,self()},
    receive 
	pong ->
	    io:format("ping received pong ~n",[])
    end,
    ping(N-1,Node).

pong() ->
    receive 
	{ping,Ping_PID}->
	    io:format("Pong received ping ~n",[]),
	    Ping_PID ! pong,
	    pong()
    after 5000 ->
	io:format("pong timed out~n",[])
    end.

start_ping(Node)->
    spawn(tut19,ping,[3,Node]).
start_pong()->
    register(pong,spawn(tut19,pong,[])).
    
