-module(test_func_clause).
-export([test_clause_match_seq/1]).

test_clause_match_seq({first,second}) ->
	io:format("the first second sequance.");
test_clause_match_seq({first,T}) ->
	io:format("the first third sequance.").
