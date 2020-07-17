#! /usr/bin/python/  python3
# coding: utf-8

import math
import os
import random
import re
import sys
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""Type of file to analyse. Is it a CSV or an XML?""")
    return parser.parse_args()

if __name__ == '__main__':

    strings = [i for i in input().split()]
    main()





import argparse
import analysis.csv as c_an
import analysis.xml as x_an

def parse_arguments():
    description = 'Passing multiple arguments and to get list of args : '
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-q", "--queries", action='store', dest='alist',
                    type=str, nargs='*', default=['item1', 'item2', 'item3'],
                    help="Examples: -i item1 item2, -i item3")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()


print("List of items: {}".format(args.alist))        