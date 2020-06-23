from bin.globalNUM import *

def indexByActy(acty):
    if(acty==MINActy):return 0
    elif(acty<=Lv1):return 1
    elif(acty<=Lv2):return 2
    else:return 3