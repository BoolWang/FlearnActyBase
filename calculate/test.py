#import UserActy.UserActy as ua
import datetime
import numpy as np
from bin.time_str import get_now
import useracty.ActyRuler
import datetime
from collections import OrderedDict
from sql.mongo import doc2mongo,get_actyh,getclient,updata_actyh
import pymongo as pmg
from bin.globalNUM import *
import pandas as pd
import time
from sql.StudyH import getclient
import time

# cur1=getclient()
# alllist="ACEFGHIJKLNPSTUVW"
# for j in alllist:
#     query="select UserId from studyh where UserId  REGEXP '^[%s]'"%j
#     start=time.clock()
#     cur1.execute(query)
#     stop1=time.clock()
#     print("spendtime:%s Sec of %s"%(stop1-start,j))
# alldata1=cur1.fetchall()
# idlist=list(map(lambda x:x[0],alldata1))
# idlist=list(set(idlist))
# stop2=time.clock()
# print("spendtime1:%s Sec"%(stop2-stop1))

class Test():
    def __init__(self):
        self.__a="a"
        self.__b=self.tt()

    def tt(self):
        self.__o="p"
        return "ab"

    def __repr__(self):
        return "a:%s,b:%s,o:%s"%(self.__a,self.__b,self.__o)

A=Test()
print(A)