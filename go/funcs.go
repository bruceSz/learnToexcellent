package main
import "fmt"

func main() {
	p2 := plusA(2)
	fmt.Printf("%v\n",p2(2))
	p3 := plusA(3)
	fmt.Printf("%v\n",p3(2))
}
func plusA(a int) func(int) int {
	return func(x int) int { return x + a}
}
