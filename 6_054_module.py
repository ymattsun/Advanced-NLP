#!/usr/bin/env python
# coding: utf-8

import sys, re
from collections import defaultdict

def module(FILE):
  class Morph:
    def __init__(self, surface, base, pos, pos1):
      self.surface = surface
      self.base = base
      self.pos = pos
      self.pos1 = pos1

  class Chunk:
    def __init__(self, num, morphs, dst, srcs):
      self.num = num
      self.morphs = morphs
      self.dst = dst
      self.srcs = srcs

  one_sentence = []
  all_sentence = []
  relate_dict = defaultdict(list)

  for line in open(FILE):
    if '* ' in line:
      line = line.strip()
      w = re.split(r' ', line)
      w[2] = w[2][:-1]
      one_chunk = Chunk(w[1], [], w[2], [])
      relate_dict[w[2]].append(w[1])
      one_sentence.append(one_chunk)

    elif '\t' in line:
      line = line.strip()
      morph_item = re.split(r'\t|,', line)
      one_chunk.morphs.append(Morph(morph_item[0], morph_item[7], morph_item[1], morph_item[2]))
     
    elif 'EOS' in line:
      for one_chunk in one_sentence: 
        one_chunk.src = relate_dict[one_chunk.num]
 
      all_sentence.append(one_sentence)
      one_sentence = []
      relate_dict = defaultdict(list)
      
  return all_sentence    

if __name__ == '__main__':
  module(sys.argv[1])
