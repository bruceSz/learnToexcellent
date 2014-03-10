
(println (reduce + (filter divisible-by-3-5? (range 1000))))