# Master Repo for Algorithm Design
[![Build Status](https://travis-ci.org/Sebastian-ba/DoDoBing.svg?branch=fix-build)](https://travis-ci.org/Sebastian-ba/DoDoBing)
<a href="https://www.codacy.com/app/Sebastian-ba/DoDoBing/dashboard"><img src="https://api.codacy.com/project/badge/Grade/c098136ef81345b78c480ee695314a21"/></a>


### Requirements

- python 3.x
- pip

### Install

```bash
$ pip install nose
```

### Running tests
Current directory:
```bash
$ nosetests -vds test.py
```

Any directory:
```bash
$ nosetests -vds -w closest-points/src testParse.py
```

Nose options:

-w Change working directory

-d Debug (e.g. "expect x, actually y")

-v Verbose, list tests failed/passed

-s Shows print statements from tests


[Reference to nosetests](http://pythontesting.net/framework/nose/nose-introduction/)

[Reference to .travis.yml](https://docs.travis-ci.com/user/languages/python/)
