import sys
import re

argvs = sys.argv
argc = len(argvs)
f = open(argvs[1]) 

line = f.readline() 

ipList = []
while line:
    tmp = line.split("\t")
    print tmp[0]
    line = f.readline() 
f.close()
