#!/usr/bin/env python
# coding: utf-8

from module import *
import sys

class feature:
  def __init__(self, pre_w, pre_pos, head_w, f_pos):
    self.pre_w = pre_w
    self.pre_pos = pre_pos
    self.head_w = head_w
    self.f_pos = f_pos

def find_head(article):
  if article == 'a' or article =='an' or article =='the':
    return article.upper()
  else:
    return 'NONE'

def make_feature(word, features, next_w, next_pos, hpos):
  item = word.split()
  if features.head_w != 'NONE' and len(item) >= 3: 
    i = 2
  else: 
    i = 1

  w_0 = ' '.join(item[i:])
  fw = item[i]
  fpos = features.f_pos
  hw = item[-1]
  print '%s\n%s\tw[0]=%s\thw=%s\thpos=%s\thw|hpos=%s|%s\tfw=%s\tfpos=%s\tfw|fpos=%s|%s\tw[-1]=%s\tpos[-1]=%s\tw[1]=%s\tpos[1]=%s' % (word, features.head_w, w_0, hw, hpos, hw, hpos, fw, fpos, fw, fpos, features.pre_w, features.pre_pos, next_w, next_pos)

def a_the_none(all_sentence):
  for one_sentence in all_sentence:
    word = ''
    pre_w = 'None'
    pre_pos = 'None'
    for one_chunk in one_sentence:
      if one_chunk.chunk == 'B-NP':
        if word.startswith('#'):
          make_feature(word, features, one_chunk.w, one_chunk.pos, pre_pos)

        head_w = find_head(one_chunk.w.lower())
        features = feature(pre_w, pre_pos, head_w, one_chunk.pos)
        word = '# ' + one_chunk.w

      elif one_chunk.chunk == 'I-NP' and word != '':
        if features.head_w != 'NONE':
          features.f_pos = one_chunk.pos

        word += ' ' + one_chunk.w

      elif word != ' ':
        make_feature(word, features, one_chunk.w, one_chunk.pos, pre_pos)
        word = ' '

      else: pass
      pre_w = one_chunk.w
      pre_pos = one_chunk.pos

if __name__ == '__main__':
  a_the_none(module(sys.argv[1]))
