package main

import (
	"flag"
	"fmt"
	"time"
)

var (
	host = flag.String("host", "192.168.100.22", "Host or direction IP to scann")
	port = flag.String("range", "1-65535", "Port range to compaare to 80-443, 1-65535")

	threads = flag.Int("threads", 1000, "threads number to use")

	timeout = flag.Duration("timeout", 1*time.Second, "Seconds per port")
)

func initScanner() {
	fmt.Println("Hi")
}

func main() {

	initScanner()

}
