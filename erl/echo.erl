-module(echo).
-export([start/0,loop/0]).

start() ->
	spawn(echo , loop,[]).

%% message box's max length,it will delete unmatched message?
loop() -> 
	receive
		{From,Message} ->
			io:format("recieved message: ~w~n",[Message]),
			From ! Message,
			loop()
	end.
