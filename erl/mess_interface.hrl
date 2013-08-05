%%% ----file mess_interface.hrl----

%%% message from client to server received in server/1 function.
-record(logon,{client_pid,username}).
-record(message,{client_pid,to_name,message}).
%%% {'EXIT',ClientPid,Reason} (client terminated or unreachable.)

%%% messages from server to client,received in await_result/0 function
-record(abort_client,{message}).
%%% messages are:user_exists_at_other_node,
%%%		 you_are_not_logged_on

-record(server_reply,{message}).

%%% messages from server to client received in client/1 function
-record(message_from,{from_name,message}).
%%% messages from shell to client received in client/1 function
%%% spawn(mess_client,client,[server_node(),Name])
-record(message_to,{to_name,message}).


