package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
//  "time"
  "sync"
)
type enpoint struct{
  url string
}

func apiGet(id int,wg *sync.WaitGroup, url string) {
  defer wg.Done()
  //url := "http://bugzilla.ensenada.gob.mx:5000/ficha/tramite/summary/list/read/ensenada"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := ioutil.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }

  fmt.Println(id," : ", res.Status)
  fmt.Println(string(body))
}

func main(){
  var apis []string
  //apis =append(apis,"http://bugzilla.ensenada.gob.mx:1123/digiTramite/all")
//  apis = append(apis, "http://bugzilla.ensenada.gob.mx:5000/ficha/tramite/summary/list/read/0")
  apis = append(apis, "http://10.0.8.62:8080/login?from=%2F")
  apis = append(apis, "http://10.0.8.62:8080/view/lista/")
  var wg sync.WaitGroup
  for i:=0; i<=10000000; i++{
	  fmt.Println("index:",i)
	  for _,url := range apis{
		  wg.Add(1)
		  fmt.Println("%\n",url)
		  go apiGet(i,&wg,url)
	  }
  }
	wg.Wait()
	fmt.Println("done")
}
