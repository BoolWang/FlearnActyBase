import json
from bin.globalNUM import *
from bin.json_io import list2json
from sql.StudyH import sqlbyid_days
import datetime

# with open(ROOTpath+'\\idlist.json') as f:
#     userli=json.load(f)
#     f.close()
# lis=userli["rows"]
# lis1=[]
# for li in lis:
#     lis1.append(li[0])
# list2json(lis1,ROOTpath+'\\idlist.json')
# fday=datetime.datetime.strptime("2019-07-12","%Y-%m-%d")
# lday=datetime.datetime.strptime("2020-06-12","%Y-%m-%d")
# a=sqlbyid_days("F3235939",fday,lday)
# print(a)
# print(fday)
# print(fday.strftime("%Y-%m-%d"))
today=datetime.datetime.today()
today=today+datetime.timedelta(days=1)
print(today.strftime("%Y-%m-%d"))
print(sqlbyid_days("A0100001",datetime.datetime.strptime("2018-03-12","%Y-%m-%d"),today))
print(80*1024)