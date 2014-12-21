#!/usr/bin/env python
# coding: utf-8

import re, glob
list_noun = []

def noun_phrase():
  for num in glob.glob('7_061_output_?.txt'):
    result = open('7_062_output_' + num[12:], 'w')
      for line in open(num):
        if '\t' in line:
          line = line.strip()
          morph_item = re.split(r'\t|,', line)

          if morph_item[1] == '名詞':
            list_noun.append(morph_item[0])

          elif len(list_noun) > 0:
            for noun in list_noun:
              rersult.write(noun)

            result.write('\n')
            list_noun = []

          else:
            list_noun = []

        elif '* ' in line or 'EOS' in line:
          if len(list_noun) > 0:
            for noun in list_noun:
              result.write(noun)

            result.write('\n')
            list_noun = []

          else:
            list_noun = []

      result.close()

if __name__ == '__main__':
  noun_phrase()
