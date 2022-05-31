from runners import m_login
import requests
import json

def get_insert_code():
        url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_APPOINTAUDIT_M/cardAdd.json'

        #caseinfo['data'] =data
        mheaders = m_login.mlogin(1, 1, 1)
        #headers = datas.headers
        #cookies = pc_login.cookies
        #testsuitm.append(caseinfo.copy())
        rs = requests.get(url=url, headers=mheaders)
        # 返回值转码
        data = rs.content.decode('utf-8')
        # json化
        data = json.loads(data)
        # 获取接口返回状态
        #print("data", data)
        sta = data['status']
        # if caseinfo['id'] == 100:
        insert = data['data']['data']['insert__']
        return insert
        #print('获取insertid',sta)
        #workticketidxxx = workticketid +1


def get_insert_code1():
        url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORKAPPLY_MCQ_M/cardAdd.json'
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