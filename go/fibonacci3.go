package main
import "fmt"


func fib() <-chan int {
	out := make(chan int,1)
	a := make(chan int ,1)
	b := make(chan int,1)
	go func () {
		out <- 0
		out <- 1
		a <- 0
		b <- 1
		for {
			x:= <-a
			y:= <-b
			out <- (x+y)
			a<-y
			b<-(x+y)
		}
	}()
	return out
}

func main() {
	x := fib()
	for i := 0;i<10;i++ {
		fmt.Println(<-x)
	}
}