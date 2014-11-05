#!/usr/bin/env python
# coding: utf-8

import sys, re

def emoji(FILE):
  parts = re.compile(ur'(\\)*(\()+[^0-9A-Za-zぁ-ヶ一-龠]+?(\))+(\/)*')

  for line in open(FILE):
    kaomoji = parts.search(line)
    if kaomoji:
      print kaomoji.group(0)

if __name__ == '__main__':
  emoji(sys.argv[1])
