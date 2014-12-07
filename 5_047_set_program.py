#!/usr/bin/env python
# coding: utf-8

import sys, re, optparse
parser = optparse.OptionParser()

parser.add_option('-a', '--verb',   action = 'store_true', help = '5_042_verb',        default = False)
parser.add_option('-b', '--vbase',  action = 'store_true', help = '5_043_verb_base',   default = False)
parser.add_option('-c', '--sahen',  action = 'store_true', help = '5_044_noun_sahen',  default = False)
parser.add_option('-d', '--AandB',  action = 'store_true', help = '5_045_A_and_B',     default = False)
parser.add_option('-e', '--syzygy', action = 'store_true', help = '5_046_noun_syzygy', default = False)

options, args = parser.parse_args()

def set_program(FILE):
  AandB_list, list_noun = [], []
  for line in open(FILE):
    line = line.strip()
    if line != 'EOS':
      mecab_list = re.split(r'\t|,', line)
      AandB_list.append(mecab_list)
      #-------------------------------------------------------42
      if options.verb == 1:
        if mecab_list[1] == '動詞':
          print mecab_list[0]
      #-------------------------------------------------------43
      if options.vbase == 1:
        if mecab_list[1] == '動詞':
          print '基本形は「' + mecab_list[7] + '」です'
      #-------------------------------------------------------44
      if options.sahen == 1:
        if mecab_list[2] == 'サ変接続':
          print mecab_list[2] + 'は「' + mecab_list[0] + '」です'
      #-------------------------------------------------------45
      if options.AandB == 1:
        i = len(AandB_list)-1
        if i > 1 and AandB_list[i-2][1] == '名詞' and AandB_list[i-1][0] == 'の' and AandB_list[i][1] == '名詞':
          print AandB_list[i-2][0], AandB_list[i-1][0], AandB_list[i][0]
      #-------------------------------------------------------46
      if options.syzygy == 1:
        if mecab_list[1] == '名詞':
          list_noun.append(mecab_list[0])

        elif len(list_noun) >= 2:
          print ' '.join(list_noun) + '\n'
          list_noun = []

        else:
          list_noun = []

if __name__ == '__main__':
  set_program(sys.argv[1])
