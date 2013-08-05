-module(mess_client).
-export([client/2]).

-include("mess_interface.hrl").

client(Server_Node,Name)->
    {messenger,Server_Node} ! #logon(client_pid=self(),username=Name),
    await_result(),
    client(Server_Node).

client(Server_Node)->
    receive 
	logoff ->
	    exit(normal);
	#message_to{to_name=ToName,message=Message}->
	    {messenger,Server_Node} !
		#message{client_pid=self(),to_name=ToName,
		message=Message},
	{message_from,FromName,Message} ->
	    io:format("Message from ~p:~p~n",[FromName,Message])
	end,
	client(Server_Node).

