#pickle文件的读写
import pickle
from bin.globalNUM import *

#INPUT By ID and data
def ipicklebyid(id,data):
    with open(ROOTpath+"//"+"%s.pickle"%id,"wb") as f:
        pickle.dump(data,f)
        f.close()

#Get data by id
def opiclebyid(id):
    with open(ROOTpath+"//"+"%s.pickle"%id,"rb") as f:
        data=pickle.load(f)
        f.close()
    return data
