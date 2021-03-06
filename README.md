# String Count Occurence 

stringCountOccurenceFlask is a Python project build using python3 to determine for each query string how many times it occurs in the list of input strings.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes

### Prerequisites

```python
#! /usr/bin/python/  python3
# coding: utf-8
import os
import argparse
import logging as lg
from sparseArray import *
```


### How it works

1. Clone the repo
```sh
$ git clone https://github.com/Fanirisoa/stringCountOccurence.git
```
2. Export the Variable (strings) to your Environment :
```shell
$ export MY_STRINGS=" ... "
```
3. Run and the add the variable (-q : queries) :
```shell
$ python3 -m  main -q  ...
```

### Example 

```shell
$ export MY_STRINGS="blue red blue yellow blue red yellow blue red red blue"
$ python3 -m  main -q blue red yellow green
{'yellow': 2, 'red': 4, 'green': 0, 'blue': 5}
```

###Requirements

To build this project you will need [Docker][Docker Install].

[Docker Install]:  https://docs.docker.com/install/





