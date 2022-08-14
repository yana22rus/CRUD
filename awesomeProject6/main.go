package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"net/url"
)

func main() {
	var url,value string

	fmt.Scan(&url,&value)

	crud(url, value)

}

func crud(link,options string) {

	data := url.Values{
		"title":  {options},
		"submit": {"Отправить"},
	}

	resp, err := http.PostForm(link, data)

	if err != nil {
		log.Fatal(err)
	}

	var res map[string]interface{}

	json.NewDecoder(resp.Body).Decode(&res)

	fmt.Println(resp.StatusCode)
}
