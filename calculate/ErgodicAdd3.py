#遍历系统中所有用户，统计系统的活跃度情况
#具体包括，系统每月的活跃度分析情况
#          系统每周的活跃度分布情况
#还需要实例化所有用户的活跃度情况，通过聚类给活跃度定级
#还是需要全部学员的idList
from sql.mongo import getDataById
from bin.globalNUM import *
import pickle
import datetime
import calendar
from bin.json_io import get_idlist,list2json
from bin.tools import indexByActy
import threading
import time
import sys
import numpy as np

finishUsers=0
class MiniUserActy():
    # 从mongo数据库实例化用于遍历的简化版用户对象
    def __init__(self,uid):
        self.__id=uid
        self.__fday,self.__lday,self.__localActy=getDataById(uid)
        self.__maxActy=self.findMaxActy()
        self.__globalActy=self.uncut()
        self.__MaxMonthActy=self.CutArrByMonth(self.__globalActy[1:],self.__fday,self.__lday)

    def findMaxActy(self):
        # 从localActy中找到历史最大活跃度
        acty=self.__localActy
        if(acty==[[]]):return MINActy
        else:
            maxActy=MINActy
            for tyh in acty:
                if(tyh[-1]==MINActy and tyh[0]%1==0):
                    pass
                else:
                    maxActy=max(maxActy,max(tyh))
            return maxActy

    def uncut(self):
        lhacty=self.__localActy
        actysh=[MINActy]
        for a in lhacty:
            if(len(a)==2 and a[-1]==MINActy):
                for i in range(a[0]):
                    actysh.append(MINActy)
            else:
                for ai in a:
                    actysh.append(ai)
        return actysh

    def CutArrByMonth(self,arr,fday,lday):
        if(len(arr)!=((lday-fday).days+1)):
            # print(self.__id)
            # print(len(arr[1:]),((lday-fday).days+1))
            return [MINActy]
        else:
            maxActy,monthMax,nday,nmonth=MINActy,[],fday,fday.month
            for i in range(len(arr)):
                if(nday.month==nmonth):
                    maxActy=max(maxActy,arr[i])
                else:
                    monthMax.append(maxActy)
                    maxActy=max(MINActy,arr[i])
                    nmonth=nday.month
                nday=nday+datetime.timedelta(days=1)
        if(nday.day!=calendar.monthrange(nday.year,nday.month)):
            monthMax.append(maxActy)
        #print(monthMax)
        return monthMax

    def apiForErgidic(self):
        fdayStr=self.__fday.strftime("%Y-%m-%d")[:7]
        return fdayStr,self.__MaxMonthActy#,(self.__lday-self.__fday).days,self.__globalActy




idlist=get_idlist()
class Ergodic():
    # 系统遍历器,fady和lday用来指定遍历的时间范围,精确到月
    # 原则上时间范围的指定只是为了避免重复遍历，即时间范围对最终统计结果是没有影响的
    def __init__(self):
        self.__lRunMonth=max(0,1)
        self.__levelData=[[],[],[],[]]
        ad=datetime.datetime(2017,1,1)
        lday=ad
        monthList=[]
        while(lday<datetime.datetime(2020,7,1)):
            monthList.append(lday.strftime('%Y-%m-%d')[:7])
            lday=lday+datetime.timedelta(calendar.monthrange(lday.year,lday.month)[1])
            for i in range(4):
                self.__levelData[i].append(0)
        self.__monthList=monthList

    def load_data(self):
        with open(ROOTpath+"\\ergoDic.pickle") as f:
            Obj=pickle.load(f)
            f.close()
        self.__lRunMonth=Obj.getAll()

    def getLeveData(self):
        return self.__levelData

    def newDataAll(self,s,e):
        # idlist=["F1027613"]
        global finishUsers
        for uid in idlist[s:e]:
            nowUser=MiniUserActy(uid)
            fmonth,maxMonthActy=nowUser.apiForErgidic()
            i=0
            while(i<len(self.__monthList)):
                if(self.__monthList[i]==fmonth):
                    # print(i,self.__monthList[i])
                    break
                else:
                    i+=1
            if(i==len(self.__monthList)):
                continue
            else:
                for maxActy in maxMonthActy:
                    if i>=len(self.__levelData[indexByActy(maxActy)]):
                        print(uid,i,len(self.__monthList),fmonth)
                    else:
                        self.__levelData[indexByActy(maxActy)][i]+=1
                        i+=1
            finishUsers+=1
            # sys.stdout.write("\r"+"at %s"%uid)
            # sys.stdout.flush()
        # print(self.__levelData)
        # list2json(self.__levelData,"levelData.json")
        # list2json(self.__monthList,"monthList.json")


#继承threading.Thread类
class myThread1 (threading.Thread):
    def __init__(self,funct,*arg):
        threading.Thread.__init__(self)
        self.funct=funct
        self.arg=arg
    def run(self):
        # print(self.arg)
        self.funct(*self.arg)

# testU=MiniUserActy("G4945495")
# print(testU.apiForErgidic())
A=Ergodic()
B=Ergodic()
C=Ergodic()
# A.newDataAll(0,1)
def calcuAll(AA,s,e):
    AA.newDataAll(s,e)

def printNow():
    for i in range(1000):
        time.sleep(10)
        finishData1=A.getLeveData()
        finishData2=B.getLeveData()
        finishData3=C.getLeveData()
        finishData=np.add(finishData1,finishData2)
        finishData=np.add(finishData,finishData3)
        sys.stdout.write("\r"+"There is Finished %s users,with %s lv1,%s lv2,%s lv3,%s lv4"%(finishUsers,sum(finishData[0]),sum(finishData[1]),sum(finishData[2])
                                                                        ,sum(finishData[3])))
        sys.stdout.flush()


thread1 = myThread1(calcuAll,A,0,120000)
thread2=myThread1(calcuAll,B,120001,-1)
thread3=myThread1(calcuAll,C,166669,-1)
thread0 = myThread1(printNow)
thread1.start()
thread2.start()
thread3.start()
thread0.start()
thread1.join()
thread2.join()
thread3.join()
thread0.join()
finishData1=A.getLeveData()
finishData2=B.getLeveData()
finishData=np.add(finishData1,finishData2)
finishData=list(finishData)
list2json(finishData,"finishData.json")

