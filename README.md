# Master Repo for Algorithm Design
[![Build Status](https://travis-ci.org/Sebastian-ba/DoDoBing.svg?branch=fix-build)](https://travis-ci.org/Sebastian-ba/DoDoBing)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2bef561e297d481da9944daf4f6dd2e2)](https://www.codacy.com/app/Sebastian-ba/DoDoBing?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Sebastian-ba/DoDoBing&amp;utm_campaign=Badge_Grade)

![DoDo](http://www.nhm.ac.uk/content/dam/nhmwww/our-science/news/2017/dodo-model-news-two-column.jpg "DoDo")

![Bing](https://mymerrychristmas.com/x/wp-content/uploads/2015/10/bingcrosby.jpg "Bing")

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
