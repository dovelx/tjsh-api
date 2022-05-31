import  requests
import json

def get_work_appoint_id(cookies,name):
    from runners import pc_login
    cookies = pc_login()
    #作业预约ID获取
    url1 = 'http://192.168.6.156/hse/HSE_WORK_APPOINT/getMetaData?0.3897117454385264&contentType=json&ajax=true&tid=1'
    #请求头
    headers={
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'csrf': '6363382b59f6435eb243fab57ea5a5e0',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'Content-Type': 'text/plain',
        }

    #请求接口
    rs=requests.get(url1, headers = headers,cookies=cookies)
    if rs.status_code == 200:
        #返回值转码name
        data = rs.content.decode('utf-8')
        #json格式化
        data = json.loads(data)
        #获取接口返回状态
        status= data['status']
        if status == 3200:
            print("获取列表成功", status)
            #获取本次作业预约的work_appoint_id
            data = data['data']['voset']['voList']
            #print(data)
            temp = []
            for a in data:
                #print("\n\n",a)
                if a['workname']  == name:
                    temp.append(a['work_appoint_id'])
            work_appoint_id = temp[0]
            #当前最大work_appoint_id加1
            #work_appoint_id =work_appoint_id+1
            print("work_appoint_idx",work_appoint_id)
            return work_appoint_id
        else:
              print("fail")


def get_work_ticket_id(cookies,name):
    # 作业任务列表接口地址

    url = 'http://192.168.6.156/hse/HSE_WORK_TASK_MCQ/getMetaData?0.9361492698096476&contentType=json&ajax=true&tid=1'
    # 请求头
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'csrf': '6363382b59f6435eb243fab57ea5a5e0',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'Content-Type': 'text/plain',
    }
    # 请求接口
    rs = requests.get(url, headers=headers, cookies=cookies)
    if rs.status_code == 200:
        # 返回值转码
        data = rs.content.decode('utf-8')
        # json格式化
        data = json.loads(data)
        # 获取接口返回状态
        status = data['status']
        if status == 3200:
            print("获取列表成功", status)
            # 获取本次作业预约的work_appoint_id
            data = data['data']['voset']['voList']
            # print(data)
            temp = []
            for a in data:
                # print("\n\n",a)
                if a['workname'] == "Created_by_Python_ImzgJq":
                    temp.append(a['work_appoint_id'])
            work_appoint_id = temp[0]
            # 当前最大work_appoint_id加1
            work_ticket_idx = work_appoint_id + 1
            print("work_ticket_idx", work_ticket_idx)
            return
        else:
            print("fail")


def get_work_task_id(cookies,name):
    # 作业任务列表接口地址

    url = 'http://192.168.6.156/hse/HSE_WORK_TASK_MCQ/getMetaData?0.9361492698096476&contentType=json&ajax=true&tid=1'
    # 请求头
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'csrf': '6363382b59f6435eb243fab57ea5a5e0',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'Content-Type': 'text/plain',
    }
    # 请求接口
    rs = requests.get(url, headers=headers, cookies=cookies)
    if rs.status_code == 200:
        # 返回值转码
        data = rs.content.decode('utf-8')
        # json格式化
        data = json.loads(data)
        # 获取接口返回状态
        status = data['status']
        if status == 3200:
            print("获取列表成功", status)
            # 获取本次作业预约的work_appoint_id
            data = data['data']['voset']['voList']
            # print(data)
            temp = []
            for a in data:
                # print("\n\n",a)
                if a['workname'] == name:
                    temp.append(a['worktaskid'])
                    worktaskidt = temp[0]
            # 当前最大work_appoint_id加1
                    #worktaskid = worktaskid + 1
            print("worktaskid", worktaskidt)
            return worktaskidt
        else:
            print("fail")
            return 0

def get_safe_task_id(cookies,name):
    # 安全分析列报表
    url = 'http://192.168.6.156/hse/HSE_SAFETY_TASK_RISK/getMetaData?0.1772610700060453&contentType=json&ajax=true&tid=1'
    # 请求头
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'csrf': '6363382b59f6435eb243fab57ea5a5e0',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'Content-Type': 'text/plain',
    }
    # 请求接口
    rs = requests.get(url, headers=headers, cookies=cookies)
    if rs.status_code == 200:
        # 返回值转码
        data = rs.content.decode('utf-8')
        # json格式化
        data = json.loads(data)
        # 获取接口返回状态
        status = data['status']
        if status == 3200:
            print("获取安全分析列表成功", status)
            # 获取本次作业预约的work_appoint_id
            data = data['data']['voset']['voList']
            # print("data",data)
            temp = []
            for a in data:
                # print("\n\n",a)
                if a['work_appoint_name'] == name:
                    # print(a)
                    temp.append(a['worktaskid'])
            worktaskid = temp[0]
            # 当前最大work_appoint_id加1
            # work_ticket_idx =worktaskid+1
            print("worktaskid", worktaskid)
            return worktaskid
        else:
            print("fail")
            return 0


if __name__ == '__main__':

    print("tired")
