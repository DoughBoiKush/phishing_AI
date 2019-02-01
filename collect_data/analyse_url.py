#coding=utf-8
from features import *
import os
curdir = os.path.dirname(__file__)

def write2file(result,filename,isphishing):
    res = ','.join(str(i) for i in result) + ','+isphishing+'\n'
    fr = open(os.path.join(curdir,filename), 'r')
    for line in fr.readlines():
        if line == res:
            print "repeat...... " + res
            return
    fw = open(os.path.join(curdir,filename),'a+')
    fw.write(res)
    fw.close()

def analyse_white_url():
    fr = open(os.path.join(curdir,'./data/white.txt'), 'r')
    result = []
    for line in fr.readlines():
	url = "http://"+line.strip('\n')
	print 'white url: '+url
	try:
   	    result = urlfeatureextractor(url) 
	except Exception as e:
            pass
     	if result != []: 
            write2file(result,'./data/white_data.csv','-1')
	url = "https://www."+line.strip('\n')
        print 'white url:'+url
	try:
            result = urlfeatureextractor(url)         
        except Exception as e:
            pass
	if result != []: 
            write2file(result,'./data/white_data.csv','-1')
    fr.close()

def analyse_black_url():
    fr = open(os.path.join(curdir,'./data/black.txt'), 'r')
    result = []
    for line in fr.readlines():
        try:
	    print "black url:" + line
            result = urlfeatureextractor(line.strip('\n'))
        except Exception as e:
            pass
        if result != []:
            write2file(result,'./data/black_data.csv','1')
    fr.close()

analyse_white_url()
analyse_black_url()
