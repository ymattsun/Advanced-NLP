#!/usr/bin/env python
# coding: utf-8

from module import *
import sys

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

def a_the_none(all_sentence):
  for one_sentence in all_sentence:
    word = ' '
    for one_chunk in one_sentence:
      if one_chunk.chunk == 'B-NP':
        if word.startswith('#'):
          word = make_article(word)
          print word

        word = '# ' + one_chunk.w

      elif one_chunk.chunk == 'I-NP' and word != ' ':
        word += ' ' + one_chunk.w

      elif word != ' ':
        word = make_article(word)
        print word
        word = ' '

      else: pass

if __name__ == '__main__':
  a_the_none(module(sys.argv[1]))
