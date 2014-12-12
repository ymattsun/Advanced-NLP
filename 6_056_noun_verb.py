#!/usr/bin/env python
# coding: utf-8

import sys, re
from module import *

def noun_verb(FILE):
  chunk_list = module(FILE)

  for chunk in chunk_list:
    for i in range(len(chunk)):
      if chunk[i].dst != '-1':
        noun, verb = '', ''
        noun_check, verb_check = 0, 0

        for j1 in chunk[i].morphs:
          if j1.surface != '、 ' and j1.surface != '。 ':
            noun += j1.surface
          if j1.pos == '名詞':
            noun_check = 1

        if noun_check == 0:
          continue 

        for j2 in chunk[int(chunk[i].dst)].morphs:
          if j2.surface != '、 ' and j1.surface != '。 ':
            verb += j2.surface
          if j1.pos == '動詞':
            verb_check = 1

        if verb_check == 0:
          continue

        print noun + '\t' + verb + '\n'


if __name__ == '__main__':
  noun_verb(sys.argv[1])
