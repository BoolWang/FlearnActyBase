#从数据库获取用户的学习记录
import pymysql
import pandas as pd
import datetime
import time
from bin.globalNUM import *

def getclient():
    conn1=pymysql.connect(SQLhost,user=SQLuser,passwd=SQLpwd,
                       db=SQLdb,charset='utf8',port=SQLport)
    cur1=conn1.cursor()#游标
    return cur1

def sqlbyid(id):
    # conn1=pymysql.connect("10.134.149.182",user='twbigdata',passwd='20200304#',
    #                   db='targetdb',charset='utf8',port=3306)
    conn1=pymysql.connect(SQLhost,user=SQLuser,passwd=SQLpwd,
                       db=SQLdb,charset='utf8',port=SQLport)
    cur1=conn1.cursor()#游标
    #query1="select VideoStartTime, SpendSec from log_data_Course_see_2 where UserId=\"%s\" and SpendSec>60"%id
    query1="select VideoStartTime, SpendSec from %s where UserId=\"%s\" and SpendSec>60"%(SQLtable,id)
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
    return sh

#只查找指定时间范围内的学习记录
def sqlbyid_days(id,fday,lday):
    fday=fday.strftime("%Y-%m-%d")
    lday=lday.strftime("%Y-%m-%d")
    cur1=getclient()
    query1="select VideoStartTime, SpendSec from %s where UserId=\"%s\" and SpendSec>60 and VideoStartTime>\"%s\" and VideoStartTime<\"%s\""%(SQLtable,id,fday,lday)
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
    return sh

def select_all_id():
    conn1=pymysql.connect(SQLhost,user=SQLuser,passwd=SQLpwd,
                       db=SQLdb,charset='utf8',port=SQLport)
    cur1=conn1.cursor()#游标
    #query1="select VideoStartTime, SpendSec from log_data_Course_see_2 where UserId=\"%s\" and SpendSec>60"%id
    query1=r"select UserId from %s where UserId  REGEXP '^[C]'"%SQLtable
    print(query1)
    #query1=r"select UserId from %s where UserId  REGEXP '^[ACEFGHIJKLNPSTUVW]'"%SQLtable
    f=time.clock()
    print("start:%s"%f)
    cur1.execute(query1)
    f1=time.clock()
    print("start:%s,spendSec:%s"%(f1,f1-f))
    alldata1=cur1.fetchall()
    idlist=list(map(lambda x:x[0],alldata1))
    idlist=list(set(idlist))
    return idlist

# print(sqlbyid("F1200162"))
# print(sorted(sqlbyid("F1200162").keys()))
# nowday=datetime.datetime(2019, 8, 25, 0, 0)
# print(sqlbyid("F3235939")[nowday])
#print(select_all_id()[0:10])