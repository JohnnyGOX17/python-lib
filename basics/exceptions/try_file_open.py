#!/usr/bin/env python3

try:
    fp = open('sample.txt')
except IOError as e:
    print('Unable to open the file:', e)

