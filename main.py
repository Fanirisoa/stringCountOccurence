#! /usr/bin/python/  python3
# coding: utf-8

import math
import os
import random
import re
import sys




def main():
    pass

if __name__ == '__main__':

    stringset = [i for i in input().split()]

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)


print(stringset)
print(strings)
print(queries)