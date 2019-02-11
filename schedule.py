#coding=utf-8
from collect_data.analyse_url import *
from collect_data.spider_work import *
from AI.bp_train import *
import time
import os
curdir = os.path.dirname(__file__)
if __name__ == '__main__':
    while 1:
        ####analyse task########
        #try:
	    #analyse_white_url()
            #analyse_black_url()
        #except Exception as e:
        #    pass
        #####bp train task######
        #train_bp()    

        ####spider task#########
	try:
#            WhiteSpider_work()
            BlackSpider_work()
	except Exception as e:
            pass

	####sleep 1 month#######
	time.sleep(30*24*60*60)
