import numpy as np
import datetime
from bin.globalNUM import *
"""
活跃度计算规则
"""
# MINActy=2.5 #最低活跃度，只要有过学习记录的人都有
# MAXtime=7200 #每日最大学习时长，超过该时长也按该时长算活跃度

#活跃度保有率,a为连续未学习天数
def ratin(a):
    return np.power(0.9,min(a,7))

#活跃度加成倍率,b为连续学习天数
def addrate(b):
    return np.power(1.1,min(b,7))*0.005

#活跃度基本计算规则,ltimes为当日学习时长，单位为h
def baseacty(last_acty,ltimes,a,b):
    if last_acty<MINActy:
        return MINActy
    else:
        return max(MINActy,last_acty*ratin(a)+ltimes*addrate(b))


#规则1：根据历史学习记录一天一天的更新
#输入每日学习时长和学习日期跨度（最后一天 - 第一天）
#hstudy是一个数据字典（日期：时长）
def onebyone(hstudy):
    hacty=[]  #按照学习周期进行存储
    #检验日期输入格式并装换为datetime.datetime
    #print(hstudy)
    for hh in hstudy:
        htp=type(hh)
        if htp!=datetime.datetime:
            if(htp==np.datetime64):
                nh=datetime.datetime.strptime(np.datetime_as_string(hh)[0:10],'%Y-%m-%d')
                hstudy[nh]=hstudy.pop(hh)
            else:
                print('type error with %s  which neither datetime.datetime nor numpy.datetime64'%htp)
                return
    datelisth=sorted(hstudy.keys())
    l=(datelisth[-1]-datelisth[0]).days+1
    #print("days=%s"%l)
    fday=datelisth[0]
    hacty.append(MINActy)
    a,b=0,0
    for i in range(l):
        nowday=fday+datetime.timedelta(days=i)
        if(nowday in hstudy):
            a,b=0,b+1
            nowacty=baseacty(hacty[-1],min(hstudy[nowday],MAXtime),a,b)
            #hacty.append(max(nowacty,MINActy))
        else:
            a,b=a+1,0
            nowacty=baseacty(hacty[-1],0,a,b)
        hacty.append(max(nowacty,MINActy))

    return hacty,fday,datelisth[-1],a,b

#根据新的学习记录进行更新，已有历史活跃度记录
def daybyday(oldactyh,hstudy,a,b):
    datelisth=sorted(hstudy.keys())
    l=(datelisth[-1]-datelisth[0]).days+1
    #print("days=%s"%l)
    fday=datelisth[0]
    for i in range(l):
        nowday=fday+datetime.timedelta(days=i)
        if(nowday in hstudy):
            a,b=0,b+1
            nowacty=baseacty(oldactyh[-1],min(hstudy[nowday],MAXtime),a,b)
            #hacty.append(max(nowacty,MINActy))
        else:
            a,b=a+1,0
            nowacty=baseacty(oldactyh[-1],0,a,b)
        oldactyh.append(max(nowacty,MINActy))
    return oldactyh,datelisth[-1],a,b
