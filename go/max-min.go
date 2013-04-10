package main
import "fmt"

func max(l [] int) (max int) {
	max = l[0]
	for _,v := range l {
		if v > max  {
			max = v
		}
	}
	return // return has been declared.it is max
}

func compare(a int,b int,flag bool) (bigger bool) {
	if flag {
		if a > b {
			bigger = true
		}
		bigger = false
	}else {
		if a < b {
			bigger = true
		}
		bigger = false
	}
	return 
}

func max-min(l []int ,maxOrMin bool) (top int) {
	top = l[0]
	for _,v := range l {
		if compare(v,top,maxOrMin) {
			v = top
		}
	}
	return
}

func main() {
	print "end."
}