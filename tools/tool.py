import random
import string
import datetime
import os
import execjs

#作业预约作业任务名称随机数生成函数
def ran_name_with_str():
    salt = ''.join(random.sample(string.ascii_letters+string.digits,6))
    now = datetime.datetime.now()
    salt = now.strftime("%Y-%m-%d %H:%M:%S")
    name = "Created_by_David_" + salt
    return  name

def getEntryPwd(encryptType,pwd,modulus,publicExponent):
    # 返回加密后的密码
    path=os.path.abspath(os.path.dirname(__file__))
    file=os.path.join(path,'./hdEncrypt_merge.js')
    #logging.debug("path:%s"%path)
    data=open(file,'r',encoding= 'utf8').read()
    jss=execjs.compile(data)
    #logging.debug(jss)
    return  jss.call("login",encryptType,pwd,modulus,publicExponent)

#获取当前时间，为作业预约提供时间变量
now = datetime.datetime.now()
now1 = now + datetime.timedelta(minutes=15)
now2 = now + datetime.timedelta(minutes=120)
#now3 = now + datetime.timedelta(minutes=50)
starttime = now1.strftime("%Y-%m-%d %H:%M:%S")
endtime = now2.strftime("%Y-%m-%d %H:%M:%S")
#mendtime = now3.strftime("%Y-%m-%d %H:%M:%S")
now =now.strftime("%Y-%m-%d %H:%M:%S")
print("now",now)