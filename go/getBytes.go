package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
    str := "jfkdjfkecjswhflaejfkehfaiaehc";
    fmt.Printf("String %s\nLength:%d,Bunes:%d\n",str,
	       len([]byte(str)),utf8.RuneCount([]byte(str)))
}
