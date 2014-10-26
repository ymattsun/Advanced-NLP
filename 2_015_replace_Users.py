#!/usr/bin/env python
# coding: utf-8

import re, sys

def replace_Users(FILE):
  f = open(FILE)
  user_Re = re.compile(r'(@([a-zA-Z0-9_]+)):')
  return [ user_Re.sub(r'<a href="https://twitter.com/#!/\2">\1</a>', line)\
           for line in f ]
  f.close()

if __name__ == '__main__':
  replaced = replace_Users(sys.argv[1])
  for line in replaced:
    print line
