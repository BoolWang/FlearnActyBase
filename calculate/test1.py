import pymysql
import pandas as pd
import datetime
import time
from bin.globalNUM import *
from sql.mongo import getDataById

lo=[[3.5,6,9,12],[25,2.5]]
def uncut(localActy):
    lhacty=localActy
    actysh=[MINActy]
    for a in lhacty:
        if(len(a)==2 and a[-1]==MINActy):
            for i in range(a[0]):
                actysh.append(MINActy)
        else:
            for ai in a:
                actysh.append(ai)
    return actysh
print(uncut(lo))