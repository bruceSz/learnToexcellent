package main
 
import "fmt"

func main() {
     i := 0
 
I:
	fmt.Print(i,"\n")
	i++
	if i < 10 {
	   goto I
	}
}