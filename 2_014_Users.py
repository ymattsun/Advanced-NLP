#!/usr/bin/env python
# coding: utf-8

import sys, re

def Users(FILE):
  user = re.compile(ur'@[a-zA-Z0-9_]+')
  users = [ user.findall(line) for line in open(FILE) \
            if len(user.findall(line)) != 0 ]

  for i in users:
    print i

if __name__ == '__main__':
  Users(sys.argv[1])
