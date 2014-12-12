import sys, re
from module import *

def tab_extract(FILE):
  chunk_list = module(FILE)

  for chunk in chunk_list:
    for i in range(len(chunk)):
      if chunk[i].dst != '-1':
        moto, saki = '', ''

        for j1 in chunk[i].morphs:
          if j1.pos != '記号':
            moto += j1.surface

        for j2 in chunk[int(chunk[i].dst)].morphs:
          if j2.pos != '記号':
            saki += j2.surface

        print moto + '\t' + saki + '\n'

if __name__ == '__main__':
  tab_extract(sys.argv[1])
