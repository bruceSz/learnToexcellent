package main
import (
	"fmt"
	"os/exec"
	"sort"
	"strconv"
	"strings"
	)

func main() {
	ps := exec.Command("ps","-e","-opid,ppid,comm")
	output,_ :=ps.Output()
	child :=make(map[int][]int)

	for i,s := range strings.Split(string(output),"\n") {
		if i == 0 {continue}
		if len(s) == 0 {continue}
		f := strings.Fields(s)
		fpp,_ :=strconv.Atoi(f[1])
		fp,_ := strconv.Atoi(f[0])
		child[fpp]=append(child[fpp],fp)
	}
	schild := make([]int ,len(child))
	i:=0
	for k,_:=range child {schild[i]=k;i++}
	sort.Ints(schild)
	for _,ppid := range schild {
		fmt.Printf("pid %d has %d child",ppid,len(child[ppid]))
		if len(child[ppid]) == 1{
			fmt.Printf(":%v\n",child[ppid])
			continue
		}
		fmt.Printf("ren: %v\n",child[ppid])
	}
}

