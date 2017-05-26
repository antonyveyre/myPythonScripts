#!/usr/bin/python
import sys,re
from datetime import datetime

def parserDate(fileToRead):
  myNewFileLog = open('myNewFileLog.txt','w')
  f = open(fileToRead)
  for line in f :
    match = re.search('timestamp=\"\d+', line)
    if(match!=None):
      #print datetime.fromtimestamp(float(match.group().split('"')[1][0:10]))
      line = line.replace(match.group(), str(datetime.fromtimestamp(float(match.group().split('"')[1][0:10]))))
    print  >> myNewFileLog,line,


def main():
  if len(sys.argv) != 2:
    print 'usage: ./parserDate.py file-to-read'
    sys.exit(1)

  parserDate(sys.argv[1])
  #print dict


if __name__ == '__main__':
  main()
