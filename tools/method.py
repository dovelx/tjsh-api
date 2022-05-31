import requests
import json
from tools import assert0
from globalpkg.global_var import logger

def gh(caseinfo,headers,cookies):
    '''get 返回为html'''
    rs = requests.get(url=caseinfo['url'], headers=headers, cookies=cookies)
    sta = rs.status_code
    if sta == 200:
        # 返回值转码
        data = rs.content.decode('utf-8')
        #print(data)
        #logger.info('返回数据：%s' % data)
        if caseinfo['exresult'] != "":
            # print("预期结果不为空，开始比对预期结果")

            response_to_check = str(data)
            expected_result = caseinfo['exresult']
            for item in expected_result['条件']:
                pattern_str = item['模式']

                logger.info('要匹配的模式（正则表达式）为：%s' % pattern_str)
                a = assert0.assertRegex(response_to_check, pattern_str, msg=item['消息'])
                if a == 1:
                    caseinfo['result'] = "pass"
                    return caseinfo['result']
                    break
                else:
                    caseinfo['result'] = "fail"
                    return "：失败，预期与实际结果不符"
        else:
            # print("预期结果为空，不做比对")
            caseinfo['result'] = "pass"
            return caseinfo['result']

    else:
        data = rs.content.decode('utf-8')
        caseinfo['result'] = "fail"
        return data


def get(caseinfo,headers,cookies):
    '''get 返回为Json'''
    rs = requests.get(url=caseinfo['url'], headers=headers, cookies=cookies,verify=False)
    if rs.status_code == 200:
        # 返回值转码
        data = rs.content.decode('utf-8')
        # json化
        data = json.loads(data)
        #logger.info('返回数据：%s' % data)
        # 获取接口返回状态
        sta = data['status']
        if sta == 3200:
            caseinfo['result'] = "pass"
            return caseinfo['result']
            # if caseinfo['exresult'] != "":
            #     #print("预期结果不为空，开始比对预期结果")
            #
            #     response_to_check = str(data)
            #     expected_result = caseinfo['exresult']
            #     for item in expected_result['条件']:
            #         pattern_str = item['模式']
            #         # logger.info('要匹配的模式（正则表达式）为：%s' % pattern_str)
            #         a=assert0.assertRegex(response_to_check, pattern_str, msg=item['消息'])
            #         if a==1:
            #             caseinfo['result'] = "pass"
            #             return caseinfo['result']
            #             break
            #         else:
            #             caseinfo['result'] = "fail"
            #             return "：失败，预期与实际结果不符"
            # else:
            #     #print("预期结果为空，不做比对")
            #     caseinfo['result'] = "fail"
            #     return caseinfo['result']
        else:
            caseinfo['result'] = "fail"
            return data
    else:
        return rs.status_code

def pa(caseinfo,headers,cookies):
    '''post 返回为json'''
    #print(caseinfo['data'])
    rs = requests.post(url=caseinfo['url'], json=caseinfo['data'], headers=headers, cookies=cookies,verify=False)
    if rs.status_code == 200:
        #print("rs",rs.content)
        # 返回值转码
        data = rs.content.decode('utf-8')
        # json化
        data = json.loads(data)
        # 获取接口返回状态
        sta = data['status']
        if sta == 3200:
            #print("作业预约成功", sta)
            caseinfo['result'] = "pass"
            return caseinfo['result']
        else:
            caseinfo['result'] = "fail"
            return data
    else:
        caseinfo['result'] = "fail"
        return rs.status_code

def pd(caseinfo,headers):
    '''post 返回为json'''

    data = str(caseinfo['data']).encode("utf-8").decode("latin1")
    print("即将请求", data)
    #rs = requests.post(url=caseinfo['url'], data=caseinfo['data'], headers=headers, cookies=cookies)
    rs = requests.request("POST", url=caseinfo['url'], headers=headers, data = data)
    if rs.status_code == 200:
        #print("rs",rs.content)
        # 返回值转码
        #print(rs.text.encode('utf8'))
        data = rs.content.decode('utf-8')
        #data = rs.text.encode('utf8')
        print(data)
        # json化
        data = json.loads(data)
        # 获取接口返回状态
        sta = data['status']
        if sta == 3200:
            #print("作业预约成功", sta)
            caseinfo['result'] = "pass"
            return caseinfo['result']
        else:
            caseinfo['result'] = "fail"
            return data
    else:
        caseinfo['result'] = "fail"
        return rs.status_code

def pm(caseinfo,mheaders):
    '''移动端 post'''
    rs = requests.post(url = caseinfo['url'],json=caseinfo['data'],headers=mheaders)
    if rs.status_code ==200:
        # 返回值转码
        data = rs.content.decode('utf-8')
        #json格式化
        data = json.loads(data)
        # 获取接口返回状态
        sta = data['status']
        if sta == 3200:
            # print("作业预约成功", sta)
            caseinfo['result'] = "pass"
            return caseinfo['result']
        else:
            caseinfo['result'] = "fail"
            return data
    else:
        return rs.status_code


def gm(caseinfo,headers):
    '''移动端 get'''
    rs = requests.get(url=caseinfo['url'], headers=headers)
    if rs.status_code == 200:
        # 返回值转码
        data = rs.content.decode('utf-8')
        # json化
        data = json.loads(data)
        # 获取接口返回状态
        sta = data['status']
        if sta == 3200:
            if caseinfo['exresult'] != "":
                response_to_check = str(data)
                expected_result = caseinfo['exresult']
                for item in expected_result['条件']:
                    pattern_str = item['模式']
                    # logger.info('要匹配的模式（正则表达式）为：%s' % pattern_str)
                    a=assert0.assertRegex(response_to_check, pattern_str, msg=item['消息'])
                    if a==1:
                        caseinfo['result'] = "pass"
                        return caseinfo['result']
                        break
                    else:
                        caseinfo['result'] = "fail"
                        return "：失败，预期与实际结果不符"
            else:
                #print("预期结果为空，不做比对")
                caseinfo['result'] = "pass"
                return caseinfo['result']
        else:
            caseinfo['result'] = "fail"
            return data
    else:
        return rs.status_code