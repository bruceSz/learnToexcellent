package main
import "fmt"

func main() {
	ch := make(chan int)
	quit := make(chan bool)
	go shower(ch,quit)
	for {
		select{
		case j := <- ch:
			fmt.Printf("%d\n",j)
		case <-quit:
			break
		}
	}

}
func shower(c chan int, quit chan bool) {
	for i:=0;i<10;i++ {
		c <-i
	}
	quit <- false
}
