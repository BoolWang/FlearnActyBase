#mongodb的读写
import pymongo as pmg
from bin.globalNUM import *

def getclient():
    client=pmg.MongoClient("mongodb://"+MONGOhost+":"+str(MONGOport)+"/")
    db=client[DBname]
    db.authenticate(USERname,USERpwd)
    return db[COLname]
mycol=getclient()

#存储文档到userActy
def doc2mongo(doc):
    # mycol=getclient()
    mycol.insert_one(doc)
    return

#按照用户id读取文档中的历史活跃度
def get_actyh(id):
    # mycol=getclient()
    result=mycol.find_one({"uid":id})
    return result

def updata_actyh(id,nowacty):
    # mycol=getclient()
    oldresult=get_actyh(id)["actyh"]
   #print("old:%s"%oldresult)
    oldresult.append(nowacty)
    newresult=oldresult
    #print("new:%s"%newresult)
    mycol.update_one({"uid":id},{"$set":{"actyh":newresult}})

def getDataById(uid):
    # client=pmg.MongoClient("mongodb://"+MONGOhost+":"+str(MONGOport)+"/")
    result=get_actyh(uid)
    return result["fday"],result["lday"],result["actyh"]
