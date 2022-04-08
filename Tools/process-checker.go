package main


import (
  "fmt"
  "os/exec"
  "log"
)

func CMD(command string) string{
  
  out, err := exec.Command("lsd", "-la").Output()
  if err != nil{
    log.Fatal("Error in the command included for the execution")
  }
  return string(out)
}


func gettingInformation(){

}




func main(){
  fmt.Println(CMD("ls -la"));
}


