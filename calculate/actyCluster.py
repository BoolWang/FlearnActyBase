#对打标范围的一个科学划分
from bin.json_io import get_idlist
from calculate.ErgodicAdd import MiniUserActy
import matplotlib.pyplot as plt
from sklearn.cluster import k_means
from sklearn.metrics import silhouette_score

idlist=get_idlist()
SetMaxActy=[]
def random_list(a,b,n):
    import numpy as np
    import random
    arr=np.arange(a,b,1)
    random.shuffle(arr)
    return sorted(arr[:n])
indx=random_list(0,len(idlist),1000)
for i in range(1000):
    Me=MiniUserActy(idlist[indx[i]])
    SetMaxActy.append([Me.findMaxActy(),1])
    # plt.scatter(i,Me.findMaxActy())
# plt.show()
model =k_means(SetMaxActy, n_clusters=3)
score=silhouette_score(SetMaxActy, model[1])
print(model,'/r',score)
label=model[1]
maxA,maxB,maxC=0,0,0
sumA,sumB,sumC=0,0,0
for i in range(1000):
    if(label[i]==0):
        maxA=max(maxA,SetMaxActy[i][0])
        sumA+=1
        plt.scatter(SetMaxActy[i][0],SetMaxActy[i][1],c='red')
    elif(label[i]==1):
        maxB=max(maxB,SetMaxActy[i][0])
        sumB+=1
        plt.scatter(SetMaxActy[i][0],SetMaxActy[i][1],c='black')
    # elif(label[i]==2):
    #     plt.scatter(SetMaxActy[i][0],SetMaxActy[i][1],c='blue')
    else:
        maxC=max(maxC,SetMaxActy[i][0])
        sumC+=1
        plt.scatter(SetMaxActy[i][0],SetMaxActy[i][1],c='green')
plt.show()
print(maxA,sumA)
print(maxB,sumB)
print(maxC,sumC)

# 33.6242 648
# 481.9515528000002 33
# 110.07294350000004 319