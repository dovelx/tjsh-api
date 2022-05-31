import requests
from tools import tool
import json

def mlogin (host,username,password):
    host = "192.168.6.27:6030"
    #移动端登录
    url = "http://v3-test-linux-m-passport.hd-cloud.com/m/passport/login/getEncryptType.json"
    #url = "http://192.168.6.27:6030/m/passport/login/getEncryptType.json"
    headers ={
	'Host': 'v3-test-linux-m-passport.hd-cloud.com',
	'Accept-Encoding': 'gzip',
	'User-Agent': 'okhttp/3.8.0',
	'Connnection': 'Keep-Alive'
}
    sr = requests.get(url,headers=headers)

    eq = sr.json()

    print("eq",eq)
    url1 ="http://v3-test-linux-m-passport.hd-cloud.com/m/passport/login/login.json"
    #url1 ="http://192.168.6.27:6030/m/passport/login/login.json"
    USER_NAME = username
    USER_NAME = "admin2021"
    password ="123456"
    loginStoken=eq['data']['loginStoken']
    encryptType=eq['data']['encryptType']
    modulus = eq['data']['pubKeyVO']['modulus']
    publicExponent = eq['data']['pubKeyVO']['publicExponent']
    pwd = tool.getEntryPwd(encryptType,password,modulus,publicExponent)

    headers={
	'Host': 'v3-test-linux-m-passport.hd-cloud.com',
	'Accept': 'application/json',
	'Content-Type': 'application/json',
	'Content-Length': '447',
	'Accept-Encoding': 'gzip',
	'User-Agent': 'okhttp/3.8.0',
	'Connnection': 'Keep-Alive'
}

    data={"appVersion":"01.20.0619","loginStoken":loginStoken,"password":pwd,"username":USER_NAME,'tenantid':0}
    data = {
	"appVersion": "01.20.1113",
	"equipmentCode": "862523332779592",
	"loginStoken": loginStoken,
	"password": pwd,
	"tenantid": 2000000000453,
	"username": USER_NAME
}

    rs= requests.post(url=url1,json =data,headers = headers)

    cookies = requests.utils.dict_from_cookiejar(rs.cookies)

    #返回值转码
    data = rs.content.decode('utf-8')
    #json化
    data = json.loads(data)
    loginStoken = data['data']['st']
    #print(data)
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "user-agent": "ONEPLUS A6010(Android/10) (com.hayden.hap.fv/1.0.2) Weex/0.16.0 1080x2134",
        "Content-Type": "application/json;charset=UTF-8",
        "st": loginStoken,
        "tid": "2000000001003"

    }
    print(headers)
    return  headers

if __name__=='__main__':
    mlogin(1,2,3)


