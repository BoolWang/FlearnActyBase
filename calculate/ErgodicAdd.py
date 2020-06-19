#遍历系统中所有用户，统计系统的活跃度情况
#具体包括，系统每月的活跃度分析情况
#          系统每周的活跃度分布情况
#还需要实例化所有用户的活跃度情况，通过聚类给活跃度定级
#还是需要全部学员的idList
from sql.mongo import getDataById
from bin.globalNUM import *

class MiniUserActy():
    # 从mongo数据库实例化用于遍历的简化版用户对象
    def __init__(self,uid):
        self.__id=uid
        self.__fday,self.__lday,self.__localActy=getDataById(uid)
        self.__maxActy=self.findMaxActy()
        self.__globalActy=self.uncut()

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




# class Ergodic():
#     # 系统遍历器,fady和lday用来指定遍历的时间范围,精确到月
#     # 原则上时间范围的指定只是为了避免重复遍历，即时间范围对最终统计结果是没有影响的
#     def __init__(self,fady,lday):


