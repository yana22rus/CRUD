package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"net/url"
)

func main() {

	var input string

	fmt.Scan(&input)

	data := url.Values{
		"title": {input},
		"submit":     {"Отправить"},
	}

	resp, err := http.PostForm("http://127.0.0.1:5000/", data)

	if err != nil {
		log.Fatal(err)
	}

	var res map[string]interface{}

	json.NewDecoder(resp.Body).Decode(&res)

	fmt.Println(resp.StatusCode)

}
