#!/usr/bin/env python
# coding: utf-8

class Morph:
  def __init__(self, surface, base, pos, pos1):
    self.surface = surface
    self.base = base
    self.pos = pos
    self.pos1 = pos1

def morph(FILE):
  import sys, re

  all_sentence = []
  one_sentence = []

  for line in open(FILE):
    if '\t' in line:
      line = line.strip()
      morph_item = re.split(r'\t|,', line)
      one_sentence.append(Morph(morph_item[0], morph_item[7], morph_item[1], morph_item[2]))

    elif 'EOS' in line:
      for item in one_sentence:
        print 'surface = %s \t base = %s \t pos = %s \t pos1 = %s' % (item.surface, item.base, item.pos, item.pos1)

      all_sentence.append(one_sentence)
      print 'EOS'
      one_sentence = []

if __name__ == '__main__':
  morph(sys.argv[1])
