;; the function as a 'first-class' 2

(defn func-a [s] (str "Func A: " s))

(defn func-b [s] (str "Func B:" s))

(defn my-func2
      "Another demo of first-class"
      [n]
      (cond
	(> n 0) func-a
	:else func-b))


(println ((my-func2 0) "my-first-class"))
