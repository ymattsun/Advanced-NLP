#!/usr/bin/env python
# coding: utf-8

import CaboCha, glob

def corpus():
  for num in glob.glob('cabocha_japanese_?.txt'):
    result = open('7_061_output_' + num, 'w')
      print num
      for line in open(num):
        Cabo = CaboCha.Parser('--charset=UTF8')
        result.write(Cabo.parse(line).toString(CaboCha.FORMAT_LATTICE))
    
    result.close()

if __name__ == '__main__':
  corpus()
