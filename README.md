Offline indexing for documentation to make it searchable.


### Indexing

1. Clone this repository
2. Clone https://github.com/cloudfoundry/docs-bosh (leave the name `docs-bosh`)
3. `cd python`
4. `make` (assumes you have `python3` installed)

This will index the documentation, creating `index_*.json` files in the current directory.


### Searching

Now that we have the indexes, we can feed it into a search engine to test things out. Let's copy the indexes into a place where the web app can find it.

```bash
$ make sync
```

Now that the data is copied, we prepare and launch the web app. First, we setup the python libraries needed to run the app:

* `pip install -r requirements.txt`

Next we need to configure some essential variables for the app:

* `source dev_variables` (if you type `echo $DOCS_URL` and get nothing, something went wrong)

We're now ready to launch the app:

```bash
$ make run
```

If you get an error about ports, edit *Makefile* and change `8001` to something else. If all went well, you should now navigate to [http://localhost:8001](http://localhost:8001) to play with the search engine.

Currently two types of search are possible:

1. search/title/[query]
2. search/content/[query]

As the names suggest, the first matches documents based on title, the second based on the entire contents.


### Log
* 01/15/17
  - started project in Golang
  - rewrote initial project in Python
  - introduced stop words
* 01/16/17
  - introduced punctuation
  - finished a basic prototype
  - introduced a search client
* 01/20/17
  - introduced LocalRepository, Document
  - tokenize entire contents of docs, not just titles
  - store positional info on tokens
    - useful for efficient phrasal queries
    - supports induction of titles (line_num == 2)
  - decided not to do [stemming](https://en.wikipedia.org/wiki/Stemming)
* 01/21/17
  - introduced TitleIndexer, ContextIndexer
  - added options to search by title or by content in the web app
  - refactored `repo` module
  - extracted dict to json routine into a utility function
  

### Sources
* The set of stop words is from [Kevin Bougé](https://sites.google.com/site/kevinbouge/stopwords-lists).
