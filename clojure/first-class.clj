;; the function as a 'first-class'

(defn my-func1
      "A demo of first-class"
      [d f]
      (f d))

(my-func1 "it's first-class!" println)
