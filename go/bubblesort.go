package main
import "fmt"

func bubblesort(l []int) {
	for i:=len(l)-1 ; i > 0 ;i--  {
		for j:=0;j<i;j++ {
			if l[j+1] < l[j] {
				l[j],l[j+1]=l[j+1],l[j]
			}
		}
	}
}


func main() {
	n:= []int{5,-1,0,12,3,5}
	fmt.Printf("unsorted %v\n",n)
	bubblesort(n)
	fmt.Printf("sorted\n",n)
}