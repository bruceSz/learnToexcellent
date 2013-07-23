-module(tut15).
-export([start/0,ping/2,pong/0]).

ping(0,Pong_PID)->
    Pong_PID ! finished,
    io:format("ping finished ~n",[]);
ping(N,Pong_PID)->
    Pong_PID !{ping,self()},
	receive
	    pong ->
		io:format("Ping received pong ~n",[])
	end,
	ping(N-1,Pong_PID).

pong() ->
    receive
	finished ->
	    io:format("Pong finished ~n",[]).

