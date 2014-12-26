#!/usr/bin/env python
# coding: utf-8

from module import *

class feature:
  def __init__(self, pre_w, pre_pos, head_w, f_pos):
    self.pre_w = pre_w
    self.pre_pos = pre_pos
    self.head_w = head_w
    self.f_pos = f_pos

def find_head(word):
  if word == 'a' or word == 'an':
    return 'A'
  elif word == 'the':
    return word.upper()
  else:
    return "NONE"

def make_article(word):
  item = word.split()
  l = item[1].lower()
  if l == ('a' or 'an'):
    word += '\n' + 'A'

  elif l == 'the':
    word += '\n' + 'THE'

  else:
    word += '\n' + 'NONE'

  return word

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

def 11feature(all_sentence):
  for one_sentence in all_sentence:
    word = ' '
    pre_w = 'None'
    pre_pos = 'None'
    for one_chunk in one_sentence:
      if one_chunk.chunk == 'B-NP':
        if word.startswith('#'):
          make_feature(word, features, one_chunk.w, one_chunk.pos, pre_pos)

        head_w = find_head(one_chunk.w.lower())
        features = feature(pre_w, pre_pos, head_w, one_chunk.pos)
        word = '# ' + one_chunk.w

      elif one_chunk.chunk == 'I-NP' and word != ' ':
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
  for name in glob.glob('8_071_GENIA_tagger_?.txt'):
    result = open('8_076_output' + name[-5] + '.f', 'w')
    11feature(module(name))
    result.close()
