# Design

## Repositories

#### `Repository`

A place where `Document`s are located.

A class is a Repository iff:

* it has a `collect` method with the signature `pattern[string] -> list[string x string]`

Assumes a flat hierarchy of files (i.e., doesn't recurse on the underlying directory tree).


#### `LocalRepository`

A `Repository` residing on the same machine as the `indexer`.

Specified as a UNIX path. Examples:

* '../docs-bosh/` (relative)
* '/Users/username/docs-bosh/' (absolute)

