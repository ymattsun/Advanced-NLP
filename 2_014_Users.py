#!/usr/bin/env python
# coding: utf-8

import sys, re

def Users(FILE):
  f = open(FILE)
  user = re.compile(ur'@[a-zA-Z0-9_]+')
  users = [ user.findall(line) for line in f \
            if len(user.findall(line)) != 0 ]
  f.close()
  return users

if __name__ == '__main__':
  users = Users(sys.argv[1])
  for user in users:
    print user
