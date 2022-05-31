def getinsert():

    import requests
    import json
    from runners import m_login
    from tools import datas
    case = '获取手机预约添加insertid'

    #用例信息变量定义
    testsuitm = []
    caseinfo = {}
    caseinfo['id'] = 1
    caseinfo['name'] = ''
    caseinfo['result'] = ""
    caseinfo['url'] = ''
    caseinfo['data'] = ''
    caseinfo['sign'] =''
    caseinfo['flag'] = ''
    caseinfo['isactive'] = ''

    #ps
    mheaders = m_login.mlogin(1, 1, 1)
    headers = datas.headers

    #cases
    caseinfo['id'] = 100
    caseinfo['name'] = '获取insertid'
    caseinfo['flag'] = 'get'
    url = 'http://192.168.6.156/m/hse_m/HSE_WORK_APPOINTAUDIT_M/cardAdd.json'

    rs = requests.get(url=url, headers=mheaders)
    # 返回值转码
    data = rs.content.decode('utf-8')
    # json化
    data = json.loads(data)
    # 获取接口返回状态

    sta = data['status']
    if sta == 3200:
        caseinfo['result'] = "pass"
    else:
        caseinfo['result'] = "Fail"

    insert = data['data']['data']['insert__']

    print('获取insertid',sta)
    return insert

def get_insert_code():
    import requests
    import json
    from runners import m_login
    url = 'http://192.168.6.156/m/hse_m/HSE_WORKAPPLY_MCQ_M/cardAdd.json'
    mheaders = m_login.mlogin(1, 1, 1)
    rs = requests.get(url=url, headers=mheaders)
    # 返回值转码
    data = rs.content.decode('utf-8')
    # json化
    data = json.loads(data)
    # 获取接口返回状态
    # print("data", data)
    sta = data['status']
    # if caseinfo['id'] == 100:
    insert = data['data']['data']['insert__']
    return insert


if __name__ == '__main__':

    print(get_insert_code())