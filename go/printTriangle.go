package main
import "fmt"

func main() {
     str := "A"
     for i:=0;i<100;{
     	 fmt.Printf("%s\n",str)
	 str = str + "A"
	 i += len(str)
     }
}    