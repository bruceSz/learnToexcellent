package main
import (
	"bytes"
	"fmt"
	"io"
	"io/ioutil"
	"mime/multipart"
	"net/http"
	"os"
	)
func postFile(filename string,targetUrl string) error {
	bodyBuf :=&bytes.Buffer()
	bodyWriter :=multipart.NewWriter(bodyBuf)
	fileWriter,err := bodyWriter.CreateFormFile("uploadfile",filename)
	if err != nil {
		fmt.Println("error writing to buffer")
		return err
	}
	fh,err := os.Open(filename)
	if err != nil {
		fmt.Println("error opening file")
		return err
	}
	_,err = io.Copy(fileWriter,fh)
	if err != nil {
		return err
	}
	contentType := bodyWriter.FormDataContentType()
	bodyWriter.Close()
	resp,err := http.Post(targetUrl,contentType,bodyBuf)
	if err != nil {
		return err
	}
	def resp.Body.Close()
	resp_body , err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return err
	}
	fmt.Println(resp.Status)
	fmt.Println(string(resp_body))
	return nil
}
func main() {
	target_url := "http://localhost:9090/upload"
	filename := "./test.txt"
	postFile(filename,target_url)
}