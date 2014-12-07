#!/usr/bin/env python
# coding: utf-8

import sys, re

def noun_sahen(FILE):
  for line in open(FILE):
    line = line.strip()
    if line != 'EOS':
      mecab_list = re.split(r'\t|,', line)
      if mecab_list[2] == 'サ変接続':
        print mecab_list[2] + 'は「' + mecab_list[0] + '」です'

if __name__ == '__main__':
  noun_sahen(sys.argv[1])
