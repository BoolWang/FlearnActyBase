import pymysql
import pandas as pd
import datetime
import time
from bin.globalNUM import *

uid="G4184118"
today=datetime.datetime.strftime(datetime.datetime.today()+datetime.timedelta(days=1),"%Y-%m-%d")
conn1=pymysql.connect(SQLhost,user=SQLuser,passwd=SQLpwd,
                       db=SQLdb,charset='utf8',port=SQLport)
cur1=conn1.cursor()#游标
#query1="select VideoStartTime, SpendSec from log_data_Course_see_2 where UserId=\"%s\" and SpendSec>60"%id
query1="select VideoStartTime, SpendSec from %s where UserId=\"%s\" and SpendSec>60 and " \
       "VideoStartTime<\"%s\"and VideoStartTime>\"2017-01-01\""%(SQLtable,uid,today)
cur1.execute(query1)
alldata1=cur1.fetchall()
all=pd.DataFrame(list(alldata1),columns=['VideoStartTime','SpendSec'])
all['VideoStartTime']=list(map(lambda x:datetime.datetime.strptime(x.strftime("%Y-%m-%d"),"%Y-%m-%d"),
                               all['VideoStartTime']))
#print(all)
all1=all.groupby(by="VideoStartTime").sum()
sh={}
for i in range(len(all1.index)):
    sh[all1.index[i].to_pydatetime()]=all1.values[i][0]
print(sh=={})