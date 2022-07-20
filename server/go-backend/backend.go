package main

import (
	"fmt"
	"os"

	"github.com/akamensky/argparse"
)

func main() {
	parser := argparse.NewParser("Paco Panda API Backend", "The Paco Panda API Backend written in Go, previously written in Python")

	s := parser.Flag("s", "scrape", &argparse.Options{Required: false, Help: "Scrape the thing"})
	a := parser.Flag("a", "api", &argparse.Options{Required: false, Help: "Run the api"})

	err := parser.Parse(os.Args)

	if err != nil {
		fmt.Print(parser.Usage(err))
		os.Exit(1)
	}

	if *s {
		scraper()
	}

	if *a {
		api()
	}
}
