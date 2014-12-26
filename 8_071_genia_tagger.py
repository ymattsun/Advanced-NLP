#!/usr/bin/env python
# coding: utf-8

import sys, re, glob
from geniatagger import *
tagger = GeniaTagger('/home/yuta/ドキュメント/NLP100_mattsun/set_8/geniatagger-3.0.1/geniatagger')

def genia_tagger():
  for name in glob.glob('english_?.txt'):
    result = open('8_071_genia_tagger_' + name[-5:], 'w')
    print 'name', name
    for line in open(name):
      line = line.strip()
      iList = re.split(r'(\.) ([A-Z])|(\[[0-9]+\]+) ([A-Z])', line)
      while None in iList: iList.remove(None)
      for w in range(len(iList)):
        w_tagger = None
        if w == 0 and len(iList) == 1
          w_tagger = tagger.parse(iList[w])

        elif w == 0 :
          w2 = iList[w]

        elif w == 1:
          w2 += iList[w]
          w_tagger = tagger.parse(w2)

        elif w % 3 == 2:
          w2 = iList[w]

        elif w == (len(iList) - 1):
          w2 += iList[w]
          w_tagger = tagger.parse(w2)

        elif w % 3 == 0:
          w2 += iList[w]

        else:
          w2 += iList[w]
          w_tagger = tagger.parse(w2)

        if w_tagger:
          for w in w_tagger:
            result.write('\t'.join(w) + '\n')

          result.write('\n')

    result.close()

if __name__ == '__main__':
  genia_tagger()
