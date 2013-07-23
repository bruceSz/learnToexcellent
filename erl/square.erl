-module(square).
-export([sum_square/1]).

compute_square(X) -> X * X.

sum_square(1) -> 1;
sum_square(N) ->
    compute_square(N) + sum_square(N-1).
