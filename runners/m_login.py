import requests
from tools import tool
import json

def mlogin (host,username,password):
    host = "https://tjsh.ushayden.com"
    #移动端登录
    url = "/m/passport/login/getEncryptType.json"
    url = host + url
    #url = "http://192.168.6.27:6030/m/passport/login/getEncryptType.json"
    headers ={
	'Host': 'tjsh.ushayden.com',
	'Accept-Encoding': 'gzip',
	'User-Agent': 'okhttp/3.8.0',
	'Connnection': 'Keep-Alive'
}
    sr = requests.get(url,headers=headers,verify= False)

    eq = sr.json()

    print("eq",eq)
    url1 ="/m/passport/login/login.json"
    url1 = host + url1
    #url1 ="http://192.168.6.27:6030/m/passport/login/login.json"
    USER_NAME = username
    USER_NAME = "weiw263"
    password ="123456"
    loginStoken=eq['data']['loginStoken']
    encryptType=eq['data']['encryptType']
    modulus = eq['data']['pubKeyVO']['modulus']
    publicExponent = eq['data']['pubKeyVO']['publicExponent']
    pwd = tool.getEntryPwd(encryptType,password,modulus,publicExponent)

    headers={
	'Host': 'tjsh.ushayden.com',
	'Accept': 'application/json',
	'Content-Type': 'application/json',
	'Content-Length': '447',
	'Accept-Encoding': 'gzip',
	'User-Agent': 'okhttp/3.8.0',
	'Connnection': 'Keep-Alive'
}

    data={
	"appVersion": "01.22.0531",
	"equipmentCode": "867254028770522",
	"ip": "192.168.2.2",
	"isAD": "true",
	"loginStoken": loginStoken,
	"password": pwd,
	"username": USER_NAME,
	"verifyPwd": pwd
}

    rs= requests.post(url=url1,json =data,headers = headers,verify=False)

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
        "user-agent": "RS801D(Android/7.0) (com.hayden.hap.fv/1.0.2) Weex/0.16.0 1080x1920",
        "Content-Type": "application/json;charset=UTF-8",
        "st": loginStoken,
        "tid": "2000000002404"

    }
    print(headers)
    return  headers

def mllogin (host,username,password):
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "user-agent": "RS801D(Android/7.0) (com.hayden.hap.fv/1.0.2) Weex/0.16.0 1080x1920",
        "Content-Type": "application/json;charset=UTF-8",
        "st": "m_login_user_stoken_ff25244c5400427a8859bd4eef65fe57",
        "tid": "2000000002404"

    }
    print(headers)
    return  headers
if __name__=='__main__':
    mlogin(1,2,3)


