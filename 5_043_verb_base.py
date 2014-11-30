#!/usr/bin/env python
# coding: utf-8

import sys, re

def verb_base(FILE):
  for line in open(FILE):
    line = line.strip()
    if line != 'EOS':
      mecab_list = re.split(r'\t|,', line)
      if mecab_list[1] == '動詞':
        print '基本形は' + mecab_list[7]

if __name__ == '__main__':
  verb_base(sys.argv[1])
