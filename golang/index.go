package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"strings"
)

const DOCS_DIR = "../docs-bosh/"
const TITLE_SEPARATOR = ": "

func inferTitle(docName string) (string, error) {
	contents, err := ioutil.ReadFile(DOCS_DIR + docName)
	if err != nil {
		return "", err
	}

	titleRow := strings.SplitN(string(contents), "\n", 3)[1]
	title := strings.SplitN(titleRow, TITLE_SEPARATOR, 2)[1]
	return title, nil
}

func main() {
	docs, err := ioutil.ReadDir(DOCS_DIR)
	if err != nil {
		log.Fatal(err)
	}

	index := map[string]map[string]struct{}{}

	for _, doc := range docs {
		docName := doc.Name()
		if !strings.Contains(docName, ".html") {
			continue
		}

		docTitle, err := inferTitle(docName)
		if err != nil {
			log.Fatal(err)
		}

		words := strings.Split(docTitle, " ")
		for _, word := range words {
			_, found := index[word]
			if !found {
				index[word] = map[string]struct{}{}
			}
			index[word][docName] = struct{}{}
		}
	}

	bytes, err := json.MarshalIndent(index, "", "\t")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("%s", string(bytes))
}
