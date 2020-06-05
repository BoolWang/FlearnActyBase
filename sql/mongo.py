#mongodb的读写
import pymongo as pmg
from bin.globalNUM import *

def getclient():
    return pmg.MongoClient(host=MONGOhost,port=MONGOport,username=USERname,password=USERpwd,authSource="admin")

#存储文档到userActy
def doc2mongo(doc):
    myclient=getclient()
    mycol=myclient[DBname][COLname]
    mycol.insert_one(doc)
    return

#按照用户id读取文档中的历史活跃度
def get_actyh(id):
    myclient=getclient()
    mycol=myclient[DBname][COLname]
    result=mycol.find_one({"uid":id})
    return result

def updata_actyh(id,nowacty):
    myclient=getclient()
    mycol=myclient[DBname][COLname]
    oldresult=get_actyh(id)["actyh"]
   #print("old:%s"%oldresult)
    oldresult.append(nowacty)
    newresult=oldresult
    #print("new:%s"%newresult)
    mycol.update_one({"uid":id},{"$set":{"actyh":newresult}})

