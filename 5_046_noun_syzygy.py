#!/usr/bin/env python
# coding: utf-8

import sys, re

def noun_syzygy(FILE):
  list_noun = []
  for line in open(FILE):
    line = line.strip()
    if line != 'EOS':
      mecab_list = re.split(r'\t|,', line)

      if mecab_list[1] == '名詞':
        list_noun.append(mecab_list[0])

      elif len(list_noun) >= 2:
        print ' '.join(list_noun) + '\n'
        list_noun = []

      else:
        list_noun = []


if __name__ == '__main__':
  noun_syzygy(sys.argv[1])
