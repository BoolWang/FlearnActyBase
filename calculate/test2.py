from useracty.UserActy import *
from sql.StudyH import select_all_id,sqlbyid
from sql.mongo import get_actyh,getclient
from bin.json_io import get_idlist
from calculate.ErgodicAdd import MiniUserActy
import matplotlib.pyplot as plt
from sklearn.cluster import k_means
from sklearn.metrics import silhouette_score
import sys
from bin.globalNUM import *
import random
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
# at WLT00001 (246471 OF 246473)
idlist=get_idlist()
SetMaxActy=[]
def random_list(a,b,n):
    import numpy as np
    import random
    arr=np.arange(a,b,1)
    random.shuffle(arr)
    return sorted(arr[:n])
indx=random_list(0,len(idlist),1)
for i in range(1):
    Me=MiniUserActy(idlist[indx[i]])
    # Me.findMaxMothActy()
    SetMaxActy.append([Me.findMaxActy(),1])
    # plt.scatter(i,Me.findMaxActy())
# plt.show()
# model =k_means(SetMaxActy, n_clusters=3)
# score=silhouette_score(SetMaxActy, model[1])
# print(model,'/r',score)
# label=model[1]
# maxA,maxB,maxC=0,0,0
# sumA,sumB,sumC=0,0,0
# for i in range(10):
#     if(label[i]==0):
#         maxA=max(maxA,SetMaxActy[i][0])
#         sumA+=1
#         plt.scatter(SetMaxActy[i][0],SetMaxActy[i][1],c='red')
#     elif(label[i]==1):
#         maxB=max(maxB,SetMaxActy[i][0])
#         sumB+=1
#         plt.scatter(SetMaxActy[i][0],SetMaxActy[i][1],c='black')
#     # elif(label[i]==2):
#     #     plt.scatter(SetMaxActy[i][0],SetMaxActy[i][1],c='blue')
#     else:
#         maxC=max(maxC,SetMaxActy[i][0])
#         sumC+=1
#         plt.scatter(SetMaxActy[i][0],SetMaxActy[i][1],c='green')
# plt.show()
# print(maxA,sumA)
# print(maxB,sumB)
# print(maxC,sumC)