#!/usr/bin/python
import sys,re,os,os.path,time
from datetime import datetime

def parsRequestLog(fileToRead):
  newLogName = str(fileToRead)+'_new.txt'
  if (os.path.isfile(newLogName)):
    os.remove(newLogName)
  newFileForLog = open(newLogName,'w')
  logToRead = open(fileToRead,'r')
  toPrint = False
  for line in logToRead:
    match = re.search('PT[0-9][0-9]\..*["][}][\]]|PT[5-9]\..*["][}][\]]',line)
    if (None !=match):
      print (line,file=newFileForLog,end='')

def main():
  if len(sys.argv) != 2:
    print ('usage requesLogParser.py file-to-decode or enter path log here:')
    pathToLog = input();
  else :
    pathToLog = sys.argv[1]
  parsRequestLog(pathToLog)
  input()

if __name__ == '__main__':
  main()
