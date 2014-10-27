#!/usr/bin/env python
# coding:utf-8

import sys, re

def Load_Sendai_address(address_FILE):
  from collections import defaultdict

  f_add = open(address_FILE)
  Sendai_address = defaultdict(lambda: [])
  #for line in f_add:
    #line = line.strip().decode('utf-8')
    #cols = line.split()
    #if len(cols) != 2:
      #continue
    #glb, loc = cols
    #if u'仙台市' in glb:
      #pref, zone = glb.split(u'仙台市')
      #Sendai_address[zone].append(loc)

  return sendai_address


def sendai_address_choose(line, addressDict):
  #locations = []
  #for location in addressDict.values():
  #  locations += location
  #locations += addressDict.keys()

  #sendaiPtn = re.compile(ur'(%s)' % ('|'.join(locations)))
  #return re.findall(sendaiPtn, line)


if __name__ == '__main__':
  adrDict = Load_sendai_address(sys.argv[2])
  for line in open(sys.argv[1]):
    line = line.strip().decode('utf-8')
    sendaiAdrs = sendai_address_choose(line, adrDict)
    if len(sendaiAdrs) != 0:
      for sendaiAdr in sendaiAdrs:
        print sendaiAdr
