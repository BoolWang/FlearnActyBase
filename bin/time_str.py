#该文档存储所有关于时间的操作
import datetime

#返回固定格式的今天的日期datetime类对象
def get_now(fmt='ymd'):
    if(fmt=='ymd'):
        now=datetime.datetime.today().__format__("%Y-%m-%d")
        return datetime.datetime.strptime(now,"%Y-%m-%d")
    else:
        return datetime.datetime.today()

#print(get_now())

#提取时间的日期
def get_date(ortime):
    return datetime.datetime.strptime(ortime.strftime("%Y-%m-%d"),"%Y-%m-%d")