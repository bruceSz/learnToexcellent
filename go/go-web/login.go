package main
import (
	"fmt"
	"html/template"
	"log"
	"net/http"
	"strings"
	"io"
	"strconv"
	"md5"
	"time"
	)
func sayhelloName(w http.ResponseWriter,r *http.Request) {
	r.ParseForm()
	fmt.Println(r.Form)
	fmt.Println("path",r.URL.Path)
	fmt.Println("scheme",r.URL.Scheme)
	fmt.Println(r.Form["url_long"])
	for k,v := range r.Form {
		fmt.Println("key:",k)
		fmt.Println("val:",strings.Join(v,""))
	}
	fmt.Println(w,"Hello astaxie!")
}
func login(w http.ResponseWriter,r *http.Request) {
	fmt.Println("method:",r.Method)
	if r.Method == "GET" {
		t,_ := template.ParseFiles("login.gtpl")
		t.Execute(w,nil)
	} else {
		fmt.Println("this is good")
		r.ParseForm(
			)
		fmt.Println("username:",r.Form["username"])
		fmt.Println("password:",r.Form["password"])
	}
}

func upload(w http.ResponseWriter,r *http.Request){
	fmt.Println("method:",r.Method)
	if r.Method == "GET" {
		curtime := time.Now().Unix()
		h := md5.New()
		io.WriterString(h,strconv.FormatInt(curtime,10))
		token := fmt.Sprintf("%x",h.Sum(nil))
		t,_ := template.ParseFiles("upload.gtpl")
		t.Execute(w,token)
	} else {
		r.ParseMultipartForm(32<<20)
		file,handler,err :=r.FormFile("uploadfile")
		if err != nil {
			fmt.Println(err)
			return
		}
		defer file.Close()
		fmt.Fprintf(w,"%v",handler.Header)
		f,err := os.OpenFile("./test/"+handler.Filename,os.O_WRONLY|os.O_CREATE,0666)
		if err != nil {
			fmt.Println(err)
			return
		}
		defer f.Close()
		io.Copy(f.file)
	}
}

func main() {
	http.HandleFunc("/",sayhelloName)
	http.HandleFunc("/login",login)
	http.HandleFunc("/upload",upload)
	err := http.ListenAndServe(":9090",nil)
	if err != nil {
		log.Fatal("ListenAndServe:",err)
	}
}