package main
import "fmt"

func Map(f func(int) int, l []int) []int {
    j := make([]int,len(l))
	for k,v := range l {
		j[k]=f(v)
	    }
    return j
}
func MapStr(f func(string)string,l []string) []string {
	j := make([]string,len(l))
	for k,v := range l {
		j[k] = f(v)
	}
	return j
}
func main() {
	m := []int{1,3,4}
	m2 := []string{"1","2","3"}
	f := func(i int) int {
		return i*i
	}
// here we need more thought here.
	f2:= func(s* string) string {
		return s+"do it!"
	}
	fmt.Printf("%v",(MapStr(f,m)))
	//    fmt.Printf("%v",m)
}
