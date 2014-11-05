#!/usr/bin/env python
# coding: utf-8

import re, sys

def replace_Users(FILE):
  user_re = re.compile(r'(@([a-zA-Z0-9_]+))')
  user_link =  [ user_re.sub(r'<a href="https://twitter.com/#!/\2">\1</a>', line)\
                 for line in open(FILE) ]

  for line in user_link:
    print line

if __name__ == '__main__':
  replace_Users(sys.argv[1])
