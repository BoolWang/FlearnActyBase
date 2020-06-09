import datetime
from bin.time_str import get_now
from useracty.ActyRuler import onebyone,daybyday
from sql.StudyH import sqlbyid,sqlbyid_days
from bin.globalNUM import *
from sql.mongo import doc2mongo,get_actyh



class UserActy():
    def __init__(self,id,fday=get_now(),lday=get_now()):
        if(get_actyh(id) is not None):
            print("用户%s已存在，正在从数据库中加载"%id)
            result=get_actyh(id)
            self.__id,self.__fday,self.__lday,self.__local_actyh\
                =result["uid"],result["fday"],result["lday"],result["actyh"]
            self.__isprotect=result["isprotect"]
            self.__loosdays,self.__condays=result["loosday"],result["condays"]
            self.uncut()

        else:
            self.__id=id    #用户id工号
            self.__fday,self.__lday=fday,lday   #用户第一次和最后一次学习的日期
            self.__acty,self.__max_acty,self.__local_max_acty,self.__actysh,self.__local_actyh\
                =0,0,0,[MINActy],[[MINActy]]  #用户的当前活跃度，历史最大活跃度，当前学习周期的最大活跃度,历史活跃度,学习周期活跃度
            self.__condays,self.__loosdays=0,0   #用户连续（未）学习天数
            self.__isprotect=0  #活跃度保护机制是否开启

    #通过历史学习记录来计算历史活跃度变化情况，sh是学习记录字典（日期：学习时长）
    #这一部分不考虑活跃度保护机制
    def newsh(self):
        sh=sqlbyid(self.__id)
        self.__actysh,self.__fday,self.__lday,self.__loosdays,self.__condays=onebyone(sh)
        self.cutsh()

    #这一部分为按每日的学习行为进行更新活跃度
    def updatash(self, today):
        #先计算天数差
        dtdays=(today-self.__lday).days
        if(dtdays<=0):
            print("已是最新记录，不用更新")
        else:
            today=today+datetime.timedelta(days=1)
            dtsh=sqlbyid_days(self.__id,self.__lday,today)
        a,b=self.__loosdays,self.__condays
        self.__actysh,self.__lday,self.__loosdays,self.__condays=daybyday(self.__actysh,dtsh,a,b)
        self.cutsh()

    #检测用户当前状态，包括是否更新过历史活跃度、是否开启活跃度保护机制、是否在数据库中有存档
    #是否有新增学习记录，历史活跃度是否更新到最新today
    def check(self):
        checkli=[self.__loosdays!=0 or self.__condays!=0,self.__isprotect,
                 get_actyh(self.__id) is not None,
                 bool(sqlbyid_days(self.__id,self.__lday,datetime.datetime.today()) !={}),
                 self.__lday.strftime("%Y-%m-%d")==datetime.datetime.today().strftime("%Y-%m-%d")]
        return checkli


    #按照历史活跃度进行学习周期切分
    def cutsh(self):
        newsh,sh=[[]],self.__actysh[1:]
        b=MINActy+1
        for a in sh:
            if(a>MINActy):
                if(b>MINActy):
                    newsh[-1].append(a)
                else:
                    newsh.append([a])
            else:
                if(b<=MINActy):
                    newsh[-1][0]+=1
                else:
                    newsh.append([1,MINActy])
            b=a
        self.__local_actyh=newsh

    def uncut(self):
        lhacty=self.__local_actyh
        acty,localmaxacty=lhacty[-1][-1],self.isstudy(lhacty[-1])
        maxacty=MINActy
        for a in lhacty:
            maxacty=max(maxacty,self.isstudy(a))
        actysh=[MINActy]
        for a in lhacty:
            if(len(a)==2 and a[-1]==MINActy):
                for i in range(a[0]):
                    actysh.append(MINActy)
            else:
                for ai in a:
                    actysh.append(ai)
        self.__acty,self.__max_acty,self.__local_max_acty,self.__actysh=acty,maxacty,localmaxacty,actysh

    def isstudy(self,b):
        if(len(b)==2 and b[-1]==MINActy):
            return MINActy
        else:
            return max(b)


    def get2doc(self):
        doc={"uid":self.__id,"actyh":self.__local_actyh,
             "fday":self.__fday,"lday":self.__lday,
             "loosday":self.__loosdays,"condays":self.__condays,
             "isprotect":self.__isprotect
             }
        return doc

    def get2mongo(self):
        doc2mongo(self.get2doc())

#一键刷新功能,逻辑上就是将当前用户的所有属性更新到最新，
    # 包括数据库中的数据也会进行更新
    def refresh(self):
        checkli=self.check()




    #def updatabytoday(self):


    def tprint(self):
        print(self.__id,self.__actysh)
        print(self.__local_actyh)
