from useracty.UserActy import *
from sql.StudyH import select_all_id,sqlbyid
from sql.mongo import get_actyh,getclient
from bin.json_io import get_idlist
import sys
from bin.globalNUM import *
#
# #由id盘点未曾计算过的用户活跃度,并对计算结果进行存储
# idlist=select_all_id()
# for uid in idlist:
#     Me=UserActy(id=uid)
#     Me.newsh()
#     Me.cutsh()
#     Me.get2mongo()
#     sys.stdout.write('\r' + "at %s"%uid)
#     sys.stdout.flush()
#
# print(len(idlist))
# #由id和盘点好的用户活跃度表进行按日更新
#at C3406949
idlist=get_idlist()
l=len(idlist)
sums=1
print(9)
for uid in idlist:
    Me=UserActy(id=uid)
    Me.newsh()
    Me.cutsh()
    Me.get2mongo()
    #Me.tprint()
    sys.stdout.write('\r' + "at %s,%s of s%"%(uid,sums,l))
    sys.stdout.flush()
    sums+=1
# for i in range(len(idlist)):
# uid="A0100001"
# a=getclient()
# mycol=a[DBname][COLname]
# rs=mycol.find_one({})
# me=UserActy(uid)
# print(me.check())
