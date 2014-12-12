#!/usr/bin/env python
# coding: utf-8

import sys, re
from module import *

def phrase_expression(FILE):
  chunk_list = module(FILE)

  chunk1, chunk2 = '', ''

  for chunk1 in chunk_list:
    for chunk2 in chunk_list:

      for i in range(len(chunk1)):
        for j in range(len(chunk2)):

          if chunk1[i].dst == chunk2[j].num:

            for j1 in chunk1[i].morphs:
              for j2 in chunk2[j].morphs:

                if j1.pos == '名詞' and j2.pos == '名詞':
                  print j1.surface + '\t' + j2.surface + '\n'
                  print chunk2[j].num + '->' + chunk1[i].num

if __name__ == '__main__':
  phrase_expression(sys.argv[1])
