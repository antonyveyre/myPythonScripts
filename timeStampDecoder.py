#!/usr/bin/python
import sys,re,os,os.path,time
from datetime import datetime




def intervalChecker(datesArray,currentDate):
  result = False
  for dates in datesArray:
    if datetime.strptime(dates[0],'%Y-%m-%d-%H%M') <currentDate<datetime.strptime(dates[1],'%Y-%m-%d-%H%M'):
      result = True
      break
  return result

datesToCheck = [
('2016-11-15-0000','2016-11-15-1200'),
('2016-11-16-1200','2016-11-16-1230')
]

def parsTimeStamp(fileToRead):
  newLogName = str(fileToRead)+'_new.txt'
  if (os.path.isfile(newLogName)):
    os.remove(newLogName)
  newFileForLog = open(newLogName,'w')
  logToRead = open(fileToRead,'r')
  toPrint = False
  for line in logToRead:
    match = re.search('timestamp=\"\d+',line)
    if (None!=match):
      curLogingDate = datetime.fromtimestamp(float(match.group().split('"')[1][0:10]))
      line = line.replace(match.group(),'timestamp=\"'+str(curLogingDate))
      toPrint = intervalChecker(datesToCheck,curLogingDate)
    if (toPrint):
      print (line,file=newFileForLog,end='')

def main():
  if len(sys.argv) != 2:
    print ('usage timestampDecoder.py file-to-decode')
    sys.exit(1)
  parsTimeStamp(sys.argv[1])

if __name__ == '__main__':
  main()
