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
            print(arr[0])
            print(len(arr[1:]),((lday-fday).days+1))
            return
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
        return fdayStr,self.__MaxMonthActy





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

    def newDataAll(self,k):
        idlist=get_idlist(k)
        for uid in idlist[300:600]:
            nowUser=MiniUserActy(uid)
            fmonth,maxMonthActy=nowUser.apiForErgidic()
            i=0
            while(i<len(self.__monthList)):
                if(self.__monthList[i]==fmonth):
                    break
                else:
                    i+=1
            for maxActy in maxMonthActy:
                self.__levelData[indexByActy(maxActy)][i]+=1
                i+=1
        print(self.__levelData)
        list2json(self.__levelData,"levelData.json")
        list2json(self.__monthList,"monthList.json")



