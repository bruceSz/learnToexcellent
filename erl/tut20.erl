-module(tut20).
-export([start/1,ping/2,pong/2]).

ping(N,Pong_Pid)->
    link(Pong_Pid),
    ping1(N,Pong_Pid).

ping1(0,_)->
    exit(ping);
ping1(N,Pong_Pid)->
    Pong_Pid ! {ping,self()},
    receive 
	pong ->
	    io:format("Ping received pong ~n",[])
    end,
    ping1(N-1,Pong_Pid).

pong() ->
    receive 
	{ping,Ping_PID}->
	    io:format("pong received ping ~n",[]),
		Ping_PID ! pong,
		pong()
    end.

start(Ping_Node)->
    PongPID = spawn(tut20,pong,[]),
    spawn(Ping_Node,tut20,ping,[3,PongPID]).
