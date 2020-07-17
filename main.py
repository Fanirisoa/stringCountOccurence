#! /usr/bin/python/  python3
# coding: utf-8

import math
import os
import random
import re
import sys
import argparse
from sparseArray import *
def parse_arguments():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--queries", action='store', dest='alist',
                    type=str, nargs='*', default=['str1', 'srt2', 'srt3'],
                    help="Examples: -q str1 srt2 srt3")
    parser.add_argument("-r", "--resultType", action='store', dest='str',
                    type=str, default=['dic'], help="""Type of the output result. Is it a vec (as vector) or a dic (as dictionary)?""")
    
    return parser.parse_args()

    

if __name__ == '__main__':
    strings = [i for i in input().split()]
    args = parse_arguments()
    queries = args.alist
    stringsToQueries =  setStringToCompare(queries,strings)


    if args.str == 'dic':
        print(stringsToQueries.matchingStringsToDic())
    elif args.str == 'vec':
        print(stringsToQueries.matchingStringsToVec())
    else:
        raise Exception("Wrong index")


