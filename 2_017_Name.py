#!/usr/bin/env python
# coding: utf-8

import sys, re

def Name(line):
  raw_Kanji = ur'[一-龠]+'
  raw_Hiragana = ur'[ぁ-ゞ]+'
  raw_Katakana = ur'[ァ-ヾ]+'
  raw_Setsubiji = ur'(くん|きゅん|君|さん|ちゃん|様|殿|たん|氏|マン|夫人|先生|選手)'

  name_pattern = re.compile(ur'(%s|%s|%s)%s' % \
                            (raw_Kanji, raw_Hiragana, raw_Katakana, raw_Setsubiji))

  return re.findall(name_pattern, line)

if __name__ == '__main__':
  for line in open(sys.argv[1]):
    line = line.strip().decode('utf-8')
    n = Name(line)
    if len(n) != 0:
      for name in n:
        name_str = ''
        for char in name:
          name_str += char
        sys.stdout.write('%s\n' % name_str.encode('utf-8'))
