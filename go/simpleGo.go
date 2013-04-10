package main
import (
	"fmt"
	"time"
)
var c chan int

func ready(w string, sec int) {
	time.Sleep(time.Duration(sec)*time.Second)
	fmt.Println(w,"is ready!")
	if w == "tea" {
		c<-1
		return 
	}
//	c <- 2
}
func main() {
	c = make(chan int)
	
	go ready("tea" ,1)
	go ready("coffee",2)
	fmt.Println("i'am waiting")
	fmt.Println(<-c)
	fmt.Println(<-c)
//	time.Sleep(5*time.Second)
}