from useracty.UserActy import *
from sql.StudyH import select_all_id,sqlbyid
from sql.mongo import get_actyh,getclient
from bin.json_io import get_idlist
import sys
from bin.globalNUM import *
# #
# # #由id盘点未曾计算过的用户活跃度,并对计算结果进行存储
# # idlist=select_all_id()
# # for uid in idlist:
# #     Me=UserActy(id=uid)
# #     Me.newsh()
# #     Me.cutsh()
# #     Me.get2mongo()
# #     sys.stdout.write('\r' + "at %s"%uid)
# #     sys.stdout.flush()
# #
# # print(len(idlist))
# # #由id和盘点好的用户活跃度表进行按日更新
# #at WLT00001 (246471 OF 246473)
nowindex=246471
idlist=get_idlist()
# l,sums=len(idlist),nowindex
# for uid in idlist[nowindex:]:
Me=UserActy(id='WLT00216')
Me.newsh()
Me.cutsh()
Me.get2mongo()
#Me.tprint()
# print(idlist[nowindex+3])