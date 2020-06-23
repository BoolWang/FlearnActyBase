import json
from bin.globalNUM import *

#将列表保存为json格式
def list2json(lis,path):
    with open(ROOTpath+'\\'+path,"w") as f:
        json.dump(lis,f)
        f.close()

#从json文件中读取用户id列表
def get_idlist(k):
    with open(ROOTpath+'\\idlist.json') as f:
        userli=json.load(f)
        f.close()
    userli1=list(filter(lambda x:x[0]==k,userli))
    return userli1

uc=get_idlist("C")
print(uc)

#更新用户id到json文件中去
def updata_idlist(id):
    with open(ROOTpath+'\\idlist.json') as f:
        userli=json.load(f)
        f.close()
    if(id in userli):return
    else:
        userli.append(id)
        userli.sort()
        list2json(userli,ROOTpath+'\\idlist.json')