# get_helm
Python script for installing kubernetes helm.

The script calls the Github API to find the latest release of helm, downloads
the `.tar.gz` archive from Google Cloud storage, and extracts the helm
binary into the location specified.

# Requirements / limitations

Currently requires Python 3.6+ due to use of
[f-strings](https://www.python.org/dev/peps/pep-0498/).

It uses only modules from the python standard library.

# Usage
```bash
$ python3 get_helm.py /usr/local/bin/helm
```
