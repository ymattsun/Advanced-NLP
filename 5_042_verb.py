#!/usr/bin/env python
# coding: utf-8

import sys, re

def verb(FILE):
  for line in open(FILE):
    line = line.strip()
    if line != 'EOS':
      mecab_list = re.split(r'\t|,', line)
      if mecab_list[1] == '動詞':
        print mecab_list[0]

if __name__ == '__main__':
  verb(sys.argv[1])
