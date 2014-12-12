#!/usr/bin/env python
# coding: utf-8

import sys, re
from module import *

def more_than_2_phrase(FILE):
  chunk_list = module(FILE)

  for chunk in chunk_list:
    for i in range(len(chunk)):
      if len(chunk[i].srcs) >= 2:
        print chunk[i].srcs
        saki = ''
        
        for j in chunk[i].morphs:
          saki += j.surface
        print saki + '\n'
          
        for src in chunk[i].srcs:
          moto = ''
          for k in chunk[int(src)].morphs:
            moto += k.surface
          print moto

if __name__ == '__main__':
  more_than_2_phrase(sys.argv[1])
