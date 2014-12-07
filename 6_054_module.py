#!/usr/bin/env python
# coding: utf-8

from collections import defaultdict

class Morph:
  def __init__(self, surface, base, pos, pos1):
    self.surface = surface
    self.base = base
    self.pos = pos
    self.pos1 = pos1

class Chunk:
  def __init__(self, num, morphs, morphs_add, dst, src, main_word, main_pos):
    self.num = num
    self.morphs = morphs
    self.morphs_add = morphs_add
    self.dst = dst
    self.src = src
    self.main_word = main_word
    self.main_pos = main_pos

def morphs_pos(self, w):
  for morphs in self.morphs:
    if morphs.pos == w:
      return True

  return False

def morphs_pos1(self, w):
  for morphs in self.morphs:
    if morphs.pos1 == w:
      return True

  return False

def morphs_not_kigou(self):
  w = ''
  for morphs in self.morphs:
    if morphs.pos != "記号":
      w = w + morphs.surface

  return w

def morphs_base_return(self):
  for morphs in self.morphs:
    if morphs.pos == '名詞' or morphs.pos == '動詞' or morphs.pos == '形容詞':
      if morphs.base != '*':
        return morphs.base
      else:
        return morphs.surface
  return False

def module(FILE):
  import sys, re

  one_sentence = []
  all_sentencd = []
  relate_dict = defaultdict(list)

  for line in open(FILE):
    if '* ' in line:
      line = line.strip()
      w = re.split(r' |/', line)
      w[2] = w[2][:-1]
      one_chunk = Chunk(w[1], [], '', w[2], [], '', '')
      relate_dict[w[2]].append(w[1])
      one_sentence.append(one_chunk)
      i = 0

    elif '\t' in line:
      line = line.strip()
      morph_item = re.split(r'\t|,', line)
      one_chunk.morphs.append(Morph(morph_item[0], morph_item[7], morph_item[1], morph_item[2]))
      if morph_item[1] != '記号':
        one_chunk.morphs_add = one_chunk.morphs_add + morph_item[0]

      if i == int(w[3]):
        if morph_item[7] == '*':
          morph_item[7] = morph_item[0]

        one_chunk.main_word = morph_item[7]
        one_chunk.main_pos = morph_item[1]

      i += 1

    elif 'EOS' in line:
      for one_chunk in one_sent:
        one_chunk.src = relate_dict[one_chunk.num]

      all_sentence.append(one_sentence)
      one_sentence = []
      relate_dict = defaultdict(list)

  return all_sentence

if __name__ == '__main__':
  module(sys.argv[1])
