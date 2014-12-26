#!/usr/bin/env python
# coding: utf-8

from collections import defaultdict
import sys

class Morph:
  def __init__(self, w, lem, pos, chunk):
    self.w = w
    self.lem = lem
    self.pos = pos
    self.chunk = chunk

def module(FILE):
  one_sentence = []
  all_sentence = []
  for line in open(FILE):
    if '\t' in line:
      morph_item = line.strip().split('\t')
      one_sentence.append(Morph(morph_item[0], morph_item[1], morph_item[2], morph_item[3]))
    else:
      all_sentence.append(one_sentence)
      one_sentence = []

  print all_sentence

if __name__ == '__main__':
  module(sys.argv[1])
