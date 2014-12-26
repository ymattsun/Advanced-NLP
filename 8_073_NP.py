#!/usr/bin/env python
# coding: utf-8

from module import *
import sys

def np(all_sentence):
  for one_sentence in all_sentence:
    word = ''
    for one_chunk in one_sentence:
      if one_chunk.chunk == 'B-NP':
        if word.startswith('#'):
          print word

        word = '# ' + one_chunk.w

      elif one_chunk.chunk == 'I-NP' and word != ' ':
        word += ' ' + one_chunk.w

      elif word != ' ':
        print word
        word = ' '

      else: pass

if __name__ == '__main__':
  np(module(sys.argv[1]))
