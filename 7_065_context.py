#!/usr/bin/env python
# coding: utf-8

from module import *
import re, glob
from collections import defaultdict

def make_word_list():
  word_list = []
  for line in open('7_064_output_tf_idf_top100.txt'):
    word = line.strip().split(' ')
    word_list.append(word)
  return word_list

def context_morphs(all_sentence, word_list):
  num = re.compile(r'[0-9]')
  for word in word_list:
    chunk_list = module(word)
    for sent in chunk_list:
      for j in range(len(sent)):
        context = []
        for k in sent[j].morph:
          if k.pos == '名詞':
            context.append(k.surface)

          else:
            if len(context) >= 2:
              a = ' '.join(context)
              if a in nouns_100:
                for b in sent[int(sent[j].dst)].morph:
                  if b.pos == '名詞' or b.pos == '動詞' or b.pos == '形容詞':
                    print a + '\t -> ' + b.base
                for c in sent[j].srcs:
                  for d in sent[int(c)].morph:
                    if b.pos == '名詞' or b.pos == '動詞' or b.pos == '形容詞':
                      print a + '\t <- ' + d.base

            context = []

        if len(context) >= 2:
          a = ' '.join(context)
          if a in nouns_100:
            for i in sent[int(sent[j].dst)].morph:
              if b.pos == '名詞' or b.pos == '動詞' or b.pos == '形容詞':
                print a + '\t -> ' + b.base

if __name__ == '__main__':
  word_list = make_word_list()
  for num in glob.glob('7_061_output_?.txt'):
    all_sentence = module(num)
    context_morphs(all_sentence, word_list)
