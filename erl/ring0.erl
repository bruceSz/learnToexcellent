-module(ring0).
-export([start/3,createProcess/3,loop/1]).

start(M,N,Message)->
    Next_PID=createProcess(N-1,M,self()),
    loop_main(M,Next_PID,Message),
    Next_PID ! stop.


loop_main(1,Next_PID,Message)->
    Next_PID ! {self(),Message};
loop_main(M,Next_PID,Message)->
    Next_PID ! {self(),Message},
    loop_main(M-1,Next_PID,Message).
    
genAtom(N)->
    Temp = lists:concat([process,N]),
    list_to_atom(Temp).

createProcess(0,M,Pid0)->
    Pid0;
createProcess(N,M,Pid0)->
    PidN=genAtom(N),
    Next_PID = createProcess(N-1,M,Pid0),
    Current_PID = spawn(fun ()->loop(Next_PID)end),
    register(PidN,Current_PID),
    Current_PID.

loop(Next_PID)->
    receive 
	{From,Message}->
	    Next_PID ! Message,
	    loop(Next_PID);
	stop ->
	    io:format("~p received exit signal and exit!",[self()])
    end.
