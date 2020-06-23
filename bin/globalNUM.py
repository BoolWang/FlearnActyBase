#需要用到的全局静态变量定义
chose=0
if(chose):
    MINActy=2.5 #最低活跃度，只要有过学习记录的人都有
    MAXtime=7200 #每日最大学习时长，超过该时长也按该时长算活跃度
    ROOTpath=r"H:\数据库相关"
    #mongo数据库相关信息
    MONGOhost="10.134.149.18"
    MONGOport=27017
    USERname="F3234721"
    USERpwd="3234721"
    DBname="discovery"
    COLname="userActy"
    #mysql相关信息
    SQLhost="10.134.149.182"
    SQLport=3306
    SQLuser='twbigdata'
    SQLpwd='20200304#'
    SQLdb='targetdb'
    SQLtable="log_data_Course_see_2"
    #活跃度等级划分
    Lv1=30
    Lv2=100

#需要用到的全局静态变量定义，测试版
else:
    MINActy=2.5 #最低活跃度，只要有过学习记录的人都有
    MAXtime=7200 #每日最大学习时长，超过该时长也按该时长算活跃度
    ROOTpath=r"E:\projectData\flearn"
    #mongo数据库相关信息
    MONGOhost="192.168.53.19"
    MONGOport=27017
    USERname="flearn"
    USERpwd="csu3216300."
    DBname="flearndb"
    COLname="userActy"
    #mysql相关信息
    SQLhost="192.168.43.80"
    SQLport=3306
    SQLuser='root'
    SQLpwd='csu3216300.'
    SQLdb='flearn'
    SQLtable="studyh"
    #活跃度等级划分
    Lv1=30
    Lv2=100
