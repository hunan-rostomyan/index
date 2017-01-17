Offline indexing for documentation to make it searchable.


### Indexing

1. Clone this repository
2. Clone https://github.com/cloudfoundry/docs-bosh (leave the name `docs-bosh`)
3. `cd python`
4. `make` (assumes you have `python3` installed)

This will index the documentation, creating an *index.json* file in the current directory. You can inspect the contents of this dictionary to make sure nothing blew up:


```python
import json

index = json.load(open('index.json'))
assert 'vcloud' in index
```

### Searching

Now that we have the documentation index (contained in *index.json*), we can feed it into a little "search engine" to test things out. Let's copy the index into a place where the web app can find it and then run the app to make some queries.

* `cp index.json web/search/data/` (otherwise you'll get an `IOError` later)

Now that the data is copied, we prepare and launch the web app. First, we setup the python libraries needed to run the app:

* `pip install -r requirements.txt`

Next we need to configure some essential variables for the app:

* `source dev_variables` (if you type `echo $DOCS_URL` and get nothing, something went wrong)

We're now ready to launch the app:

1. `cd web` (you're inside the web root)
2. `export PORT=8005`
3. `./manage.py runserver $PORT` (if you get an error about ports, try (2) with a different port)

If all went well, you should now navigate to [http://localhost:[PORT]](http://localhost:[PORT]) to play with the search engine.

Change the query following `search/` in the URL to find different matching documents. Here, for example, we search for "cloud":

* `http://localhost:[PORT]/search/cloud`,

which returns a list of hyperlinks to the relevant documents in the specified repository:

```
You searched for: "cloud".

Relevant documents:
  cloud => cck.html.md.erb
  cloud => cloud-config.html.md.erb
  vcloud => deploy_microbosh_to_vcloud.html.md.erb
  vcloud => init-vcloud.html.md.erb
  vcloud => vcloud-cpi.html.md.erb
```


### Log
* 01/15/17
  - started project in Golang
  - rewrote initial project in Python
  - introduced stop words
* 01/16/17
  - introduced punctuation
  - finished a basic prototype
  - introduced a search client


### Sources
* The set of stop words is from [Kevin Bougé](https://sites.google.com/site/kevinbouge/stopwords-lists).
