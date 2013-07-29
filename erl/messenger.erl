%%% Message passing utility.
%%% User interface:
%%% logon(Name)
%%%	One user at a time can log in from each Erlang node in the
%%%	system messenger: and choose a suitable Name. If the Name
%%%	is already logged in at another node or if someone else is
%%%     already logged in at the same node.login will be rejected
%%%      with a suitable error message.
%%% logoff()
%%%	logs off anybody at node.
%%% message(ToName,Message)
%%%	sends Message to ToName,Error Message if the user of this 
%%%	function is not logged on or if ToName, is not logged on at
%%%	any node.


%%% one node in the network of erlang nodes run a server which maintains
%%% data about the logged on users. The server is registered as "messenger"
%%% each node where there is a user logged on runs a client process
%%% registered
%%% as mess_client.

%%% Protocol between the client processes and the server
%%% ----------------------------------------------------
%%% To server: {ClientPid,logon,UserName}
%%% Reply {messenger,stop,user_exists_at_other_node} stops the client 
%%% Reply {messenger,logged_on} logon was successful.
%%% 
%%% To server:{ClientPid,logoff}
%%% Reply:{messenger,logged_off}
%%%
%%% To server:{ClientPid,message_to,ToName,Message} send a message
%%% Reply:{messenger,stop,you_are_not_logged_on} stops the client
%%% Reply:{messenger,receiver_not_found} no user with this name logged on
%%% Reply:{messenger,send} Message has been sent (but no guarantee)

%%% To client:{message_from,Name,Message},
%%% 
%%% Protocol between the "commands" and the client
%%%-----------------------------------------------------
%%% Started: messenger:client(Server_Node,Name)
%%% To client: logoff
%%% To client:{message_to,ToName,Message}
%%%
%%% Configuration: change the server_node() function to return the
%%% name of the node where the messenger server runs
%%% 
-module(messenger).
-export([start_server/0,server/1,logon/1,logoff/0,message/2,client/2]).

%%% Change the function below to return the name of the node where the
%%% messenger server runs
server_node()->
    messenger@localhost.

%%% This is the server process for the "messenger"
%%% the user list has the format [{ClientPid1,Name1},{ClientPid2,Name2},...]

server(User_List)->
    receive 
	{From,logon,Name}->
	    New_User_List=server_logon(From,Name,User_List),
	    server(New_User_List);
	{From,logoff}->
	    New_User_List=server_logoff(From,User_List),
	    server(New_User_List);
	{From,message_to,To,Message}->
	    server_transfer(From,To,Message,User_List),
	    io:format("list is now :~p~n",[User_List]),
	    server(User_List)
    end.
%%% start the server
start_server() ->
    register(messenger,spawn(messenger,server,[[]])).

%%% server adds a new user to the user list
server_logon(From,Name,User_List)->
    case lists:keymember(Name,2,User_List) of
	true ->
	    From ! {messenger,stop,user_exists_at_other_node}, % reject logon
	    User_List;
	false->
	    From ! {messenger,logged_on},
	    [{From,Name}|User_List] % add user to the list
    end.

%%% server delete a user from the user list.
server_logoff(From,User_List)->
    lists:keydelete(From,1,User_List).
	
%%% server transfer a message between user
server_transfer(From,To,Message,User_List) ->
    %% check that the user is logged on and who he is
    case lists:keysearch(From,1,User_List) of
	false ->
	    From ! {messenger,stop,you_are_not_logged_on};
	{value,{From,Name}} ->
	    server_transfer(From,Name,To,Message,User_List)
    end.

server_transfer(From,Name,To,Message,User_List)->
    case lists:keysearch(To,2,User_List) of
	false ->
	    From ! {messenger,receiver_not_found};
	{value,{ToPid,To}}->
	    ToPid ! {messenger_from,Name,Message},
	    From ! {messenger,sent}
    end.

%%% User commands
logon(Name)->
    case whereis(mess_client) of
	undefined ->
	    register(mess_client,spawn(messenger,client,[server_node(),Name]));
	_ -> already_logged_on
    end.
    
logoff() ->
    mess_client ! logoff.

message(ToName,Message)->
    case whereis(mess_client) of
	undefined ->
	    not_logged_on;
	_ ->
	    mess_client ! {message_to,ToName,Message},
	    ok
    end.
client(Server_Node,Name)->
    {messenger,Server_Node} ! {self(),logon,Name},
    await_result(),
    client(Server_Node).

client(Server_Node)->
    receive 
	logoff ->
	    {messenger,Server_Node} ! {self(),logoff},
	    exit(normal);
	{message_to,ToName,Message}->
	    {messenger,Server_Node} ! {self(),message_to,ToName,Message},
	    await_result();
	{message_from,FromName,Message}->
	    io:format("message from ~p :~p ~n",[FromName,Message])
    end,
    client(Server_Node).

%%% wait for a response from the server
await_result() ->
    receive 
	{messenger,stop,Why}->
	    io:format("~p~n",[Why]),
	    exit(normal);
	{messenger,What}->
	    io:format("~p~n",[What])
    end.
