This defines a Docker images that we use for our CI. We have multiple images because we want to test against multiple
versions of Python. The `build_push_all.sh` script in this directory can be used to to update the container for all the
different versions. For example:

```
$ ./build_push_all.sh v005
```

would create new images tagged `registry.gitlab.com/companionlabs-opensource/classy-fastapi:v005-py3.9` and
`registry.gitlab.com/companionlabs-opensource/classy-fastapi:v005-py3.11` for the two different versions of Python we
currently support. Our CI then runs the same check.sh script against these different versions of Python.
