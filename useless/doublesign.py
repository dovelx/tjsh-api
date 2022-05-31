import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import random
import string
import datetime
#大票和小票合并审核
#临时cookies
cookies={'JSESSIONID': 'F7F4B597A81664716FE28B267297190E30H8mW'}
#作业预约作业任务名称随机数生成函数
def ranstr(num):
    salt = ''.join(random.sample(string.ascii_letters+string.digits,num))
    return  salt
name = "Created_by_Python_"+ranstr(6)
print("作业预约名称",name)

#获取当前时间，为作业预约提供时间变量
now = datetime.datetime.now()
now1 = now + datetime.timedelta(minutes=5)
now2 = now + datetime.timedelta(minutes=10)
fnow1 = now1.strftime("%Y-%m-%d %H:%M:%S")
fnow2 = now2.strftime("%Y-%m-%d %H:%M:%S")
now =now.strftime("%Y-%m-%d %H:%M:%S")
#获取作业票id
from mobile import mydb
from globalpkg.global_var import logger

testdb = mydb.MyDB('./config/dbconfig.conf', 'CHANGQING')
'''
sql_update = 'UPDATE ' + case_step_report_tb + ' SET runresult=\"%s\",reason=\"%s\", protocol_method=\"%s\", runtime=\"%s\"' \
                                               ' WHERE executed_history_id = %s AND testcase_id = %s AND step_id = %s' \
                                               ' AND project=\'%s\' AND testplan=\'%s\''
data = ('Block', '%s' % e, protocol_method, run_time, str(case_executed_history_id), self.testcase_id, step_id,
        self.testproject, testplan)
'''
sql_query_ticket = 'select workticketid from hse_work_ticket order by workticketid desc limit 1'
sql_query_ts = 'select ts from hse_work_ticket order by ts desc limit 1'
sql_query_worktaskid = 'select worktaskid from hse_work_ticket ORDER BY worktaskid desc limit 1'
sql_query_work_appoint_id ='SELECT work_appoint_id from hse_safety_task ORDER BY  work_appoint_id desc LIMIT 1'
logger.info('正在更新步骤执行结果')
#testdb.execute_update(sql_update, data)
temp = testdb.select_one_record(sql_query_ticket)
#temp = temp.decode('utf-8')
workticketid = temp[0]
#作业票数据库当前ID
workticketid = workticketid[0]
print(workticketid)
temp = testdb.select_one_record(sql_query_ts)

print(temp)
ts = temp[0][0]
print(ts)
ts = ts.decode('utf-8')
#TS ID
tsi = int(ts)
print(ts)
temp = testdb.select_one_record(sql_query_worktaskid)
worktaskid = temp[0]
#worktaskid
worktaskid = worktaskid[0]
print(worktaskid)

temp = testdb.select_one_record(sql_query_work_appoint_id)
work_appoint_id = temp[0]
#worktaskid
work_appoint_id = work_appoint_id[0]
print("work_appoint_id",work_appoint_id)
testdb.close()
#暂时关闭登录
'''
#selenium登录测试长庆
driver = webdriver.Firefox()
driver.get("http://192.168.6.27:6030/passports/login?service=http%3A%2F%2F192.168.6.27%3A6030%2Fportals%2Fcas&tenantCode=cqsh&trial=false")

driver.find_element(By.ID, "username").send_keys("test")
driver.find_element(By.ID, "pwd1").send_keys("1")
driver.find_element(By.CSS_SELECTOR, ".justUse").click()

#获取JSESSIONID
c= driver.get_cookies()
#print (c)
#print (c[0])
for a in c:
    #print (a)
    if a['name'] == 'JSESSIONID':
        b=a
        #print (b)
cookies={'JSESSIONID': b['value']}

'''
print(cookies)
#用例信息变量定义
testsuit = []
caseinfo = {}

caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = 0


#预约列表用例信息
caseid = 1
casename = '预约列表接口获取'
count =1

caseinfo['id'] = caseid
caseinfo['name'] = casename

#预约列表接口地址
url1 = 'http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/getMetaData?0.3897117454385264&contentType=json&ajax=true&tid=1'
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
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())
#获取列表最大work_appoint_id
data = data['data']['voset']['voList']
temp = []
for a in data:
    temp.append(a['work_appoint_id'])
work_appoint_id = temp[0]
#当前最大work_appoint_id加1
c =work_appoint_id+1




#=====================开始作业预约
#用例信息

casename = '作业预约'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename
#拼写预约URL

num = c
print("作业预约列表NEW ID:",num)
url2='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.3707947936681053&contentType=json&ajax=true&tid=1'%(num,num)
#作业预约作业任务名称随机数生成函数
#print ("预约url\n",url2)

#作业预约请求头
headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'csrf': 'bd95a01c276341b89715228e81d0ca3f',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Content-Type': 'text/plain',
    }
#动火
formdatanew ={
	"tableName": "hse_work_appoint",
	"iscontractor": "0",
	"workunitname_no": "",
	"territorialunitid": 2000000003339,
	"worktaskid_no": 0,
	"isreport": "0",
	"territorialunitname": "运行一部",
	"territorialunitcode": "CS8082020",
	"wf_audit_state": "6",
	"status": "draft",
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"isspecialcondition": "",
	"specialenvironment": "DH0000_000002_SE01",
	"task_worktype_code": "GCN",
	"task_worktype_name": "储罐浮舱内",
	"cywlqfyxzz": "0",
	"isdzdh": "0",
	"projecttype": "rcjx",
	"isupgradedh": "0",
	"persistent_type": "newoperation",
	"issjtssxzy": "0",
	"worklevel_dh": "mcq_dh_workLevel02",
	"worklevel_sx": "",
	"worklevel_gc": "",
	"worklevel_dz": "",
	"worklevel_gx": "",
	"sourcetype": "",
	"territorialdeviceid": 2000000003454,
	"territorialdevicename": "制氢装置",
	"work_position_id": 2000000002019,
	"work_position_name": "制氢北区",
	"worksite": "作业地点123",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"workname": name,
	"workcontent": "作业内容123",
	"worktypename": "作业许可证,动火作业",
	"worktype": "xkz,dh",
	"appointstarttime": fnow1,
	"appointendtime": fnow2,
	"risksmeasures": "重点防控的风险123",
	"material_medium": "物料介质123"
}
#受限
data = {
	"tableName": "hse_work_appoint",
	"iscontractor": "0",
	"workunitname_no": "",
	"territorialunitid": 2000000003339,
	"worktaskid_no": 0,
	"isreport": "0",
	"territorialunitname": "运行一部",
	"territorialunitcode": "CS8082020",
	"wf_audit_state": "6",
	"status": "draft",
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"isspecialcondition": "",
	"specialenvironment": "ALLNOT",
	"task_worktype_code": "QT",
	"task_worktype_name": "其他",
	"cywlqfyxzz": "0",
	"isdzdh": "0",
	"projecttype": "rcjx",
	"isupgradedh": "0",
	"persistent_type": "newoperation",
	"issjtssxzy": "0",
	"worklevel_dh": "",
	"worklevel_sx": "mcq_sx_workLevel02",
	"worklevel_gc": "",
	"worklevel_dz": "",
	"worklevel_gx": "",
	"sourcetype": "",
	"worktypename": "受限空间,作业许可证",
	"worktype": "sx,xkz",
	"territorialdeviceid": 2000000003454,
	"territorialdevicename": "制氢装置",
	"work_position_id": 2000000002019,
	"work_position_name": "制氢北区",
	"worksite": "作业地点111",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"workcontent": "作业内容dddd",
	"workname": name,
	"appointstarttime": fnow1,
	"appointendtime": fnow2,
	"material_medium": "物料介质123",
	"risksmeasures": "重点防控的风险123"
}
#作业许可
data = {
	"tableName": "hse_work_appoint",
	"iscontractor": "0",
	"workunitname_no": "",
	"territorialunitid": 2000000003339,
	"worktaskid_no": 0,
	"isreport": "0",
	"territorialunitname": "运行一部",
	"territorialunitcode": "CS8082020",
	"wf_audit_state": "6",
	"status": "draft",
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"isspecialcondition": "",
	"specialenvironment": "ALLNOT",
	"task_worktype_code": "QT",
	"task_worktype_name": "其他",
	"cywlqfyxzz": "0",
	"isdzdh": "0",
	"projecttype": "rcjx",
	"isupgradedh": "0",
	"persistent_type": "newoperation",
	"issjtssxzy": "0",
	"worklevel_dh": "",
	"worklevel_sx": "",
	"worklevel_gc": "",
	"worklevel_dz": "",
	"worklevel_gx": "",
	"sourcetype": "",
	"territorialdeviceid": 2000000003454,
	"territorialdevicename": "制氢装置",
	"work_position_id": 2000000002019,
	"work_position_name": "制氢北区",
	"worksite": "作业地点123",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"workname": name,
	"workcontent": "作业内容123",
	"worktypename": "作业许可证",
	"worktype": "xkz",
	"appointstarttime": fnow1,
	"appointendtime": fnow2,
	"material_medium": "物料介质123",
	"risksmeasures": "重点防控的风险123"
}
#请求作业预约保存接口
rs=requests.post(url2, json = data, headers = headers,cookies=cookies)
'''
rs.encoding='utf-8'
rsp = str(rs.content, 'utf8')
#if rsp['status'] == 3200:
#	print("预约接口访问成功:")
print ("作业预约保存返回:",rsp)
'''
#返回值转码
data = rs.content.decode('utf-8')
#json化
data = json.loads(data)
#获取接口返回状态
sta= data['status']
if sta == 3200:
    print("作业预约成功", sta)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())

#送交用例信息

casename = '作业预约送交'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename
#送交接口地址
url3='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/wfSend?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.30092471197648707&contentType=json&ajax=true&tid=1'%(num,num)

formdata2={
	"opinion": "申请审批",
	"nodeStr": "2000000009070",
	"2000000009070": "测试用户",
	"2000000009070_id": 1000
}
#time.sleep(15)
#请求送交接口
rs=requests.post(url3, json = formdata2, headers = headers,cookies=cookies)
#rs.encoding='utf-8'
#rsp = str(rs.content, 'utf8')
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())
#作业预约审批用例信息

casename = '作业预约审批'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename
#审批接口地址
url4='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/wfFinish?parentEntityId=&parentFuncCode=&topEntityId=+&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.027850408425730055&contentType=json&ajax=true&tid=1'%(num)
#参数
formdata ={
	"opinion": "同意",
	"cC": "1000",
	"cCName": "测试用户",
	"nickName": "用户",
	"is_normal_finish": "true",
	"nodeStr": ""
}
#请求接口
rs=requests.post(url4, json = formdata, headers = headers,cookies=cookies)
#rs.encoding='utf-8'
#cc = str(rs.content, 'utf8')
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())
#print(cc)
#安全分析第一个保存用例信息
#caseid = 5
casename = '安全分析及交底保存'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename

urlfenxi ='http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_SAFETY_TASK_RISK&0.6529845051499572&contentType=json&ajax=true&tid=1'
formdatafenxi ={
	"tableName": "hse_safety_task",
	"wf_create_user": 1000,
	"iscontractor": "0",
	"analyze_type": "jsa,aqjd",
	"work_appoint_name": name,
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"workstatus": "draft",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"projecttype": "rcjx",
	"territorialdeviceid": 2000000003454,
	"territorialdevicename": "制氢装置",

	"work_appoint_id": num,
	"workcontent": "作业内容123",
	"workname": name,
	"worktickettype": "xkz,dh",
	"worktickettype_name": "作业许可证,动火作业",
	"workunitname": "长庆石化分公司",
	"workunit": 1688712,
	"planstarttime":fnow1,
	"planendtime": fnow2,
	"site": "作业地点123",
	"equipmentname": "",
	"work_position_name": "制氢北区",
	"work_position_id": 2000000002019,
	"equipmentnumber": "",
	"equipmentcode": "",
	"constructionscheme": "",
	"standardmaintenance": ""
}
#time.sleep(5)
#请求接口
rs=requests.post(urlfenxi, json = formdatafenxi, headers = headers,cookies=cookies)
rs.encoding='utf-8'
cc = str(rs.content, 'utf8')

#print("安全分析及交底保存",cc)
data = rs.content.decode('utf-8')
#json化
data = json.loads(data)

#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())
#获取worktaskid
data = data['data']['data']['worktaskid']
print("worktaskid",data)
worktaskid = data
#获取安全分析接口用例信息
#caseid = 6
casename = '获取安全分析列表'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename

#预约安全分析接口地址
url11 = 'http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/getMetaData?0.26386458099914045&contentType=json&ajax=true&tid=1'

#请求接口
rs=requests.get(url11, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json化
data = json.loads(data)

#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())
#print (sta)
a = data['data']["voset"]["voList"]
b =[]
for i in range(len(a)):

    if a[i]['worktaskid'] !="" and a[i]['worktaskid'] !="None":
        b.append(a[i]['worktaskid'])
#print (b)
num1 = worktaskid
print ("安全分析列表使用ID:",num1)

#安全分析步骤添加
#安全分析步骤添加接口用例信息
#caseid = 7
casename = '安全分析步骤添加'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename
#url ='http://192.168.6.27:6030/hse/HSE_SAFETY_ANALYSIS_STEP_RISK/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_ANALYSIS_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&0.5426692795870303&contentType=json&ajax=true&tid=1'%(num1,num1)
url ='http://192.168.6.27:6030/hse/HSE_SAFETY_ANALYSIS_STEP_RISK/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_ANALYSIS_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&0.8939960513657317&contentType=json&ajax=true&tid=1'%(num1,num1)
data = {
	"tableName": "hse_safety_analysis_step",
	"qualify_level": "no_qualify",
	"duty_name": "",
	"jsaid": num1,
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"step_type": "02",
	"evaluate_type": "",
	"risk_level": "02",
	"remain_risk_accept": "",
	"risk_value": 0,
	"risk_harm": "风险及危害123",
	"gravity": "1",
	"consequence": "后果123",
	"accident_possibility": "2",
	"step_name": "步骤活动123"
}
#请求接口
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())
#time.sleep(5)
#安全分析保存
#安全分析步保存加接口用例信息

casename = '安全分析保存'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename
#num1 = num1
print("num1:",num1)
#url='http://192.168.6.27:6030/hse/HSE_SAFETY_ANALYSIS_RISK/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_TASK_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.2955948527813328&contentType=json&ajax=true&tid=1'%(num1,num1,num1)
url='http://192.168.6.27:6030/hse/HSE_SAFETY_ANALYSIS_RISK/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_TASK_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.09494809285755568&contentType=json&ajax=true&tid=1'%(num1,num1,num1)
data = {
	"tableName": "hse_safety_analysis",

	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": "2020-06-01 13:50:32",
	"updated_by": 1000,
	"updated_dt": "2020-06-01 13:50:32",
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"jsaid": num1,
	"jsa_templete_name": "",
	"jsa_templete_id": "",
	"temp_type": "newWorkTask",
	"jsa_monitor_userid": 1000,
	"jsa_monitor_name": "测试用户",
	"jsa_menber_userids": "1000",
	"jsa_menber_username": "测试用户",
	"analyze_time": "2020-06-03 13:51:20",
	"worktickettype": "",
	"equip_stuff": "",
	"worktaskid": num1,
	"workstatus": "",
	"worktype": "jsa",
	"revampandadvide": "",
	"inspection_name": "",
	"work_position_id": 2000000002019,
	"projecttype": "",
	"workname": "",
	"workunitname": "",
	"reference": "",
	"iscontractor": "",
	"territorialunitid": "",
	"territorialunitname": "",
	"planendtime": "",
	"reviewer": "",
	"site": "",
	"worknumber": "",
	"workunit": "",
	"craftprocess": "",
	"planstarttime": "",
	"workcontent": "",
	"isnew": "",
	"wf_instance": "",
	"wf_current_user": "",
	"wf_audit_time": "",
	"wf_current_nodeid": "",
	"wf_type": "",
	"wf_create_user": "",
	"wf_audit_state": "",
	"sourcejsaid": "",
	"remainsrisk_level": "",
	"risk_level": "04"
}
#time.sleep(5)
#请求接口
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())
#安全交底
#安全交底接口用例信息

casename = '安全交底'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename
num2 = num1+17
print ("送交ID:",num2)
url='http://192.168.6.27:6030/hse/HSE_SAFETY_DISCLOSURE/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_TASK_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.7447101068947941&contentType=json&ajax=true&tid=1'%(num1,num1,num2)
data = {
	"tableName": "hse_safety_disclosure",
	"additional_content": "",
	"confirm_content": "1、已清楚作业区域及周边生产作业情况\r\n2、已清楚本次作业的安全风险（JSA）\r\n3、已清楚本次作业的具体安全要求（作业许可证中的控制措施）\r\n4、已对本次作业现场安全措施进行了检查确认\r\n5、已清楚本次作业涉及的作业许可证的有限期限 \r\n6、已掌握个人防护用具正确佩戴使用方法\r\n7、已清楚突发情况下的应急避险方法",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"safeclarid": num2,
	"projecttype": "",
	"safe_name": "长庆石化安全交底",
	"worktype": "aqjd",
	"workstatus": "draft",
	"scopeandenv": "",
	"workrisk": "",
	"preventmeasure": "",
	"emermeasure": "",
	"othermatter": "",
	"safe_content": "长庆石化安全交底",
	"safe_clar_temp_id": 2000000001040,
	"safe_clar_temp_name": "",
	"worktaskid": num1,
	"work_position_id": 2000000002019
}
data = {
	"tableName": "hse_safety_disclosure",
	"additional_content": "",
	"confirm_content": "1、已清楚作业区域及周边生产作业情况\r\n2、已清楚本次作业的安全风险（JSA）\r\n3、已清楚本次作业的具体安全要求（作业许可证中的控制措施）\r\n4、已对本次作业现场安全措施进行了检查确认\r\n5、已清楚本次作业涉及的作业许可证的有限期限 \r\n6、已掌握个人防护用具正确佩戴使用方法\r\n7、已清楚突发情况下的应急避险方法",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"safeclarid": 2000000002100,
	"projecttype": "",
	"safe_name": "自动化测试用不要删除",
	"worktype": "aqjd",
	"workstatus": "draft",
	"scopeandenv": "",
	"workrisk": "",
	"preventmeasure": "",
	"emermeasure": "",
	"othermatter": "",
	"safe_content": "",
	"safe_clar_temp_id": 2000000001050,
	"safe_clar_temp_name": "",
	"worktaskid": num1,
	"work_position_id": 2000000002019
}
#请求接口
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())

#安全送交
#安全送交接口用例信息

casename = '安全送交'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename
url = 'http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/wfSend?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.9498759321537273&contentType=json&ajax=true&tid=1'%(num1,num1)
data = {}
#请求接口
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())
#作业任务添加
#作业任务添加接口用例信息

casename = '作业任务添加'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename

url = 'http://192.168.6.27:6030/hse/HSE_WORK_TASK_MCQ/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_WORK_TASK_MCQ&0.9079012038155838&contentType=json&ajax=true&tid=1'
#双票
data  = {
	"tableName": "hse_work_task",
	"iscontractor": "0",
	"isupgrade": "0",
	"work_appoint_name": name,
	"territorialunitid": 2000000003339,
	"applyunitname": "长庆石化分公司",
	"task_pause": "0",
	"territorialunitname": "运行一部",
	"territorialunitcode": "CS8082020",
	"applyunitid": "1688712",
	"workstatus": "draft",
	"autorisklevel": 1,
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"projecttype": "rcjx",
	"isrecord": "",
	"eq_position": "",
	"territorialdeviceid": 2000000003454,
	"territorialdevicename": "制氢装置",
	"jsaid": num1,
	"work_appoint_id": num1,
	"jsa_code": "Created_by_Python_HmNEGR",
	"site": "作业地点123",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"work_position_id": 2000000002019,
	"work_position_name": "制氢北区",
	"workcontent": "作业内容123",
	"planstarttime": fnow1,
	"planendtime": fnow2,
	"standardmaintenance_name": "",
	"constructionscheme": 0,
	"worktickettype": "xkz,dh",
	"worktickettype_name": "作业许可证,动火作业",
	"standardmaintenance": "",
	"equipmentname": "",
	"equipmentnumber": "",
	"equipmentcode": "",
	"workname": name
}
#单票
data = {
	"tableName": "hse_work_task",
	"iscontractor": "0",
	"isupgrade": "0",
	"work_appoint_name": "",
	"territorialunitid": 2000000003339,
	"applyunitname": "长庆石化分公司",
	"task_pause": "0",
	"territorialunitname": "运行一部",
	"territorialunitcode": "CS8082020",
	"applyunitid": "1688712",
	"workstatus": "draft",
	"autorisklevel": 1,
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"projecttype": "",
	"isrecord": "",
	"eq_position": "",
	"territorialdeviceid": 2000000003454,
	"territorialdevicename": "制氢装置",
	"jsaid": 2000000002082,
	"work_appoint_id": "",
	"jsa_code": "任务名称",
	"site": "作业地点123",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"work_position_id": 2000000002019,
	"work_position_name": "制氢北区",
	"workcontent": "作业内容123",
	"planstarttime": fnow1,
	"planendtime": fnow2,
	"standardmaintenance_name": "",
	"constructionscheme": 0,
	"worktickettype": "xkz",
	"worktickettype_name": "作业许可证",
	"standardmaintenance": "",
	"equipmentname": "",
	"equipmentnumber": "",
	"equipmentcode": "",
	"workname": name
}
#请求接口
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())
#请求作业任务列表
#请求作业任务列表添加接口用例信息

casename = '请求作业任务列表'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TASK_MCQ/getMetaData?0.8715056152376748&contentType=json&ajax=true&tid=1'
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'csrf': '6363382b59f6435eb243fab57ea5a5e0',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Content-Type': 'text/plain',
    }

#请求接口
rs=requests.get(url, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())
#print (data['status'])
#print (data['data']["voset"]["voList"])
a = data['data']["voset"]["voList"]
b =[]
for i in range(len(a)):

    if a[i]['worktaskid'] !="" and a[i]['worktaskid'] !="None":
        b.append(a[i]['worktaskid'])
#print (b)
#print (max(b))
num2 = max(b)
print("作业任务列表ID-num2==:",num2)
#作业任务提交
#作业任务提交接口用例信息

casename = '作业任务提交'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TASK_MCQ/hse_work_task_submit?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=%d&0.7819922897402813&contentType=json&ajax=true&tid=1'%(num2,num2)
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TASK_MCQ/hse_work_task_submit?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=%d&0.412998005925274&contentType=json&ajax=true&tid=1'%(num2,num2)
#双票
data ={
	"tableName": "hse_work_task",
	"task_worktype_code": "",
	"hasrescueplan": "",
	"territorialdeviceid": 2000000003454,
	"drawshow": "",
	"cywlqfyxzz": "",
	"autorisklevel": 1,
	"worktools": "",
	"othercontent": "",
	"equipmentcode": "",
	"ishasworker": "",
	"territorialdevicename": "制氢装置",
	"hasdrawpaper": "",
	"hassafetyplan": "",
	"worker": "",
	"card_code": "",
	"reminder": "",
	"constructionscheme": 0,
	"reminderid": "",
	"worktickettype_name": "作业许可证,动火作业",
	"task_worktype_name": "",
	"standardmaintenance": "",
	"attaches": "",
	"material_medium": "",
	"risksmeasures": "",
	"isrecord": "",
	"persistent_type": "",
	"flights": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"worktaskid": num2,
	"workname": name,
	"work_position_name": "制氢北区",
	"work_appoint_name": name,
	"actualstarttime": "",
	"actualendtime": "",
	"isgas_detection": "",
	"delayreason": "",
	"cancelreason": "",
	"pause": 0,
	"isupgrade": "0",
	"sourcetaskid": "",
	"nlglnumber": "",
	"isreport": "",
	"iswfnotreport": 0,
	"gas_standard_type": "",
	"parentid": "",
	"lsydticketid": "",
	"dqyzticketid": "",
	"dqezticketid": "",
	"task_pause": "0",
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"site": "作业地点123",
	"work_property": "bespeak",
	"equipmentnumber": "",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"projecttype": "rcjx",
	"iscontractor": "0",
	"planstarttime": fnow1,
	"planendtime": fnow2,
	"worktickettype": "xkz,dh",
	"workstatus": "draft",
	"applyunitid": 1688712,
	"applyunitname": "长庆石化分公司",
	"created_by_name": "测试用户",
	"updated_by_name": "测试用户",
	"workcontent": "作业内容123",
	"woid": "",
	"wo_code": "",
	"territorialunitcode": "CS8082020",
	"equt_position": "",
	"position_name": "",
	"equipmentname": "",
	"safeclar": "",
	"safecode": "",
	"work_position_id": 2000000002019,
	"jsa_code": name,
	"jsaid": num,
	"work_appoint_id": num,
	"wf_current_nodeid": "",
	"wf_audit_time": "",
	"task_risklevel": "",
	"task_closereason": "",
	"task_closetype": "",
	"wf_current_user": "",
	"wf_audit_state": "0",
	"wf_create_user": 1000,
	"wf_instance": "",
	"wf_type": "",
	"delaynum": 0,
	"beendelaynum": 0,
	"jobstatus": "",
	"weekplanid": "",
	"plan_type": 3,
	"gasdetecttype": "",
	"close_type": "",
	"closereason": "",
	"jsa_code2": "",
	"jsaid2": "",
	"isproprietor": "",
	"planendtime_org": "",
	"specialenvironment": "",
	"gas_aging": "",
	"safetyanalysisid": "",
	"safetyanalysiscode": "",
	"isspecialcondition": "",
	"specialcondition": "",
	"task_risklevel_org": "",
	"eq_position": ""
}
data = {
	"tableName": "hse_work_task",
	"task_worktype_code": "",
	"hasrescueplan": "",
	"territorialdeviceid": 2000000003454,
	"drawshow": "",
	"cywlqfyxzz": "",
	"autorisklevel": 1,
	"worktools": "",
	"othercontent": "",
	"equipmentcode": "",
	"ishasworker": "",
	"territorialdevicename": "制氢装置",
	"hasdrawpaper": "",
	"hassafetyplan": "",
	"worker": "",
	"card_code": "",
	"reminder": "",
	"constructionscheme": 0,
	"reminderid": "",
	"worktickettype_name": "作业许可证",
	"task_worktype_name": "",
	"standardmaintenance": "",
	"attaches": "",
	"material_medium": "",
	"risksmeasures": "",
	"isrecord": "",
	"persistent_type": "",
	"flights": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"worktaskid": 2000000004392,
	"workname": name,
	"work_position_name": "制氢北区",
	"work_appoint_name": "",
	"actualstarttime": "",
	"actualendtime": "",
	"isgas_detection": "",
	"delayreason": "",
	"cancelreason": "",
	"pause": 0,
	"isupgrade": "",
	"sourcetaskid": "",
	"nlglnumber": "",
	"isreport": "",
	"iswfnotreport": 0,
	"gas_standard_type": "",
	"parentid": "",
	"lsydticketid": "",
	"dqyzticketid": "",
	"dqezticketid": "",
	"task_pause": "0",
	"device_id": "",
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"site": "作业地点123",
	"work_property": "rush_to_repair",
	"equipmentnumber": "",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"projecttype": "",
	"iscontractor": "0",
	"planstarttime": fnow1,
	"planendtime": fnow2,
	"worktickettype": "xkz",
	"workstatus": "draft",
	"applyunitid": 1688712,
	"applyunitname": "长庆石化分公司",
	"created_by_name": "测试用户",
	"updated_by_name": "测试用户",
	"workcontent": "作业内容123",
	"woid": "",
	"wo_code": "",
	"territorialunitcode": "CS8082020",
	"equt_position": "",
	"position_name": "",
	"equipmentname": "",
	"safeclar": "",
	"safecode": "",
	"work_position_id": 2000000002019,
	"jsa_code": name,
	"jsaid": num,
	"work_appoint_id": "",
	"wf_current_nodeid": "",
	"wf_audit_time": "",
	"task_risklevel": "",
	"task_closereason": "",
	"task_closetype": "",
	"wf_current_user": "",
	"wf_audit_state": "0",
	"wf_create_user": 1000,
	"wf_instance": "",
	"wf_type": "",
	"delaynum": 0,
	"beendelaynum": 0,
	"jobstatus": "",
	"weekplanid": "",
	"plan_type": 3,
	"gasdetecttype": "",
	"close_type": "",
	"closereason": "",
	"jsa_code2": "",
	"jsaid2": "",
	"isproprietor": "",
	"planendtime_org": "",
	"specialenvironment": "",
	"gas_aging": "",
	"safetyanalysisid": "",
	"safetyanalysiscode": "",
	"isspecialcondition": "",
	"specialcondition": "",
	"task_risklevel_org": "",
	"eq_position": ""
}
data = {
	"tableName": "hse_work_task",
	"task_worktype_code": "",
	"hasrescueplan": "",
	"territorialdeviceid": 2000000003454,
	"drawshow": "",
	"cywlqfyxzz": "",
	"autorisklevel": 1,
	"worktools": "",
	"othercontent": "",
	"equipmentcode": "",
	"ishasworker": "",
	"territorialdevicename": "制氢装置",
	"hasdrawpaper": "",
	"hassafetyplan": "",
	"worker": "",
	"card_code": "",
	"reminder": "",
	"constructionscheme": 0,
	"reminderid": "",
	"worktickettype_name": "作业许可证",
	"task_worktype_name": "",
	"standardmaintenance": "",
	"attaches": "",
	"material_medium": "",
	"risksmeasures": "",
	"isrecord": "",
	"persistent_type": "",
	"flights": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"worktaskid": num2,
	"workname": name,
	"work_position_name": "制氢北区",
	"work_appoint_name": "",
	"actualstarttime": "",
	"actualendtime": "",
	"isgas_detection": "",
	"delayreason": "",
	"cancelreason": "",
	"pause": 0,
	"isupgrade": "0",
	"sourcetaskid": "",
	"nlglnumber": "",
	"isreport": "",
	"iswfnotreport": 0,
	"gas_standard_type": "",
	"parentid": "",
	"lsydticketid": "",
	"dqyzticketid": "",
	"dqezticketid": "",
	"task_pause": "0",
	"device_id": "",
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"site": "作业地点123",
	"work_property": "rush_to_repair",
	"equipmentnumber": "",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"projecttype": "",
	"iscontractor": "0",
	"planstarttime": fnow1,
	"planendtime": fnow2,
	"worktickettype": "xkz",
	"workstatus": "draft",
	"applyunitid": 1688712,
	"applyunitname": "长庆石化分公司",
	"created_by_name": "测试用户",
	"updated_by_name": "测试用户",
	"workcontent": "作业内容123",
	"woid": "",
	"wo_code": "",
	"territorialunitcode": "CS8082020",
	"equt_position": "",
	"position_name": "",
	"equipmentname": "",
	"safeclar": "",
	"safecode": "",
	"work_position_id": 2000000002019,
	"jsa_code": name,
	"jsaid": num,
	"work_appoint_id": "",
	"wf_current_nodeid": "",
	"wf_audit_time": "",
	"task_risklevel": "",
	"task_closereason": "",
	"task_closetype": "",
	"wf_current_user": "",
	"wf_audit_state": "0",
	"wf_create_user": 1000,
	"wf_instance": "",
	"wf_type": "",
	"delaynum": 0,
	"beendelaynum": 0,
	"jobstatus": "",
	"weekplanid": "",
	"plan_type": 3,
	"gasdetecttype": "",
	"close_type": "",
	"closereason": "",
	"jsa_code2": "",
	"jsaid2": "",
	"isproprietor": "",
	"planendtime_org": "",
	"specialenvironment": "",
	"gas_aging": "",
	"safetyanalysisid": "",
	"safetyanalysiscode": "",
	"isspecialcondition": "",
	"specialcondition": "",
	"task_risklevel_org": "",
	"eq_position": ""
}
#time.sleep(3)
#请求接口
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
    print(data)
#收集用例执行信息
testsuit.append(caseinfo.copy())

#作业许可证保存
#作业票ID
num3 = workticketid+1
ts = tsi+1
print(num3)
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TICKET_XKZ/cardSave?parentEntityId=%d&parentFuncCode=HSE_WORK_TASK_MCQ&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=%d&ts=1590652813735&0.27372678355625824&contentType=json&ajax=true&tid=1'%(num2,num2,num3)
#url = 'http://192.168.6.27:6030/hse/HSE_WORK_TICKET_XKZ/cardSave?parentEntityId=%d&parentFuncCode=HSE_WORK_TASK_MCQ&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=2000000005573&ts=1590656443277&0.7178753893110355&contentType=json&ajax=true&tid=1'%(num2,num2)
#print(url)
#双票
data = {
	"tableName": "hse_work_ticket",
	"clause": "",
	"tasktype": "",
	"radiosourcenum": "",
	"relevantdoc": "",
	"safedistance": "",
	"issjtssxzy": "",
	"isupgradedh": "",
	"isdzdh": "",
	"isrecord": "",
	"excavation_eqp": "",
	"territorialunitcode": "CS8082020",
	"worker": "9002",
	"pipeline_level": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": 1590656443277,
	"istaskpause": 0,
	"classgroup": "",
	"isend": "",
	"end_reason": "",
	"end_dt": "",
	"groundwire_num": "",
	"groupknife_num": "",
	"groundwire_code": "",
	"othercontent": "",
	"sent_overdueclose_message": 0,
	"isupgrade": "0",
	"isfireday": "0",
	"isdue": "0",
	"operator": "",
	"worktimeconsum": "",
	"task_pause": "0",
	"projecttype": "",
	"is_pause": 0,
	"workticketid": num3,
	"worktaskid": num2,
	"equipmentnumber": "",
	"worktype": "xkz",
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"applyunitid": 1688712,
	"applyunitname": "长庆石化分公司",
	"worknumber": "",
	"worklevel": "",
	"site": "作业地点123",
	"workway": "",
	"planstarttime": fnow1,
	"planendtime": fnow2,
	"actualstarttime": "",
	"actualendtime": "",
	"otherwork": "",
	"workname": name,
	"workcontent": "作业内容123",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"workstatus": "draft",
	"equipmentpipename": "",
	"medium": "",
	"temperature": "",
	"pressure": "",
	"blindplate_material": "",
	"blindplate_spec": "",
	"blindplate_code": "",
	"blindplate_mapandcode": "",
	"workhighly": "",
	"objectmass": "",
	"poweraccesspoint": "",
	"workvoltage": "",
	"equipmentandpower": "",
	"otherunit": "",
	"workreason": "",
	"isharmconfirm": "",
	"ismeasureconfirm": "",
	"isgascomplate": "",
	"issigncomplate": "",
	"created_by_name": "测试用户",
	"updated_by_name": "测试用户",
	"closereason": "",
	"gastestaging": "",
	"blindplate_worktype": "",
	"gasket_material": "",
	"gasket_spec": "",
	"close_type": "",
	"delaynum": 0,
	"beendelaynum": 0,
	"isppeconfirm": "",
	"invalidreason": "",
	"hassafetyplan": "0",
	"hashseplan": "",
	"hasemergencyplan": "",
	"hasdrawpaper": "0",
	"haschecklist": "",
	"hasrescueplan": "",
	"loadradius": "",
	"loaddegree": "",
	"loadrate": "",
	"objectnorm": "",
	"loadmass": "",
	"haslineopensitemap": "",
	"radiosourcetype": "",
	"sourcecode": "",
	"sourcestrength": "",
	"suprange": "",
	"controlrange": "",
	"drawshow": "",
	"hashookcheck": "",
	"hasfacadecheck": "",
	"hasdrivermedical": "",
	"objectname": "",
	"cancelreason": "",
	"hidesituation": "",
	"work_position_id": 2000000002019,
	"isgas_detection": "1",
	"gas_aging": "1",
	"isqualgasdetection": "",
	"dig_size_l": "",
	"dig_size_w": "",
	"dig_size_h": "",
	"attaches": "",
	"lock_status": 0,
	"lock_equipment_id": "",
	"dl_uuid": "",
	"dl_time": "",
	"level_upgrade": 0,
	"loadgoodsname": "",
	"loadhigh": "",
	"worktask_name": name,
	"worktype_name": "作业许可证",
	"dz_craneno": "",
	"gas_standard_type": "",
	"isproprietor": "",
	"worksite": "",
	"workticketmbcdid": "",
	"isstoppower": "",
	"work_position_name": "制氢北区",
	"gas_detector_no": "",
	"additional_requirements": "",
	"worklevel_org": ""
}

data = {
	"tableName": "hse_work_ticket",
	"clause": "",
	"tasktype": "",
	"radiosourcenum": "",
	"relevantdoc": "",
	"safedistance": "",
	"issjtssxzy": "",
	"isupgradedh": "",
	"isdzdh": "",
	"isrecord": "",
	"excavation_eqp": "",
	"territorialunitcode": "CS8082020",
	"worker": "3123213",
	"pipeline_level": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": 1591170000174,
	"istaskpause": 0,
	"classgroup": "",
	"isend": "",
	"end_reason": "",
	"end_dt": "",
	"groundwire_num": "",
	"groupknife_num": "",
	"groundwire_code": "",
	"othercontent": "",
	"sent_overdueclose_message": 0,
	"isupgrade": "0",
	"isfireday": "0",
	"isdue": "0",
	"operator": "",
	"worktimeconsum": "",
	"device_id": "",
	"task_pause": "0",
	"projecttype": "",
	"is_pause": 0,
	"workticketid": num3,
	"worktaskid": num2,
	"equipmentnumber": "",
	"worktype": "xkz",
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"applyunitid": 1688712,
	"applyunitname": "长庆石化分公司",
	"worknumber": "",
	"worklevel": "",
	"site": "作业地点123",
	"workway": "",
	"planstarttime": fnow1,
	"planendtime": fnow2,
	"actualstarttime": "",
	"actualendtime": "",
	"otherwork": "",
	"workname": name,
	"workcontent": "作业内容123",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"workstatus": "draft",
	"equipmentpipename": "",
	"medium": "",
	"temperature": "",
	"pressure": "",
	"blindplate_material": "",
	"blindplate_spec": "",
	"blindplate_code": "",
	"blindplate_mapandcode": "",
	"workhighly": "",
	"objectmass": "",
	"poweraccesspoint": "",
	"workvoltage": "",
	"equipmentandpower": "",
	"otherunit": "",
	"workreason": "",
	"isharmconfirm": "",
	"ismeasureconfirm": "",
	"isgascomplate": "",
	"issigncomplate": "",
	"created_by_name": "测试用户",
	"updated_by_name": "测试用户",
	"closereason": "",
	"gastestaging": "",
	"blindplate_worktype": "",
	"gasket_material": "",
	"gasket_spec": "",
	"close_type": "",
	"delaynum": 0,
	"beendelaynum": 0,
	"isppeconfirm": "",
	"invalidreason": "",
	"hassafetyplan": "0",
	"hashseplan": "",
	"hasemergencyplan": "",
	"hasdrawpaper": "0",
	"haschecklist": "",
	"hasrescueplan": "",
	"loadradius": "",
	"loaddegree": "",
	"loadrate": "",
	"objectnorm": "",
	"loadmass": "",
	"haslineopensitemap": "",
	"radiosourcetype": "",
	"sourcecode": "",
	"sourcestrength": "",
	"suprange": "",
	"controlrange": "",
	"drawshow": "",
	"hashookcheck": "",
	"hasfacadecheck": "",
	"hasdrivermedical": "",
	"objectname": "",
	"cancelreason": "",
	"hidesituation": "",
	"work_position_id": 2000000002019,
	"isgas_detection": "0",
	"gas_aging": "",
	"isqualgasdetection": "",
	"dig_size_l": "",
	"dig_size_w": "",
	"dig_size_h": "",
	"attaches": "",
	"lock_status": 0,
	"lock_equipment_id": "",
	"dl_uuid": "",
	"dl_time": "",
	"level_upgrade": 0,
	"loadgoodsname": "",
	"loadhigh": "",
	"worktask_name": name,
	"worktype_name": "作业许可证",
	"dz_craneno": "",
	"gas_standard_type": "",
	"isproprietor": "",
	"worksite": "",
	"workticketmbcdid": "",
	"isstoppower": "",
	"work_position_name": "制氢北区",
	"gas_detector_no": "",
	"additional_requirements": "",
	"worklevel_org": ""
}
#请求接口
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
rs.encoding='utf-8'
cc = str(rs.content, 'utf8')
#print ("作业许可证保存",cc)

#作业许可证提交
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TICKET_XKZ/hse_work_ticket_submit?parentEntityId=%d&parentFuncCode=HSE_WORK_TASK_MCQ&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=%d&ts=1591086843103&0.5776995917838637&contentType=json&ajax=true&tid=1'%(num2,num2,num3)
#print(url)
data ={
	"tableName": "hse_work_ticket",
	"clause": "",
	"tasktype": "",
	"radiosourcenum": "",
	"relevantdoc": "",
	"safedistance": "",
	"issjtssxzy": "",
	"isupgradedh": "",
	"isdzdh": "",
	"isrecord": "",
	"excavation_eqp": "",
	"territorialunitcode": "CS8082020",
	"worker": "无",
	"pipeline_level": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": ts,
	"istaskpause": 0,
	"classgroup": "",
	"isend": "",
	"end_reason": "",
	"end_dt": "",
	"groundwire_num": "",
	"groupknife_num": "",
	"groundwire_code": "",
	"othercontent": "",
	"sent_overdueclose_message": 0,
	"isupgrade": "0",
	"isfireday": "0",
	"isdue": "0",
	"operator": "",
	"worktimeconsum": "",
	"task_pause": "0",
	"projecttype": "",
	"is_pause": 0,
	"workticketid": num3,
	"worktaskid": num2,
	"equipmentnumber": "",
	"worktype": "xkz",
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"applyunitid": 1688712,
	"applyunitname": "长庆石化分公司",
	"worknumber": "",
	"worklevel": "",
	"site": "作业地点123",
	"workway": "",
	"planstarttime": fnow1,
	"planendtime": fnow2,
	"actualstarttime": "",
	"actualendtime": "",
	"otherwork": "",
	"workname": name,
	"workcontent": "作业内容123",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"workstatus": "draft",
	"equipmentpipename": "",
	"medium": "",
	"temperature": "",
	"pressure": "",
	"blindplate_material": "",
	"blindplate_spec": "",
	"blindplate_code": "",
	"blindplate_mapandcode": "",
	"workhighly": "",
	"objectmass": "",
	"poweraccesspoint": "",
	"workvoltage": "",
	"equipmentandpower": "",
	"otherunit": "",
	"workreason": "",
	"isharmconfirm": "",
	"ismeasureconfirm": "",
	"isgascomplate": "",
	"issigncomplate": "",
	"created_by_name": "测试用户",
	"updated_by_name": "测试用户",
	"closereason": "",
	"gastestaging": "",
	"blindplate_worktype": "",
	"gasket_material": "",
	"gasket_spec": "",
	"close_type": "",
	"delaynum": 0,
	"beendelaynum": 0,
	"isppeconfirm": "",
	"invalidreason": "",
	"hassafetyplan": "0",
	"hashseplan": "",
	"hasemergencyplan": "",
	"hasdrawpaper": "0",
	"haschecklist": "",
	"hasrescueplan": "",
	"loadradius": "",
	"loaddegree": "",
	"loadrate": "",
	"objectnorm": "",
	"loadmass": "",
	"haslineopensitemap": "",
	"radiosourcetype": "",
	"sourcecode": "",
	"sourcestrength": "",
	"suprange": "",
	"controlrange": "",
	"drawshow": "",
	"hashookcheck": "",
	"hasfacadecheck": "",
	"hasdrivermedical": "",
	"objectname": "",
	"cancelreason": "",
	"hidesituation": "",
	"work_position_id": 2000000002019,
	"isgas_detection": "0",
	"gas_aging": "",
	"isqualgasdetection": "",
	"dig_size_l": "",
	"dig_size_w": "",
	"dig_size_h": "",
	"attaches": "",
	"lock_status": 0,
	"lock_equipment_id": "",
	"dl_uuid": "",
	"dl_time": "",
	"level_upgrade": 0,
	"loadgoodsname": "",
	"loadhigh": "",
	"worktask_name": name,
	"worktype_name": "作业许可证",
	"dz_craneno": "",
	"gas_standard_type": "",
	"isproprietor": "",
	"worksite": "",
	"workticketmbcdid": "",
	"isstoppower": "",
	"work_position_name": "制氢北区",
	"gas_detector_no": "",
	"additional_requirements": "",
	"worklevel_org": ""
}
#print("last::", data)
#请求接口
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
rs.encoding='utf-8'
cc = str(rs.content, 'utf8')
#print (cc)
#driver.close()
#driver.quit()
#动火作业保存
num3 = workticketid +1
ts = tsi+1
#动火
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TICKET_DH_MCQ/cardSave?parentEntityId=%d&parentFuncCode=HSE_WORK_TASK_MCQ&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=%d&ts=%d&0.9284553583877271&contentType=json&ajax=true&tid=1'%(num2,num2,num3,ts)
data = {
	"tableName": "hse_work_ticket",
	"clause": "",
	"tasktype": "dh01",
	"radiosourcenum": "",
	"relevantdoc": "rd01",
	"safedistance": "",
	"issjtssxzy": "",
	"aecolcode": "",
	"isupgradedh": "",
	"isdzdh": "",
	"isrecord": "",
	"excavation_eqp": "",
	"territorialunitcode": "CS8082020",
	"worker": "",
	"pipeline_level": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": 1591092134666,
	"istaskpause": 0,
	"classgroup": "",
	"isend": "",
	"end_reason": "",
	"end_dt": "",
	"groundwire_num": "",
	"groupknife_num": "",
	"groundwire_code": "",
	"othercontent": "",
	"sent_overdueclose_message": 0,
	"isupgrade": "0",
	"isfireday": "0",
	"isdue": "0",
	"operator": "",
	"worktimeconsum": "",
	"device_id": "",
	"task_pause": "0",
	"projecttype": "",
	"is_pause": 0,
	"workticketid": num3,
	"worktaskid": num2,
	"equipmentnumber": "",
	"worktype": "dh",
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"applyunitid": 1688712,
	"applyunitname": "长庆石化分公司",
	"worknumber": "",
	"worklevel": "mcq_dh_workLevel02",
	"site": "作业地点123",
	"workway": "mcq_dhfs01",
	"planstarttime": fnow1,
	"planendtime": fnow2,
	"actualstarttime": "",
	"actualendtime": "",
	"otherwork": "",
	"workname": name,
	"workcontent": "作业内容123",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"workstatus": "draft",
	"equipmentpipename": "",
	"medium": "介质123",
	"temperature": "",
	"pressure": "",
	"blindplate_material": "",
	"blindplate_spec": "",
	"blindplate_code": "",
	"blindplate_mapandcode": "",
	"workhighly": "",
	"objectmass": "",
	"poweraccesspoint": "",
	"workvoltage": "",
	"equipmentandpower": "",
	"otherunit": "",
	"workreason": "",
	"isharmconfirm": "",
	"ismeasureconfirm": "",
	"isgascomplate": "",
	"issigncomplate": "",
	"created_by_name": "测试用户",
	"updated_by_name": "测试用户",
	"closereason": "",
	"gastestaging": "",
	"blindplate_worktype": "",
	"gasket_material": "",
	"gasket_spec": "",
	"close_type": "",
	"delaynum": 0,
	"beendelaynum": 0,
	"isppeconfirm": "",
	"invalidreason": "",
	"hassafetyplan": "",
	"hashseplan": "",
	"hasemergencyplan": "",
	"hasdrawpaper": "",
	"haschecklist": "",
	"hasrescueplan": "",
	"loadradius": "",
	"loaddegree": "",
	"loadrate": "",
	"objectnorm": "",
	"loadmass": "",
	"haslineopensitemap": "",
	"radiosourcetype": "",
	"sourcecode": "",
	"sourcestrength": "",
	"suprange": "",
	"controlrange": "",
	"drawshow": "",
	"hashookcheck": "",
	"hasfacadecheck": "",
	"hasdrivermedical": "",
	"objectname": "",
	"cancelreason": "",
	"hidesituation": "",
	"work_position_id": 2000000002019,
	"isgas_detection": "1",
	"gas_aging": 1,
	"isqualgasdetection": "",
	"dig_size_l": "",
	"dig_size_w": "",
	"dig_size_h": "",
	"attaches": "",
	"lock_status": 0,
	"lock_equipment_id": "",
	"dl_uuid": "",
	"dl_time": "",
	"level_upgrade": 0,
	"loadgoodsname": "",
	"loadhigh": "",
	"worktask_name": name,
	"worktype_name": "动火作业",
	"dz_craneno": "",
	"gas_standard_type": "",
	"isproprietor": "",
	"worksite": "",
	"workticketmbcdid": "",
	"isstoppower": "",
	"work_position_name": "制氢北区",
	"gas_detector_no": "",
	"additional_requirements": "",
	"worklevel_org": ""
}
#请求接口
#rs=requests.post(url, json = data, headers = headers,cookies=cookies)
rs.encoding='utf-8'
cc = str(rs.content, 'utf8')
#print(cc)
#动火票提交
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TICKET_DH_MCQ/hse_work_ticket_submit?parentEntityId=%d&parentFuncCode=HSE_WORK_TASK_MCQ&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=%d&ts=%d&0.6197776458397488&contentType=json&ajax=true&tid=1'%(num2,num2,num3,ts)
data ={
	"tableName": "hse_work_ticket",
	"clause": "",
	"tasktype": "dh01",
	"radiosourcenum": "",
	"relevantdoc": "rd01",
	"safedistance": "",
	"issjtssxzy": "",
	"aecolcode": "",
	"isupgradedh": "",
	"isdzdh": "",
	"isrecord": "",
	"excavation_eqp": "",
	"territorialunitcode": "CS8082020",
	"worker": "",
	"pipeline_level": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": ts,
	"istaskpause": 0,
	"classgroup": "",
	"isend": "",
	"end_reason": "",
	"end_dt": "",
	"groundwire_num": "",
	"groupknife_num": "",
	"groundwire_code": "",
	"othercontent": "",
	"sent_overdueclose_message": 0,
	"isupgrade": "0",
	"isfireday": "0",
	"isdue": "0",
	"operator": "",
	"worktimeconsum": "",
	"device_id": "",
	"task_pause": "0",
	"projecttype": "",
	"is_pause": 0,
	"workticketid": num3,
	"worktaskid": num2,
	"equipmentnumber": "",
	"worktype": "dh",
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"applyunitid": 1688712,
	"applyunitname": "长庆石化分公司",
	"worknumber": "",
	"worklevel": "mcq_dh_workLevel02",
	"site": "作业地点123",
	"workway": "mcq_dhfs01",
	"planstarttime": fnow1,
	"planendtime": fnow2,
	"actualstarttime": "",
	"actualendtime": "",
	"otherwork": "",
	"workname": name,
	"workcontent": "作业内容123",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"workstatus": "draft",
	"equipmentpipename": "",
	"medium": "介质123",
	"temperature": "",
	"pressure": "",
	"blindplate_material": "",
	"blindplate_spec": "",
	"blindplate_code": "",
	"blindplate_mapandcode": "",
	"workhighly": "",
	"objectmass": "",
	"poweraccesspoint": "",
	"workvoltage": "",
	"equipmentandpower": "",
	"otherunit": "",
	"workreason": "",
	"isharmconfirm": "",
	"ismeasureconfirm": "",
	"isgascomplate": "",
	"issigncomplate": "",
	"created_by_name": "测试用户",
	"updated_by_name": "测试用户",
	"closereason": "",
	"gastestaging": "",
	"blindplate_worktype": "",
	"gasket_material": "",
	"gasket_spec": "",
	"close_type": "",
	"delaynum": 0,
	"beendelaynum": 0,
	"isppeconfirm": "",
	"invalidreason": "",
	"hassafetyplan": "",
	"hashseplan": "",
	"hasemergencyplan": "",
	"hasdrawpaper": "",
	"haschecklist": "",
	"hasrescueplan": "",
	"loadradius": "",
	"loaddegree": "",
	"loadrate": "",
	"objectnorm": "",
	"loadmass": "",
	"haslineopensitemap": "",
	"radiosourcetype": "",
	"sourcecode": "",
	"sourcestrength": "",
	"suprange": "",
	"controlrange": "",
	"drawshow": "",
	"hashookcheck": "",
	"hasfacadecheck": "",
	"hasdrivermedical": "",
	"objectname": "",
	"cancelreason": "",
	"hidesituation": "",
	"work_position_id": 2000000002019,
	"isgas_detection": "1",
	"gas_aging": 1,
	"isqualgasdetection": "",
	"dig_size_l": "",
	"dig_size_w": "",
	"dig_size_h": "",
	"attaches": "",
	"lock_status": 0,
	"lock_equipment_id": "",
	"dl_uuid": "",
	"dl_time": "",
	"level_upgrade": 0,
	"loadgoodsname": "",
	"loadhigh": "",
	"worktask_name": name,
	"worktype_name": "动火作业",
	"dz_craneno": "",
	"gas_standard_type": "",
	"isproprietor": "",
	"worksite": "",
	"workticketmbcdid": "",
	"isstoppower": "",
	"work_position_name": "制氢北区",
	"gas_detector_no": "",
	"additional_requirements": "",
	"worklevel_org": ""
}
#请求接口
#rs=requests.post(url, json = data, headers = headers,cookies=cookies)
rs.encoding='utf-8'
cc = str(rs.content, 'utf8')
#print(cc)
for i in range(len(testsuit)):
    print(testsuit[i])


import requests
import execjs
import os
import json

def getEntryPwd(encryptType,pwd,modulus,publicExponent):
    # 返回加密后的密码
    path=os.path.abspath(os.path.dirname(__file__))
    file=os.path.join(path,'./hdEncrypt_merge.js')
    #logging.debug("path:%s"%path)
    data=open(file,'r',encoding= 'utf8').read()
    jss=execjs.compile(data)
    #logging.debug(jss)
    return  jss.call("login",encryptType,pwd,modulus,publicExponent)
#移动端登录
url = "http://192.168.6.27:6030/m/passport/login/getEncryptType.json"
url1 ="http://192.168.6.27:6030/m/passport/login/login.json"

headers ={
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.12.0',
    'Connnection':'Keep-Alive'
    }
sr = requests.get(url,headers=headers)

eq = sr.json()

USER_NAME = "test"
password ="1"
loginStoken=eq['data']['loginStoken']
encryptType=eq['data']['encryptType']
modulus = eq['data']['pubKeyVO']['modulus']
publicExponent = eq['data']['pubKeyVO']['publicExponent']
pwd = getEntryPwd(encryptType,password,modulus,publicExponent)
#print (eq)
#print (eq['status'])
#print(loginStoken)
#print(encryptType)
#print( pwd)
#print(eq['data']['pubKeyVO'])
headers={
    'Accept': 'application/json',
     'Content-Type': 'application/json',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.12.0',
    'Connnection': 'Keep-Alive'
    }

data={"appVersion":"01.20.0530","loginStoken":loginStoken,"password":pwd,"username":"test",'tenantid':0}
#data = base64.b64encode(json.dumps(data))
rs= requests.post(url=url1,json =data,headers = headers)

cookies = requests.utils.dict_from_cookiejar(rs.cookies)

#返回值转码
data = rs.content.decode('utf-8')
#json化
data = json.loads(data)
loginStoken = data['data']['st']
#print(data)
print(loginStoken)
#encryptType = eq['data']['encryptType']
#print (encryptType)

#cookies={'JSESSIONID': '0F5ED4C32181CF4F223E2984DFCE086A0afqB2'}
#保存作业许可票
num3 = workticketid+2
ts = tsi+2
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_XKZ_MCQ_M/cardSave.json?level=1"
headers = {
            "Accept":"application/json",
"Accept-Encoding": "gzip",
"user-agent":"ONEPLUS A6010(Android/10) (com.hayden.hap.fv/1.0.2) Weex/0.16.0 1080x2134",
"Content-Type": "application/json;charset=UTF-8",
    "st":loginStoken,
    "tid":"1"

}
data = {
	"children": {
		"HSE_WORK_TASK_HARM_MCQ_M": [{
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008710,
				"harmcode": "gzxy001",
				"harmname": "爆炸性气体",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019723,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008711,
				"harmcode": "gzxy002",
				"harmname": "易燃性物质",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019724,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008712,
				"harmcode": "gzxy003",
				"harmname": "腐蚀性液体",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019725,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008713,
				"harmcode": "gzxy004",
				"harmname": "有毒有害化学品",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019726,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008714,
				"harmcode": "gzxy005",
				"harmname": "高压气体/液体",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019727,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008715,
				"harmcode": "gzxy006",
				"harmname": "蒸汽",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019728,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008716,
				"harmcode": "gzxy007",
				"harmname": "爆炸性粉尘",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019729,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008717,
				"harmcode": "gzxy008",
				"harmname": "惰性气体",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019730,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008718,
				"harmcode": "gzxy009",
				"harmname": "危险物料混窜",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019731,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008719,
				"harmcode": "gzxy010",
				"harmname": "转动设备",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019732,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008720,
				"harmcode": "gzxy011",
				"harmname": "物料自然",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019733,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008721,
				"harmcode": "gzxy012",
				"harmname": "中毒窒息",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019734,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008722,
				"harmcode": "gzxy013",
				"harmname": "辐射",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019735,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008723,
				"harmcode": "gzxy014",
				"harmname": "化学反应",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019736,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008724,
				"harmcode": "gzxy015",
				"harmname": "隐蔽工程泄漏",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019737,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008725,
				"harmcode": "gzxy016",
				"harmname": "不利天气",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019738,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008726,
				"harmcode": "gzxy017",
				"harmname": "坠落",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019739,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008727,
				"harmcode": "gzxy018",
				"harmname": "产生火花",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019740,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008728,
				"harmcode": "gzxy019",
				"harmname": "噪音",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019741,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008729,
				"harmcode": "gzxy020",
				"harmname": "灼伤/烫伤",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019742,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008730,
				"harmcode": "gzxy021",
				"harmname": "物体打击",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019743,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008731,
				"harmcode": "gzxy022",
				"harmname": "触电/静电",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019744,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008732,
				"harmcode": "gzxy023",
				"harmname": "湿滑跌倒",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019745,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008733,
				"harmcode": "gzxy024",
				"harmname": "淹溺/坍塌",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019746,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008734,
				"harmcode": "gzxy025",
				"harmname": "其他请注明：（）",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019747,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmname": "风险及危害123",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019748,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}],
		"HSE_WORK_TASK_EQUIPMENT_M": [{
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "安全眼镜",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000100,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010018,
				"equipmentcode": "aqyj",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "全封闭眼罩",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000101,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010019,
				"equipmentcode": "qfbyz",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "焊接护目镜",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000102,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010020,
				"equipmentcode": "hjhmj",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "安全帽",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000103,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010021,
				"equipmentcode": "aqm",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "防静电服装",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000104,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010022,
				"equipmentcode": "fjdfz",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "护耳",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000105,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010023,
				"equipmentcode": "he",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "安全鞋",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000106,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010024,
				"equipmentcode": "aqx",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "防毒面罩",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000107,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010025,
				"equipmentcode": "fdmz",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "正压式呼吸器",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000108,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010026,
				"equipmentcode": "zyshxq",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "防化服",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000109,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010027,
				"equipmentcode": "fhf",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "手套",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000110,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010028,
				"equipmentcode": "st",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "绝缘服",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000111,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010029,
				"equipmentcode": "jyfz",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "防弧面具",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000112,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010030,
				"equipmentcode": "fhmj",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "安全带",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000113,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010031,
				"equipmentcode": "aqd",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "安全绳",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000114,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010032,
				"equipmentcode": "aqs",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "逃生设施",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000115,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010033,
				"equipmentcode": "tsss",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "人员培训已完成",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000116,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010034,
				"equipmentcode": "rypx",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "其他（）",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000117,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010035,
				"equipmentcode": "qtfh",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}],
		"HSE_WORK_TASK_MEASURE_MCQ_M": [{
			"vo": {
				"measuredesc": "切断工艺流程",
				"riskrepositoryid": 2000000004946,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk01",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042204,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "设路障",
				"riskrepositoryid": 2000000004947,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk02",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042205,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "设备隔离、吹扫、置换",
				"riskrepositoryid": 2000000004948,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk03",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042206,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "工作警示牌",
				"riskrepositoryid": 2000000004949,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk04",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042207,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "电源切断",
				"riskrepositoryid": 2000000004950,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk05",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042208,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "通讯工具",
				"riskrepositoryid": 2000000004951,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk06",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042209,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "完成上锁挂牌",
				"riskrepositoryid": 2000000004952,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk07",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042210,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "火花防护罩",
				"riskrepositoryid": 2000000004953,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk08",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042211,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "通风",
				"riskrepositoryid": 2000000004954,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk09",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042212,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "气体检测仪",
				"riskrepositoryid": 2000000004955,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk10",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042213,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "气体检测",
				"riskrepositoryid": 2000000004956,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk11",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042214,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "防爆机具",
				"riskrepositoryid": 2000000004957,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk12",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042215,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "工作区域围栏、警戒线",
				"riskrepositoryid": 2000000004958,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk13",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042216,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "急救设施",
				"riskrepositoryid": 2000000004959,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk14",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042217,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "紧急疏散指示",
				"riskrepositoryid": 2000000004960,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk15",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042218,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "消防设施",
				"riskrepositoryid": 2000000004961,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk16",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042219,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "需要夜间照明和警示灯具",
				"riskrepositoryid": 2000000004962,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk17",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042220,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "安全冲淋设施",
				"riskrepositoryid": 2000000004963,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk18",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042221,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "设备安全检查合格并已贴标签",
				"riskrepositoryid": 2000000004964,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk19",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042222,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "安全工作方案审核通过",
				"riskrepositoryid": 2000000004965,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk20",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042223,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "特种作业人员均持有效资质",
				"riskrepositoryid": 2000000004966,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk21",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042224,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "其他措施：（）",
				"riskrepositoryid": 2000000004967,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk22",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042225,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}]
	},
	"vo": {
		"hse_work_task_harm_mcq_m": 26,
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"drawshow": "",
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"otherunit": "",
		"level_upgrade": 0,
		"beendelaynum": 0,
		"created_by_name": "测试用户",
		"tableName": "hse_work_ticket",
		"aecolcode": 0,
		"othercontent": "",
		"hse_work_task_equipment_m": 18,
		"worktype_name": "作业许可证",
		"territorialunitid": 2000000003339,
		"hasdrawpaper": "0",
		"hassafetyplan": "0",
		"aecolcode_attachshowlist": [],
		"territorialunitname": "运行一部",
		"worker": "长庆石化分公司",
		"is_pause": 0,
		"ver": 1,
		"lock_status": 0,
		"planendtime": fnow2,
		"applyunitname": "长庆石化分公司",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"created_by": 1000,
		"worknumber": "",
		"workunit": 1688712,
		"task_pause": 0,
		"updated_by": 1000,
		"planstarttime": fnow1,
		"isgas_detection": 1,
		"hse_work_task_measure_mcq_m": 22,
		"workcontent": "作业内容123",
		"workticketid": num3,
		"close_type": "",
		"isupgrade": 0,
		"invalidreason": "",
		"ticketdealphoto_attachshowlist": [],
		"work_position_name": "制氢北区",
		"updated_by_name": "测试用户",
		"tenantid": 1,
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"actualendtime": "",
		"created_dt": now,
		"closereason": "",
		"worktype": "xkz",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isdue": 0,
		"updated_dt": now,
		"gas_detector_no": "",
		"applyunitid": 1688712,
		"ticketdealphoto": 0,
		"gas_aging": "1",
		"territorialunitcode": "CS8082020",
		"hashseplan": "",
		"worktaskid": num2,
		"ts": ts
	}
}

#rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#手机提交作业许可票
num3 = workticketid+2
ts = tsi+2
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_XKZ_MCQ_M/submit.json?dataId=%d&ts=%d"%(num3,ts)
data = {
	"vo": {
		"hse_work_task_harm_mcq_m": 52,
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"drawshow": "",
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"otherunit": "",
		"level_upgrade": 0,
		"beendelaynum": 0,
		"created_by_name": "测试用户",
		"tableName": "hse_work_ticket",
		"aecolcode": 0,
		"othercontent": "",
		"hse_work_task_equipment_m": 36,
		"worktype_name": "作业许可证",
		"territorialunitid": 2000000003339,
		"hasdrawpaper": 0,
		"hassafetyplan": 0,
		"aecolcode_attachshowlist": [],
		"territorialunitname": "运行一部",
		"worker": "长庆石化分公司",
		"is_pause": 0,
		"ver": 1,
		"lock_status": 0,
		"planendtime": fnow2,
		"applyunitname": "长庆石化分公司",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"created_by": 1000,
		"worknumber": "",
		"workunit": 1688712,
		"task_pause": 0,
		"updated_by": 1000,
		"planstarttime": fnow1,
		"isgas_detection": 1,
		"hse_work_task_measure_mcq_m": 44,
		"workcontent": "作业内容123",
		"workticketid": num3,
		"close_type": "",
		"isupgrade": 0,
		"invalidreason": "",
		"ticketdealphoto_attachshowlist": [],
		"work_position_name": "制氢北区",
		"updated_by_name": "测试用户",
		"tenantid": 1,
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"actualendtime": "",
		"created_dt": now,
		"closereason": "",
		"worktype": "xkz",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isdue": 0,
		"updated_dt": now,
		"gas_detector_no": "",
		"applyunitid": 1688712,
		"ticketdealphoto": 0,
		"gas_aging": 1,
		"territorialunitcode": "CS8082020",
		"hashseplan": "",
		"worktaskid": num2,
		"ts": ts
	}
}
#rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#手机保存和提交动火作业许可票
num3 = workticketid+1
ts = tsi+1
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_DH_MCQ_M/submit.json?dataId=%d&ts=%d"%(num3,ts)
data = {
	"vo": {
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"drawshow": "",
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"level_upgrade": 0,
		"relevantdoc": "rd01",
		"created_by_name": "测试用户",
		"beendelaynum": 0,
		"tableName": "hse_work_ticket",
		"aecolcode": 0,
		"worktype_name": "动火作业",
		"territorialunitid": 2000000003339,
		"hasdrawpaper": "",
		"hassafetyplan": "",
		"aecolcode_attachshowlist": [],
		"territorialunitname": "运行一部",
		"is_pause": 0,
		"ver": 1,
		"tasktype": "dh01",
		"worklevel": "mcq_dh_workLevel02",
		"lock_status": 0,
		"planendtime": fnow2,
		"applyunitname": "长庆石化分公司",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"created_by": 1000,
		"worknumber": "",
		"workunit": 1688712,
		"task_pause": 0,
		"updated_by": 1000,
		"planstarttime": fnow1,
		"isgas_detection": 1,
		"hse_work_task_measure_mcq_m": 20,
		"workcontent": "作业内容123",
		"workticketid": num3,
		"close_type": "",
		"isupgrade": 0,
		"ticketdealphoto_attachshowlist": [],
		"work_position_name": "制氢北区",
		"medium": "戒指",
		"updated_by_name": "测试用户",
		"workway": "mcq_dhfs01",
		"tenantid": 1,
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"actualendtime": "",
		"created_dt": "2020-06-02 19:04:40",
		"worktype": "dh",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isupgradedh": "",
		"isdzdh": "",
		"isdue": 0,
		"updated_dt": now,
		"applyunitid": 1688712,
		"gas_aging": "1",
		"ticketdealphoto": 0,
		"territorialunitcode": "CS8082020",
		"hashseplan": "",
		"worktaskid": num2,
		"ts": ts
	}
}

#rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#手机疑似合并审批，个人防护
num5 = workticketid+1
num6 = workticketid+2
ts = tsi+1
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/ppeHebinAudit.json?worktaskid=%d&workType=zyrw&workTicketids=%d,%d&tabtype=ppe&actionCode=ppe"%(num2,num5,num6)
data = {
	"mainAttributeVO": {},
	"voList": [{
		"isselect": 0,
		"ver": 1,
		"df": 0,
		"created_dt": now,
		"ismust": 1,
		"equipmentname": "安全眼镜",
		"dataStatus": 0,
		"worktype": "xkz",
		"personequipmentid": 2000000000100,
		"person_name": "",
		"created_by": 1000,
		"tableName": "hse_work_task_equipment",
		"worktaskequipmentid": 2000000010018,
		"equipmentcode": "aqyj",
		"updated_dt": now,
		"updated_by": 1000,
		"tenantid": 1,
		"audittype": "",
		"workticketid": num6,
		"worktaskid": num3,
		"isconfirm": 1,
		"signSrc": ""
	}]
}

rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#手机合并审批，气体
num5 = workticketid+1
num6 = workticketid+2
ts = tsi+1
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/gasHebinAudit.json?workType=zyrw&datatype=gas&detectiontype=audit"
data = {
	"mainAttributeVO": {
		"cardnum": "911CDA4D",
		"saveApprvoalInfo": "true",
		"person_type": "orgperson",
		"latitude": 39.98274,
		"idnumber": "",
		"busdata": {
			"cardnum": "911CDA4D",
			"person_type": "orgperson",
			"dataStatus": 0,
			"personid": 2000000009956,
			"person_name": "海顿测试"
		},
		"person_name": "海顿测试",
		"personid": 2000000009956,
		"specialworktype": "",
		"uuid": "1591168224558",
		"longitude": 116.338418
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007038",
		"personList": [{
			"cardnum": "911CDA4D",
			"saveApprvoalInfo": "true",
			"person_type": "orgperson",
			"latitude": 39.98274,
			"idnumber": "",
			"busdata": {
				"cardnum": "911CDA4D",
				"person_type": "orgperson",
				"dataStatus": 0,
				"personid": 2000000009956,
				"person_name": "海顿测试"
			},
			"person_name": "海顿测试",
			"personid": 2000000009956,
			"specialworktype": "",
			"uuid": "1591168224558",
			"longitude": 116.338418
		}],
		"latitude": 39.98274,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 4,
		"isinputidnumber": 0,
		"name": "现场作业负责人",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 4,
		"longitude": 116.338418
	}],
	"voList": [{
		"unCompleteStaticValueList": [{
			"downlimit": 0,
			"groupType": "3",
			"code": "combustible",
			"dataStatus": 0,
			"worktype": ["dh", "xkz"],
			"isShow": 1,
			"expand": "false",
			"isincludeboundary": 1,
			"name": "可燃气体",
			"value": "0",
			"worktypename": ["动火作业", "作业许可证"],
			"workticketid": [num5, num6],
			"upperlimit": 10
		}, {
			"downlimit": 20,
			"groupType": "3",
			"code": "oxygen",
			"dataStatus": 0,
			"worktype": ["dh", "xkz"],
			"isShow": 1,
			"expand": "false",
			"isincludeboundary": 1,
			"name": "氧气",
			"value": "20",
			"worktypename": ["动火作业", "作业许可证"],
			"workticketid": [num5, num6],
			"upperlimit": 25
		}, {
			"downlimit": 0,
			"groupType": "3",
			"code": "hydrogen sulfide",
			"dataStatus": 0,
			"worktype": ["dh", "xkz"],
			"isShow": 1,
			"expand": "false",
			"isincludeboundary": 1,
			"name": "硫化氢",
			"value": "",
			"worktypename": ["动火作业", "作业许可证"],
			"workticketid": [num5, num6],
			"upperlimit": 10
		}, {
			"downlimit": 0,
			"groupType": "3",
			"code": "benzene",
			"dataStatus": 0,
			"worktype": ["dh", "xkz"],
			"isShow": 1,
			"expand": "false",
			"isincludeboundary": 1,
			"name": "苯",
			"value": "",
			"worktypename": ["动火作业", "作业许可证"],
			"workticketid": [num5, num6],
			"upperlimit": 10
		}, {
			"code": "detectiontype",
			"value": ""
		}, {
			"code": "analysisname",
			"value": "合格"
		}, {
			"code": "part",
			"value": ""
		}, {
			"code": "workticketid",
			"value": ""
		}, {
			"code": "detectiontime",
			"value": "2020-06-03 15:09:39"
		}, {
			"code": "iscomplete",
			"value": ""
		}, {
			"code": "created_by",
			"value": ""
		}, {
			"code": "created_dt",
			"value": ""
		}, {
			"code": "updated_by",
			"value": ""
		}, {
			"code": "updated_dt",
			"value": ""
		}, {
			"code": "tenantid",
			"value": ""
		}, {
			"code": "remark",
			"value": ""
		}, {
			"code": "gasdetectionid",
			"value": 2000000002864
		}],
		"commonvo": {
			"dataStatus": 0,
			"lowerlimit": "10",
			"upperlimit": "10"
		},
		"worktype": "dh",
		"dataStatus": 0,
		"titleList": [{
			"groupType": "1",
			"code": "analysisname",
			"name": "分析点名称",
			"dataStatus": 0,
			"isShow": 1
		}, {
			"groupType": "2",
			"code": "detectiontime",
			"name": "检测时间",
			"dataStatus": 0,
			"isShow": 1
		}, {
			"groupType": "1",
			"code": "remark",
			"name": "备注",
			"dataStatus": 0,
			"isShow": 1
		}, {
			"downlimit": 0,
			"groupType": "3",
			"isincludeboundary": 1,
			"code": "combustible",
			"name": "可燃气体",
			"dataStatus": 0,
			"upperlimit": 10,
			"isShow": 1
		}, {
			"downlimit": 20,
			"groupType": "3",
			"isincludeboundary": 1,
			"code": "oxygen",
			"name": "氧气",
			"dataStatus": 0,
			"upperlimit": 25,
			"isShow": 1
		}, {
			"downlimit": 0,
			"groupType": "3",
			"isincludeboundary": 1,
			"code": "hydrogen sulfide",
			"name": "硫化氢",
			"dataStatus": 0,
			"upperlimit": 10,
			"isShow": 1
		}, {
			"downlimit": 0,
			"groupType": "3",
			"isincludeboundary": 1,
			"code": "benzene",
			"name": "苯",
			"dataStatus": 0,
			"upperlimit": 10,
			"isShow": 1
		}, {
			"groupType": "4",
			"code": "2662667",
			"latitude": 0,
			"dataStatus": 0,
			"ismustaudit": 1,
			"force_photo": 0,
			"isEnd": 1,
			"ismulti": 0,
			"isShow": 1,
			"auditorder": 1,
			"isinputidnumber": 0,
			"alarm_type": "gasdetectionexpire_alarm",
			"name": "检测人",
			"audittype": "sign,card,face",
			"isbrushposition": 1,
			"disporder": 1,
			"longitude": 0
		}],
		"workticketid": num5,
		"worktypename": "动火作业"
	}, {
		"unCompleteStaticValueList": [{
			"downlimit": 0,
			"groupType": "3",
			"code": "combustible",
			"dataStatus": 0,
			"worktype": ["dh", "xkz"],
			"isShow": 1,
			"expand": "false",
			"isincludeboundary": 1,
			"name": "可燃气体",
			"value": "",
			"worktypename": ["动火作业", "作业许可证"],
			"workticketid": [num5, num6],
			"upperlimit": 10
		}, {
			"downlimit": 20,
			"groupType": "3",
			"code": "oxygen",
			"dataStatus": 0,
			"worktype": ["dh", "xkz"],
			"isShow": 1,
			"expand": "false",
			"isincludeboundary": 1,
			"name": "氧气",
			"value": "20",
			"worktypename": ["动火作业", "作业许可证"],
			"workticketid": [num5, num6],
			"upperlimit": 25
		}, {
			"downlimit": 0,
			"groupType": "3",
			"code": "hydrogen sulfide",
			"dataStatus": 0,
			"worktype": ["dh", "xkz"],
			"isShow": 1,
			"expand": "false",
			"isincludeboundary": 1,
			"name": "硫化氢",
			"value": "",
			"worktypename": ["动火作业", "作业许可证"],
			"workticketid": [num5, num6],
			"upperlimit": 10
		}, {
			"downlimit": 0,
			"groupType": "3",
			"code": "benzene",
			"dataStatus": 0,
			"worktype": ["dh", "xkz"],
			"isShow": 1,
			"expand": "false",
			"isincludeboundary": 1,
			"name": "苯",
			"value": "",
			"worktypename": ["动火作业", "作业许可证"],
			"workticketid": [num5, num6],
			"upperlimit": 10
		}, {
			"code": "detectiontype",
			"value": ""
		}, {
			"code": "analysisname",
			"value": "合格"
		}, {
			"code": "part",
			"value": ""
		}, {
			"code": "workticketid",
			"value": ""
		}, {
			"code": "detectiontime",
			"value": "2020-06-03 15:09:39"
		}, {
			"code": "iscomplete",
			"value": ""
		}, {
			"code": "created_by",
			"value": ""
		}, {
			"code": "created_dt",
			"value": ""
		}, {
			"code": "updated_by",
			"value": ""
		}, {
			"code": "updated_dt",
			"value": ""
		}, {
			"code": "tenantid",
			"value": ""
		}, {
			"code": "remark",
			"value": ""
		}],
		"commonvo": {
			"dataStatus": 0,
			"lowerlimit": "10",
			"upperlimit": "10"
		},
		"worktype": "xkz",
		"dataStatus": 0,
		"titleList": [{
			"groupType": "1",
			"code": "analysisname",
			"preValue": "厂房",
			"name": "分析点名称",
			"dataStatus": 0,
			"isShow": 1
		}, {
			"groupType": "2",
			"code": "detectiontime",
			"preValue": "2020-06-03 15:06:11",
			"name": "检测时间",
			"dataStatus": 0,
			"isShow": 1
		}, {
			"groupType": "1",
			"code": "remark",
			"name": "备注",
			"dataStatus": 0,
			"isShow": 1
		}, {
			"downlimit": 0,
			"groupType": "3",
			"isincludeboundary": 1,
			"code": "combustible",
			"name": "可燃气体",
			"dataStatus": 0,
			"upperlimit": 10,
			"isShow": 1
		}, {
			"downlimit": 0,
			"groupType": "3",
			"isincludeboundary": 1,
			"code": "hydrogen sulfide",
			"name": "硫化氢",
			"dataStatus": 0,
			"upperlimit": 10,
			"isShow": 1
		}, {
			"downlimit": 0,
			"groupType": "3",
			"isincludeboundary": 1,
			"code": "benzene",
			"name": "苯",
			"dataStatus": 0,
			"upperlimit": 10,
			"isShow": 1
		}, {
			"downlimit": 20,
			"groupType": "3",
			"isincludeboundary": 1,
			"code": "oxygen",
			"name": "氧气",
			"dataStatus": 0,
			"upperlimit": 25,
			"isShow": 1
		}, {
			"groupType": "4",
			"code": "2000000005635",
			"latitude": 0,
			"dataStatus": 0,
			"ismustaudit": 1,
			"force_photo": 0,
			"isEnd": 1,
			"ismulti": 0,
			"isShow": 1,
			"auditorder": 1,
			"isinputidnumber": 0,
			"name": "现场作业负责人",
			"audittype": "sign,card,face",
			"isbrushposition": 1,
			"disporder": 1,
			"longitude": 0
		}],
		"workticketid": num6,
		"worktypename": "作业许可证"
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#手机合并审批，危害
num5 = workticketid+1
num6 = workticketid+2
ts = tsi+1
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/harmHebinAudit.json?worktaskid=%d&workType=zyrw&workTicketids=%d,%d&tabtype=harm&actionCode=harm"%(num2,num5,num6)
data = {
	"mainAttributeVO": {},
	"voList": [{
		"isselect": 0,
		"df": 0,
		"ver": 1,
		"created_dt": "2020-06-03 15:06:11",
		"ismust": 1,
		"dataStatus": 0,
		"worktype": "xkz",
		"person_name": "",
		"harmid": 2000000008710,
		"harmcode": "gzxy001",
		"harmname": "爆炸性气体",
		"created_by": 1000,
		"tableName": "hse_work_task_harm",
		"worktaskharmid": 2000000019723,
		"updated_dt": "2020-06-03 15:07:50",
		"tenantid": 1,
		"updated_by": 1000,
		"audittype": "",
		"worktaskid": num2,
		"workticketid": num6,
		"ismustconfirm": 0,
		"isconfirm": 1,
		"signSrc": ""
	}, {
		"isselect": 0,
		"df": 0,
		"ver": 1,
		"created_dt": "2020-06-03 15:06:11",
		"ismust": 1,
		"dataStatus": 0,
		"worktype": "xkz",
		"person_name": "",
		"harmid": 2000000008711,
		"harmcode": "gzxy002",
		"harmname": "易燃性物质",
		"created_by": 1000,
		"tableName": "hse_work_task_harm",
		"worktaskharmid": 2000000019724,
		"updated_dt": "2020-06-03 15:07:49",
		"tenantid": 1,
		"updated_by": 1000,
		"audittype": "",
		"worktaskid": num2,
		"workticketid": num6,
		"ismustconfirm": 0,
		"isconfirm": 1,
		"signSrc": ""
	}, {
		"isselect": 0,
		"df": 0,
		"ver": 1,
		"created_dt": "2020-06-03 15:07:47",
		"ismust": 1,
		"dataStatus": 0,
		"worktype": "dh",
		"person_name": "",
		"harmid": 2000000008667,
		"harmcode": "dhzy001",
		"harmname": "爆炸",
		"created_by": 1000,
		"tableName": "hse_work_task_harm",
		"worktaskharmid": 2000000023523,
		"workway": "mcq_dhfs01",
		"updated_dt": "2020-06-03 15:07:47",
		"tenantid": 1,
		"updated_by": 1000,
		"audittype": "",
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 1,
		"signSrc": ""
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#手机合并审批，作业风险消减措施
num5 = workticketid+1
num6 = workticketid+2
ts = tsi+1
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/measureHebinAudit.json?worktaskid=%d&workType=zyrw&workTicketids=%d,%d&tabtype=measure&businesstype=zyfxxjcs&actionCode=measure"%(num2,num5,num6)
data = {
	"mainAttributeVO": {
		"cardnum": "911CDA4D",
		"saveApprvoalInfo": "true",
		"person_type": "orgperson",
		"latitude": 39.982751,
		"idnumber": "",
		"busdata": {
			"cardnum": "911CDA4D",
			"person_type": "orgperson",
			"dataStatus": 0,
			"personid": 2000000009956,
			"person_name": "海顿测试"
		},
		"person_name": "海顿测试",
		"personid": 2000000009956,
		"specialworktype": "",
		"uuid": "1591152230035",
		"longitude": 116.338439
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"groupType": "4",
		"code": "2000000006988",
		"personList": [{
			"cardnum": "911CDA4D",
			"saveApprvoalInfo": "true",
			"person_type": "orgperson",
			"latitude": 39.982751,
			"idnumber": "",
			"busdata": {
				"cardnum": "911CDA4D",
				"person_type": "orgperson",
				"dataStatus": 0,
				"personid": 2000000009956,
				"person_name": "海顿测试"
			},
			"person_name": "海顿测试",
			"personid": 2000000009956,
			"specialworktype": "",
			"uuid": "1591152230035",
			"longitude": 116.338439
		}],
		"latitude": 39.982751,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"name": "作业单位措施确认及安全教育人",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 1,
		"longitude": 116.338439
	}],
	"voList": [{
		"measuredesc": "1.在动火点处设置隔离设施",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 1,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000005024,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dhzy12",
		"dataStatus": 0,
		"worktype": "dh",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "zyfxxjcs",
		"updated_dt": now,
		"worktaskmeasureid": 2000000045595,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": "1"
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#手机合并审批，工艺风险消减措施
num5 = workticketid+1
num6 = workticketid+2
ts = tsi+1
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/measureHebinAudit.json?worktaskid=%d&workType=zyrw&workTicketids=%d,%d&tabtype=measure&businesstype=gyfxxjcs&actionCode=measure"%(num2,num5,num6)
#签名数据
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"groupType": "4",
		"code": "2000000006987",
		"latitude": 39.982854,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\nSUVORK5CYII=\n",
			"uuid": ""
		}],
		"name": "属地措施确认及安全教育人",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\nSUVORK5CYII=\n",
		"isbrushposition": 1,
		"disporder": 1,
		"longitude": 116.337967
	}],
	"voList": [{
		"measuredesc": "2.管道容器内可燃介质用蒸汽、氮气或水处理干净",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 1,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000005014,
		"isselect": 0,
		"ver": 1,
		"created_dt": "2020-06-03 11:05:45",
		"measurecode": "dhzy02",
		"dataStatus": 0,
		"worktype": "dh",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "gyfxxjcs",
		"updated_dt": "2020-06-03 11:05:45",
		"worktaskmeasureid": 2000000045685,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": "1"
	}, {
		"measuredesc": "3.清除动火点周围的可燃介质和可燃物",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 1,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000005015,
		"isselect": 0,
		"ver": 1,
		"created_dt": "2020-06-03 11:05:45",
		"measurecode": "dhzy03",
		"dataStatus": 0,
		"worktype": "dh",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "gyfxxjcs",
		"updated_dt": "2020-06-03 11:05:45",
		"worktaskmeasureid": 2000000045686,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": "1"
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#手机合并审批，工作前安全措施
num5 = workticketid+1
num6 = workticketid+2
ts = tsi+1
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/measureHebinAudit.json?worktaskid=%d&workType=zyrw&workTicketids=%d,%d&tabtype=measure&businesstype=gzqaqcs&actionCode=measure"%(num2,num5,num6)
data = {
	"mainAttributeVO": {
		"cardnum": "911CDA4D",
		"saveApprvoalInfo": "true",
		"person_type": "orgperson",
		"latitude": 39.982754,
		"idnumber": "",
		"busdata": {
			"cardnum": "911CDA4D",
			"person_type": "orgperson",
			"dataStatus": 0,
			"personid": 2000000009956,
			"person_name": "海顿测试"
		},
		"person_name": "海顿测试",
		"personid": 2000000009956,
		"specialworktype": "",
		"uuid": "1591162714351",
		"longitude": 116.338475
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"groupType": "4",
		"code": "2000000006990",
		"personList": [{
			"cardnum": "911CDA4D",
			"saveApprvoalInfo": "true",
			"person_type": "orgperson",
			"latitude": 39.982754,
			"idnumber": "",
			"busdata": {
				"cardnum": "911CDA4D",
				"person_type": "orgperson",
				"dataStatus": 0,
				"personid": 2000000009956,
				"person_name": "海顿测试"
			},
			"person_name": "海顿测试",
			"personid": 2000000009956,
			"specialworktype": "",
			"uuid": "1591162714351",
			"longitude": 116.338475
		}],
		"latitude": 39.982754,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"name": "措施确认人（属地/作业方）",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 1,
		"longitude": 116.338475
	}],
	"voList": [{
		"measuredesc": "切断工艺流程",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 1,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000004946,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "gzxk01",
		"dataStatus": 0,
		"worktype": "xkz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "gzqaqcs",
		"updated_dt": "2020-06-03 11:44:53",
		"worktaskmeasureid": 2000000042204,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": num6,
		"worktaskid": num2,
		"isconfirm": "1"
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#手机合并审批，会签前检查
num5 = workticketid+1
num6 = workticketid+2
ts = tsi+1
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/beforeHebinSignValidate.json?worktaskid=%d&workTicketids=%d,%d"%(num2,num5,num6)

rs = requests.get(url = url,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#手机合并审批，申请人会签
num5 = workticketid+1
num6 = workticketid+2
ts = tsi+1
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000006894",
		"latitude": 39.982719,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\nAAAAAIBj+x/KNec4fbkNOwAAAABJRU5ErkJggg==\n",
			"uuid": ""
		}],
		"name": "申请人",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\nAAAAAIBj+x/KNec4fbkNOwAAAABJRU5ErkJggg==\n",
		"isbrushposition": 1,
		"disporder": 1,
		"longitude": 116.338469
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#手机合并审批，作业人会签
num5 = workticketid+1
num6 = workticketid+2
ts = tsi+1
#url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
data ={
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000006895",
		"latitude": 39.982719,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 2,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "作业人",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 2,
		"longitude": 116.338469
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#手机合并审批，属地监护人会签
num5 = workticketid+1
num6 = workticketid+2
ts = tsi+1
#url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000006896",
		"latitude": 39.982719,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\nTkSuQmCC\n",
			"uuid": ""
		}],
		"name": "属地监护人",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\nTkSuQmCC\n",
		"isbrushposition": 1,
		"disporder": 3,
		"longitude": 116.338469
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#手机合并审批，作业单位监护人会签
num5 = workticketid+1
num6 = workticketid+2
ts = tsi+1
#url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000006897",
		"latitude": 39.982735,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 4,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\nRU5ErkJggg==\n",
			"uuid": ""
		}],
		"name": "作业单位监护人",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\nRU5ErkJggg==\n",
		"isbrushposition": 1,
		"disporder": 4,
		"longitude": 116.338297
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#手机合并审批，当班班长会签
num5 = workticketid+1
num6 = workticketid+2
ts = tsi+1
#url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000006898",
		"latitude": 39.982723,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 5,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "iVBORw0KGgoAAAANSUhEUgAAAhwAAAGhCAYAAAAqQm1KAAAAAXNSR0IArs4c6QAAAARzQklUCAgI\nCHwIZIgAAA/eSURBVHic7d17rGXVQQbwj5nhUehAmcI4KI8BDUqVthrTpkqBVmJ4FGtrmyjRkNin\nghSwjtaiiS0N1Zr6B9GktjU+2ioGwdo2QCCtSQOUVA0vlSJPoQgMj+EtDHD948yk471r3ztzZ++9\n7lnn90tWLmzOnPOdgdnnY6119k4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgO2+keTJJO+qHQQAaNPcvPH2unEAgNb8TxYWjs1V\nE8EMWVU7AMAI/iHJhsLxW8YOAgC06aQsnNnYPgAAdtu+6S4br6yYCwBoSFfZOK1mKACgHY+mXDau\nrhkKAGjHF1MuG8/UDAUAtOP42CQKAAxo73SXjXUVcwEADekqG2fUDAUAtOOhlMvG9TVDAQDt+LPY\ntwEADOhHomwAAAPrKhvra4YCANrRVTbOqhkKAGjHNSmXjTtqhgIA2vGjsW8DABhYV9nYs2YoAKAd\nj6dcNk6tGQoAaMdHUy4bt9YMBQC0Y5/YtwEADKyrbLyqZigAoB1/mXLZuKhiJgCgIQenXDaerxkK\n2DV71A4AsISuPRqrFvlnwAqzqnYAgEV8s+P4+6NsAAA9WJ/yUspjNUMBy2NJBVipumYwnLdgCllS\nAVaiv+04/u5RUwAAzTog5aWULTVDAbvH1CSw0lhKgQZZUgFWkq4LeZ01agoAoGku8AUADKrrtvOr\na4YCANpxYspl448rZgJ6ZBMWsBLYKAqNs2kUqO26juOHjJoCAGjW2pSXUv6lZiigf6YrgZpeTHlT\nqHMTNMaSClDLaSmXjZPHDgIAtKu0lPJC1UQAQFM+k3LhWFszFADQllLZ+PeqiQCAptybcuEAAOjF\n/imXjY/XDAUAtOW5mN0AAAZ0dMpl4ydqhgLG4eI6wFhKMxkvx91gYSa48BcwhlM6jh8+agoAoGml\npZQnqiYCAJpyTsqFY5+aoQCAtpTKxt1VEwEATTkvvgYLAAysVDZuqJoIAGjKuTG7AQAMrFQ2vl41\nEQDQlA/F7AYAMLBS2bi6aiIAoCnvj9kNAGBgpbJxVdVEAEBTTorZDQBgYKWycUvVRABAUzamXDjc\nlRoA6M3zWVg2Hq6aCABoytqUZzfW1gwFALTl4SwsG89XTQQANGVVyrMbGytmAgAac0t8FRYAGFip\nbLy1aiIAoCmXxuwGADCwUtl4T9VEsLIcUTsAwLT7o5jdgPl+N8mz8ecCoDelsvGJqolgfJuSPJ3y\nn4cdx8W1AgJMs/fF7Aaz6cNJnszSBWP+uLxGWIBpVzqhfqlqIhjGeUm2ZNcLhjIOsJt+OE6otOtD\nSR7L7heM7eO/x40P0I7STdruqpoIlu+slC/Nv9xxX3xTC2C37ZXySXavmqFgF/x6kofSX8F4IJM9\nTQD06LYsPOFurZoIuu2R5Jz0O4PxYJIPjvkmAGZR6QT82qqJ4Hv2zOQ6GE+lv4KxOZNlFwBG8pnY\nLMrK8uokf5LkxfRXMB7NZFZkjxHfBwA7KJ2cz6maiFnzpiSXpb9yMZfJbMj5Y74JALqdGbMbjO/M\nJLek34LxeCYFwwwGwApUOnH/fdVEtOboJH+aySbkPgvGw7FEAjAVjozZDfq1JpONmN9Jv+ViLsnt\nmcyMADBlSne+vL9qIqbNzye5Iv2Xi7kk1yY5dby3AsAQ1qR8kl9bMxQr1qokv5Tk6gxTLuaSfCHJ\nsWO9IQDGcVMWnvBfrpqIlWL/JOem/N9IX+PRJBckeeVI7wmASkofAifWDEQVx2VyHZanM1y5mEvy\nlSQnjfSeAFghPpXyhwLtOjzJbyX5doYtFnNJbs7kvibuwwMw40ofEhdUTURfjsjkWhTXZfhiMZfJ\ntTTOSbLvGG8OgOnx5uza7MZ7MrnnxBVJXj94OnbW65P8XpIbM06xmMvkWyNuzw7ATnkpCz9IvtXx\n2J8rPHb7OG/wpGzI5LoTl6T8FeYhx2VJ3jb8WwSgRV1fhV3T8fjvdjx+/rgkyYFDBm/YcUk+kuTK\njFsoto+7kvxBkh8a+o0CMDu+lYUfOFsXefzlhcfvzPirJD8zyDuYLm9McnaSv07yn6lTKLaPZzP5\n9+JCWvTOteWB+eYKx47LZG1+V37Ncl2Z5Jpt46Yen3dMhyQ5Jslrtv08JskbkuxXM9QOHsukKP5j\nkq9WzsKMUDiAHf1OkosKx3fmXHFAkr9LcnKvico2J7k7yT3bft69w9/fvsznXFsYRyQ5bNs4fIe/\nnpYrrd6Q5GtJ/inTW94AaFBpmv2Ty3yuTR3PZ/Q7vpPk4iSn7dy/FgCo6/tS/kDrw1FJvtzx/Mbi\n4+Ekl2ZyHQtfOQZg6j2YhR929w70Wj+Z5HOF15vFcX8mNyR7b3wLhIbZwwFsN1c4dlAmN9Aay+FJ\nTkjy45n83/zrkqwb8fX7dFMm3zrZPm7OZPkDZpLCASTJH2ay52K+lXqO+MFMyslRSTZuG4dt+/vD\nlvmcz2Zyc7Knto0nkmzJpHA9su3n9vFQktuSPL7M1wKAmVSa6j+/aiIAoClHp1w4AAB6szkLy8at\nVRMBAM0pzW6slCtiAgAN+O1YTgEABlYqGxdUTQQANGW/mN0AAAZ2fRaWjS1VEwEAzSnNbhxdNREA\n0JQ3xXIKADCwx7KwbFxeNREA0JzS7MaeVRMBAE05M5ZTAICBvZyFZeOTVRMBzVupt54GhlOazXAu\nAAa1qnYAYFTvrR0AAGjfi1m4nLKpaiJgJphGhdliOQWowpIKzI5frB0AAGjf01m4nPKxqomAmWEq\nFWaH5RSgGksqMBsOqB0AAGjfn2fhcsq1VRMBAM0pXcr8DVUTATPF+i3MBvs3gKrs4YD2vaJ2AACF\nA9p3duHYVaOnAACadl8W7t84vWoiYOZYw4X22b8BVGdJBQAYnMIBAAxO4YC2vbp2AIBE4YDWva5w\n7PrRUwAzT+GAtm0sHLtr7BAACge0bWPh2D0jZwBQOKBxGwrH7hk7BIDCAW1bUzj27OgpgJmncEDb\nSoWjdCEwgEEpHNC2FwvH9hw9BTDzFA5o23cLxw4ZPQUw8xQOaFupcHz/6CmAmadwQNtuLxx78+gp\ngJnnjpHQPneLBaozwwEADE7hgNm0unYAYLYoHNC+WwvHLhw9BQDQtLdmso9j/gAA6FWpcPxs1UQA\nQHPuSLl0uCYHANCbvVMuHHNJzqiYCwBozNfSXTrmkryvXjQAoCV3ZvHSMZfk5iSn1goItMnVBmH2\nPJbkwF38Ndcm+UaSe5PcneSlwmP2SbLXTowdv47/ZJJHkmye9/PpXcwHAKxAH8nSMx0rcdyZ5NNJ\nTuj/twQAGErtAtHn+GySn+73twcA6MuqJNekfmHoe2xNsqnH3ycAoEebUr8sDDE+3+dvErBrbBoF\nlnJwksOSHJrkkG1jQ5L1Sdbt8LgX5o3nC8deyP/fcPqqbc+/foefhwz3VpJMNqQemcnmVACABU7N\nZNPobdn9GY+7Rs4OAEy5o5JclMnXane1eKwrPB8AwE75lUyu86F0AACjOCNLlw4AgF6cku7C4eqm\nAECvukrHB2qGgpb5Wiwwq15O+RzovAgDWLX0QwCatF/H8Q+PmgIAaN6/xQZSAGAEpcJxYNVEAEBz\ntmRh4fhK1UQAQHOOjWUVGJzd2ADlguH8CD3yLRWA5JnCsbeNngIatrp2AIAVYN8kx887tj7J31TI\nAgA0an3s44BBWaMEmLCPAwZkDwcAMDiFAwAYnMIBAAxO4QCYeLRwbN3oKaBRCgfAxF6FY8+PngIa\nZQc2wIRvqcCAzHAAAINTOACAwSkcAMDgFA6A5JcLx2wYBQB69UAW3kflN6smgsbYgQ3gGyowOEsq\nwKw7pXYAAKB9L2ThcsoXqyYCAJozv2zMJVldNRE0yJIKMMs+3XH8pVFTAABNK81unF01EQDQlNek\nXDgAAHrzTBaWjTuqJgIAmlOa3di/aiIAoCmXxXIKADCwUtl4d9VEAEBTzo3ZDQBgYKWy8RdVEwEA\nTXlnzG4AAAMrlY1vVk0EADTlHTG7AQAMrFQ27qyaCABoyq/G7AYAMLBS2bixaiIAoCmfitkNAGBg\npbJxVdVEAEBTro/ZDQBgQHunXDYurBkKAGjL/8bsBgAwoLekXDbeXjMUzLI9agcAGEBpJuOlJGvG\nDgJMrKodAKBnX+o4ftCoKQCAZq1JeSnlppqhAIC2bI2NogDAgH4j5bLx0ZqhgAmbRoFWdM1kOM/B\nCmDTKNCCRzqOrx01BQDQrA+mvJRyac1QAEA79km5bNgoCgD0pqtsHFEzFADQjhtTLhtX1AwFALTj\nF1IuG1trhgIA2rEx3UspvgILAOy21ekuG2+pmAsAaEhX2fjnipkAgIY8l3LZ2FwzFADQjqfiehsA\nwIAejbIBAAzogXSXjXUVcwEAjXg83WXj4Iq5AIBGbE132dhQMRcA0IiuojGXyUW/AACWbbE7vyob\nAMBuOzSLl4219aIBAC04IYuXjTX1ogEALdiUxcsGAMBu+Xq6i8YzFXMBAI14MN1l4556sQCAVryc\n7rJxdcVcAEADjsji+zV+v140AKAF52fxsnFitWQAQBNuz+Jl46B60YCx7FE7ANCsNZncE6XLXJJV\nI2UBKvOHHRjCT2XxsnFfnH8AgN1weRZfQrm4XjQAoAXPZvGycUy9aADAtHtnFi8aL9aLBgC04P4s\nXjZuqBcNAJh2x2bxojGX5F3V0gEAU+/aLF029q2WDgCYam/M0kXjimrpAICptjrJlixdNo6qFRAA\nmG7/mqWLxp3V0gEAU+2rWbpozCU5uVZAAGD5Pp7vfZi/osLr35SdKxr3VsgGAPRgU+rcTfX0JM8V\nXrtrHDpCJgBgIF0f8BsGeK3XJvmvRV6zNH5tgBwAwMi+nO4P++N7eP4js3ObQOePj/Xw2gDACrLY\nB/+Vy3i+H0vy7SWet2t8YjfeBwCwwi1119VLFvm1a5NcmF3bkzF/nN73GwIAVqYnsvzCsJzxhSSr\nRnlnAMCKsrNfUV3uuC7DbEgFAKbMB9Jvybg6yQ+M+g4AgKlxXZZfMj6bZM34kQGAafWOJP+RxQvG\nNbHxEwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAABgGv0fJjC4AxZcausAAAAASUVORK5CYII=\n",
			"uuid": ""
		}],
		"name": "当班班长",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 5,
		"longitude": 116.338397
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#手机合并审批，工艺
num5 = workticketid+1
num6 = workticketid+2
ts = tsi+1
#url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000006899",
		"latitude": 39.982724,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 6,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "工艺",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 6,
		"longitude": 116.33846
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#手机合并审批，设备
num5 = workticketid+1
num6 = workticketid+2
ts = tsi+1
#url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000006900",
		"latitude": 39.982724,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 7,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\npvjP2RrBAAAAAElFTkSuQmCC\n",
			"uuid": ""
		}],
		"name": "设备",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\npvjP2RrBAAAAAElFTkSuQmCC\n",
		"isbrushposition": 1,
		"disporder": 7,
		"longitude": 116.33846
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#手机合并审批，安全
num5 = workticketid+1
num6 = workticketid+2
ts = tsi+1
#url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000006901",
		"latitude": 39.982785,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 8,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\nRU5ErkJggg==\n",
			"uuid": ""
		}],
		"name": "安全",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\nRU5ErkJggg==\n",
		"isbrushposition": 1,
		"disporder": 8,
		"longitude": 116.338409
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#手机合并审批，组长/队长
num5 = workticketid+1
num6 = workticketid+2
ts = tsi+1
#url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000006902",
		"latitude": 39.982785,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 9,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\nABr7X8zKB9O35nSzAAAAAElFTkSuQmCC\n",
			"uuid": ""
		}],
		"name": "组长/队长",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "iVBORw0KGgoAAAANSUhEUgAAAhwAAAGhCAYAAAAqQm1KAAAAAXNSR0IArs4c6QAAAARzQklUCAgI\nCHwIZIgAABEgSURBVHic7d19rORXXQfg7+62292+gX2jgG0XBSRY6YuUEpBAI1KQWANqIxCrUVJe\nDDXYWo0olKiV+IJG4gslwRZMqqgIFUKkQROplBdtWl8ipWCt29ra7ra63b5td3v9427jOnPO3Llz\n55wz8zvPk0yanDl37mfnpvd87u+cmYkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAqGxT6wDAYHxHRJwb\nEd8WEU+LiJMi4vCIuDsi/jMi/jkiboyI21oFBAAW3zMj4h0R8bmIWJnT7ZMR8aya/wgAYHGcHxHX\nxfyKxTS3OyPiZTX+cQBAfYdFxC9HxIGoWzDWKh/fU/IfDQCU95yI+Gq0LxbT3O6KiG8p8zQAtTg0\nCv04JSI+HhEvLPDY90fEv0bErRHxjVg9KHpPROyL1bJw6sH/PneD3/+ciPj7DSUFAIp4Q8zvasNn\nI+LSWC0OG3VcRHxihgznzOF7AwBz8tqYvVj8dUT8SERsqZR1S0R8cMpst1fKBABMcHxE7I/1FYzr\nI+IFLcImHB4R10Y+6yfaRQMAIlbPaExbMj4aEdvaxJzajlg9C3JobgCgoWlKxp3N0g3Px2L1sOxb\nWgcBgBpeE2sXjfuapRuebZG+WgQAg/WXsXbZOLtZuuHZFPnnGQAG6aaYXDSubRdtsCY93wAwODvD\n4lfbQ5F/vv+rYS4AKOKByC98NzXMNWS3xOSC96Z20QBg/vZGftG7smGuIXtPrH1OBgAGY1/kF7yX\nNMw1ZM+P6V5uDACDMOmj449vmGvIDo/pysZVrQICwDxNWuyOaphr6KYpGysRcUSrgAAwD5Pe88FC\nV9YdMX3hAICltT0mL3Kb20UbvF+K6cvGvY0yAsCGnRT+om7lmTF92ViJiB9sExMANuZ5oWy0lHve\nT86MA8DSmVQ2Hm+Yqxe7Iv3cvyMivjdzHwAslWdHvmzsbZirF++K9HN/28H7H0nc9776MQFgdpPK\nhs/oKO+YWHsLy9UNAJbasyK/2N3eMFdPcs//sQfvvyRzPwAshR2RX+x2tovVlS9G+vm/7JA5qfsv\nrxsTAGaXKxt3tgzVkTNj7W2s3EFeAFgKubJxd8tQnZnmpcePJe539QmApXBvKBut5X4Gpx8y59jM\nnGOqJgWAGXwy0ovYoy1DdeaHI/0z+OLIvEcTc56oFxMAZnNBTHcZn7Km+RmclZnzimopAWAGWyO/\n0B3dMFdv9sbkl8A+KTXH1Q0AFl6ubJzXMlRnfirSP4MPjsy7IjPvxFpBAWAWn4r0AvaxlqE6szmm\nu2qxJTPvjmpJAWAGT430AubD2OpKvbx1JSK2jcx7ODMPABZabivlsJahOvPTkf4ZXDky762Zeb9Y\nLSkAzCD3CaTvbRmqQ9NeYUrN218pIwDMzFZKew/GdFeYclsuW6slBYAZXBe2Ulq7KNI/g18fmXdl\nZt4HqiUFgBmlFrDfa5qoP7nzM4c6asp5ALBw/iEsYK3dHemfweibrOXKxuirVwBg4aQWsPc3TdSX\n74z0z+DqkXmfz8x7X62gADCrj4erG61Ns0VyZmaOQ70ALIXUIvYrTRP1JVf4vnlkXq6UbK6WFABm\nlHuDKerYHunn/59G5j2UmffmakkBYAOc3Whrf6xd+H43M2dnvZgAMLtTw9WNli6O9PN/4SFzdmTm\n+DkBsDR2xfgi9o2mifqSKhGPTjFnJSJOrhcTADYmtZAd2TRRP74c6ef/0Hd1fSAzx5YXAEvjinCZ\nvpVjYu333PiNzJw9NYMCwEalFrNLmibqx76YXPZOy9yvEAKwVLaExayV10X6uX/pIXNyZWNHzaAA\nsFF/EOOL2d6mifqx1kHRPZk5PkQPgKWTWtBe3jRRH/400s/9EQfvz73fxoPVkwLAHNhOaSP1vH/m\n4H3PydzvZwPAUkqdIfDKh/LujcllwrkNAAblhhhf1C5vmmj4nh7pMnHxwftzn5Pym9WTAsCcpBa2\nbU0TDd+krZIPZ+7bVT8mAMyPMwJ1vSHSz/nzD96c2wBgcL4pLG61pZ7vhybctxIRx9ePCaRsbh0A\nltRLEmOfrZ6iHx/KjJ8QEY9k7vuZiNhdJg4A1PGrMf7X9HubJhq21NWLf4mIP8ncd3ubmAAwX38b\n44vcq5smGq6bIl0qzsiM29oCYDAej/FF7ilNEw1XqlBclRlfiYgj28QEgPnzV3Ud90e+WKRuF7WJ\nCQBlKBzlPSPWVzZubhMTmMam1gFgSaUKhv+f5uuJWN9z6vmHBeZlscAienmsr0BsLRUEAFqypVLW\nerZSvDoIgMFSOMq5PKYvGzc0ygiskz1PmI0zHOVMW95WwrYwLA3/swKL5Np1zD2sWAoAWBD7wgeF\nlTDtVspLWwUEgJpujPFF8LubJlp+t8V0ZeMzrQICs7OlArO5KTF2bvUUw7EtIp49xbz9EfGawlmA\nAhQOmM3nEmMWwtntmnLe4UVTAMCCOSK8NHZedsR0WylnNMoHAE0pHPMxTdn442bpAKAxhWPjzo+1\ny8aDzdIBwAJILY4nN020fKa5ugEMgEOjMLu/SIz9WO0QS+zSKeZsK54CABbcBTH+1/iepomWy1pX\nNs5pFw0AFostgNl8OCaXjd9pFw0AFo/CMZtJZeOWhrkAYCHdGuML5mVNEy2+r0S+bNzRMBcALKzX\nh6sc6/GtkS8b/9MwFwAsPIVjOi+KfNl4rGEuAFgK+2N8AX1/00SLJ3claCUinmiYCwCWxsXhKsck\n7w5v7AUAc5FaSF/ZNNFi+LOYXDZObxcNAJbPjeGv91H3hLctB4C5Sy2ob2uaqJ21isZK+NwZAJjJ\nfeGv+FNiurKxt1VAAFh22yO9uP5Wy1AVvSmmKxsrEfGURhkBYBDuiPQCe1TLUBX8XUxfNnY1yggA\ng9LbAcnHYvqysRI+ch66tLl1ABig386M31Q1RXmnxmqB2LqOr9kZEY+WiQMA/cn9df+qlqHm6Bdi\n8lWM+zPjAMAcbY3hHpi8PSaXjUsjYk9ifE+LsAAwdK+NYZ3nODqme2+NXNk6sX5kAOjDpyK9+O5r\nGWoGb4/JRePQcxm3Ju73AW0AUNjuSC/Sy3KI9OsxuWxcPzI/NeeFtcICQM9yi/Uif8DbcbH2Fsro\nIdirM/MAgAq2RH7R3tQwV87VMbloHIjVf9Oo1NyLyscFAJ50eqQX5MdbhhqxPVbPW0wqG5/PfO0r\nM/MBgMquj/Si/IctQx30a7H2Fsp3Tfj6A4n5ny6YFwCYILeYP6NRnhMnZFrPlQpXNwBgwcy6qM/b\nVyZkefJ2xRSP81eZrwUAGnprpBfof6z0/X8g8/1HD4ZO+zkpqa9/xVwTAwAzuTfSC/WLC37PU2P1\nkOpaZeP31/GYr848BgCwIGptrTx9wvcavR29zsdOfW7KR+eSGgCYi7Mjvejvn9PjnxARD2e+x+jt\nbTN+j9Rjpd6jAwBo6MZIL9pf28BjfiDzmKnbVzfwfX4885gAwALKlYG71vEYb5nwOLnbaQVyX7HB\nxwQACppUDP4tIp47Mv/CiLh2ja/L3S4omBkAWGBnxmzlYT23n5xj3ssy3wMAWHBnRZmicX6BrKnP\nXPFBbQCwJE6O+ZSMPy+c09UNABiAS2J9BePhiHhnpWzfn8kAACyp0yLilvj/C/vuiLgmVt/ls4Vd\nMV423tUoC7AENrUOACyl1NUMv0+ArM2tAwBL59tbBwAAhu9LMb6dck3TRADA4KQOi25vmggAGJTt\n4dUpAEBhfxTjZeMLTRMBAIOTurrxvKaJgKXgZWzAeng5LDATL4sFpvWexNju6ikAgEFLbad8X9NE\nwNJwKRSYlu0UYGa2VIBpeHdRAKC4T8f4dspHmiYCAAYndX7jxKaJgKVi/xWYhvMbwIY4wwGs5fWJ\nsQPVUwAAg/b1GN9OeXfTRMDScUkUWEtqO2VzZhwgyZYKMEnujxJlA1gXhQOY5OcSY/dVTwEADNr+\nGD+/8camiYCl5AwHMImXwwJzYUsFyPHGXgBAcVfF+HbK3zRNBAAMTurtzM9tmghYWvZigRznN4C5\ncYYDSDm6dQBgWBQOIOVnE2Nfrp4CABi0R2L8/MYFTRMBS81+LJDi/AYwV7ZUgFF+LwBz5xcLMOrt\nibF/rx0CABi23TF+fuPNTRMBS8+eLDDK+Q1g7mypAADFKRzAoS5MjO2tngIAGLSbY/z8xs83TQQA\nDE7qA9sOa5oIGAQHwYBDOTAKFOEMB/Ck01sHAACG70Mxvp3ykaaJAIDBORDjhePspomAwbA3CzzJ\n+Q2gGGc4AIDiFA4gIuKNibGd1VMAAIP2pRg/v/HOpokAgMHxhl9AUQ6EAREOjAKFOcMBnNA6ADB8\nCgdwWWLsuuopAIBBezjGz2+c1zQRMDj2aAHnN4DibKkAAMUpHNC3FyTGHq+eAhg8hQP69hOJsWuq\npwAABi11YPTFTRMBg+RgGPTNgVGgClsqAEBxCgf065TWAYB+KBzQrx9KjHmHUQBgrm6I8QOjP9o0\nEQAwOKmPpD+qaSJgsJxGh355hQpQjTMcAEBxCgf0aWvrAEBfFA7o0+sSY1+ongLohsIBfTovMeYl\nsQDAXH0txl+h8qKmiYBBcyId+uQVKkBVtlQAgOIUDgCgOIUDAChO4YD+pD4l9rHqKYCuKBzQnzMS\nYzdWTwF0ReGA/pyZGLulegqgKwoH9CdVOG6ungIAGLTbYvxNv85qmggYPG/0A/1JvenX5sw4wFzY\nUgEilA2gMIUDAChO4QAAilM4AIDiFA4AoDiFAwAoTuEAAIpTOKAvRyXGfHAbUJzCAX1JfVLsf1RP\nAXRH4YC+pArHzuopgO4oHNAXhQNoQuGAvthSAZpQOKAvrnAATSgc0BeFA2hC4YC+nJwYu6d6CqA7\nCgf0ZXti7JHqKYDuKBzQF4UDaELhgL5sS4wpHEBxCgf0xRUOAKC4AxGxMnLb0jQR0IVNrQMAVa0k\nxvweAIqzpQIAFKdwAADFKRwAQHEKBwBQnMIBABSncAAAxSkcAEBxCgcAUJzCAQAUp3AAAMUpHABA\ncQoHAFCcwgEAFKdwAADFKRwAQHEKBwBQnMIBABSncAAAxSkcAEBxCgcAUJzCAQAUp3AAAMUpHABA\ncQoHAFCcwgEAFKdwAADFKRwAQHEKBwBQnMIB/Tg8MfZ49RRAlxQO6MexibE91VMAXVI4oB9PTYz9\nd/UUQJcUDujH8Ymx3dVTAF1SOKAfJyTGFA6gCoUD+uEKB9CMwgH9UDiAZhQO6IfCATSjcEA/FA6g\nGYUD+qFwAM0oHNAPr1IBmlE4oB/HJcZ2VU8BdEnhgH6kCscD1VMAAIP2cESsjNyObJoI6Mam1gGA\nalYSY34HAFXYUgEAilM4AIDiFA4AoDiFAwAoTuEAAIpTOACA4hQOAKA4hQMAKE7hAACKUzgAgOIU\nDgCgOIUD+pD6kLbHqqcAuqVwQB9OTIzdVz0F0C2FA/qgcABNKRzQB4UDaErhgD6clBhTOIBqFA7o\nw77E2F3VUwAAg7cycnta2zgAwBC9LP6vbLyqcRYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nABr7X8zKB9O35nSzAAAAAElFTkSuQmCC\n",
		"isbrushposition": 1,
		"disporder": 9,
		"longitude": 116.338409
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#手机合并审批，确认人
num5 = workticketid+1
num6 = workticketid+2
ts = tsi+1
#url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000006904",
		"latitude": 39.982727,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 0,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 11,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "iVBORw0KGgoAAAANSUhEUgAAAhwAAAGhCAYAAAAqQm1KAAAAAXNSR0IArs4c6QAAAARzQklUCAgI\nCHwIZIgAABJeSURBVHic7d1pzG1leQbg+3AYLFoEjrHFKq1KneuAlUEsOFRD6hAbo5VJi0i00Ggt\nbWmcUmNtjFONdYjElBrbmqhpqdaKViuIE2q1Ris4IFQbtVIEBEHG0x+HUz7Pevd3vmHv9ay91nUl\n+88L59v3ft+d9Txr2GslAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADBv21e8nlWcBQAYofPysw3H9tI0MCFbqgMA9KjV\nYNgOQg/2qA4A0JO9qwMAAOP3tnRPp3ylNBEAMDq7Nhvbkzy8NBEAbMCnk3wvyRHVQei4Q9oNBwAs\nlV0L2eG1cdjFx9Jdo2+XJgKAdXp8usXssspAdLSObtytNBEArFOrmJ1TmoiVTorTKQAsuQPTLmZ+\ncj4crfV5fWkiAFinS9ItZj8pTcRK94ijGwCMQKuYPaA0ESv9ON31+W5pIgBYp6Nj73noWutzYGki\nAFinH8TFokP2gWgIARiBVjH7udJErNRanyeXJgKAdXpQ7D0P2SmxPgCMwIXpFrNzSxOxUqvZOKs0\nEQBsQKugHVSaiJ1m3RsFAJbKvlHQhuw76a7NFaWJAGAD/jrdgnZpaSJWajWDv1CaCAA2oFXQHl0Z\niP/36jj6BMBIKGjD1VqbF5UmAoANODPdgnZDaSJ2OiSaQQBG4tZ0C9rzShOx0/+muzZfLU0EABtk\nD3q4WmuzX2kiANiAp0bDMVRvirUBYCRah+zfUJqInVrNxumliQBgg1pFbWtpIpLkmDi6AcBI3D+K\n2lDdku66fKI0EQBs0GfSLWofLE1EkuyZdiO4Z2UoANioVlHbVpqIJPlyuutyS2kiANggD2sbrta6\nHFOaCAA2yMPahumN0QgCMCKtonZ0aSKS9rq8rDQRAGyCvejheXqsCwAj8op0i9p1pYlI2s3GuaWJ\nAGATWoXtWaWJuE8c3QBgZBS24bkp3TX5YWkiANiE06LhGJoD0l6Tn68MBQCbcXO6he1PShPxo3TX\n5IbSRACwSY5uDMus25jfpzIUAGzGSdFwDM1lsSYAjMwN6Ra2V5UmmrYtaTcbj6kMBQCbZU96WL4a\nawLAyBwXxW1oWuvxxNJEALBJN6Zb3F5fmmjaPhYNIAAjpLgNS2s9nl6aCAA2ya9ThsXRDQBGqXU6\n5bWliaat1WycWJoIAObA3vRwnB/rAcAInRoFbkhaa3F8aSIAmIPWs1NeWZpoui6M5g+AkVLghqO1\nFseVJgKAOXhhNBxD8R+xFgCMVKvAnVGaaJr2SHstnloZCgDmxR71MFwSawHASL0iitwQbE17HY6u\nDAUA89IqcieXJpqmH0TjB8BIzdqrpl93THsdHlIZCgDm5ex0i9w1pYmm6dpo/AAYsVaRe1xpoum5\ne9rrcM/KUAAwL/vHXvUQ3JLuGlxfmggA5uiT6Ra6S0oTTc+vpd30HVgZCgDmyWH8eq01uKI0EbAQ\ne1YHgCKPnDF+aa8ppu2JM8a3rfHfH5Lk2dlxDchBSS5P8p9JvpTkw5tOBwBzcGW6e9bvK000Pa2j\nGxfv5t+8fMa/m/U6J07PAFCoVZz2Kk00LS/K2i/Y/eXs+KnyehqN1utDSfZZyKcBgIbfj1+nVGvN\n/8d3+X9OnfH/zeP1ewv7ZABwm1YBemlpoml5c1Zv+J40478v4nXBwj4lAJO2VxzdqNaa/7OT3GPG\nf1vt9bkkZyR5cpITkrx6A39je5JvL/QTAzA570+32Fxbmmhazk274F82Y7z1ev4a3+tRSb6wjr+7\nPcmnN/fxAGCHVpE5qjTRtGz01MdXNvm+d86Ooxhrfb8TN/l+AEzY4XE6pdLFWX+jcc4Ccpy1xve+\nOsmWBbw/ACPXeiLpv5Qmmo6tWV+jcVEPmZ63xiz37SELACPSKibuvdGP72Ztxf3m7Dj90afj15Dr\nj3vOBMCSek2cTqlyh6yt2TipKuBt3pXV8/1NWTIAlkargJxSmmg6fpzVC/kX6qJ17J/Vs55XlgyA\nwTsojm5U2d1RjXvVRVvVtzI78/mFuQAYsMvSLRqfrww0Eas1Gp8ozLVWs+6Iuj3JPxfmAmCgWgVj\n39JE47das/GYwlzr9YLM/hwvLswFwMCcHqdT+vb1rP4rlGVzYmZ/nl8vzAXAgLSKxAtKE43brF8D\n7XwdVBdtU1Y7vbJ3YS4ABmCfOLrRp8dm9xeJLrOPZJyfC4BN+kS6heGyykAjdkB232wcWpZufmb9\neuXCylAA1BrTIf2h212zMaajALPuK+J6DoAJekLGXfSG5Orsvtl4elm6xRh7UwXAGl2fbjF4fWmi\n8ZrS0Y2dnpH253R/DoCJmULRG4rdNRtn1EVbqCvS/rweCAgwES9MtwjcWppo/FpHlKbQ6LU+75Wl\niQDoTasIPKc00TS05v2DpYkW75lpf+57V4aCIdpSHQAWoLVX7bu+WHsmuakxvkemcZSjxXcOVtij\nOgDM2RsbY1f1nmJ6zmuM3ZzxNxtJcs8Z48f3mgKAXrUObz+yNNE0TH3eZ11ACsAIbYmNfoWTY963\npj0Hr6kMBcBivDXdDf53ShNNw63pzvubShPV+FQ0XgCT0NrYP6I00TQosrdrzcXflyYCYK5mHdJm\nsV4a875S6yjblOcDYHScTqnRKq6nlyaq15qT80sTATA3rY38w0sTjZ+LdNvOjHkBGC0b+P69JeZ9\nlta8fKs0EQCb9mfpbtyvrgw0Ea2i+qTSRMNxXNrz4+6jAEustWF/WmmiaXB0Y3Wt+fl8aSIANkXh\n69+z051zT+T9WU+O7ybAaJwWG/UK16U752eWJhqm1nfznNJEAGzIzgeErXydUZpoGjR5a3NqzBXA\nKNiY9++QmPf1aM3V20oTAbAuj4vCV+E96c75P5QmGraXxfcUYKl9L92N+DtKE01Dq3geUppo+Fpz\n9rzSRACsWWsjvndpommwt75+bpIGsKS2xQa8wm/EvG9Ua962lSYCYLc+kO7G+zOliabhgnTn/U2l\niZbH99Odu++XJgJgt1p7iw8sTTQNrXm/Y2mi5fGLcXQIYKl4Smkd8745rfl7Q2kiAGZ6ZbobbQ9r\nW7z7RcOxWR5dD7BEWhvs40oTTcNZ6c7735UmWk6t7++DSxMB0GQPscYt6c77w0sTLadvpjuP3ylN\nBEDHU6LhqGLe5+OAmEuAwbs83Q3160oTTYciOT+tuTy2NBEAP6O1od5ammgajkp33q8sTbTc3hvz\nCTBYd4m97CpvS3fe/6o00XLbK77LAIPV2iv8VGmi6fhJunN/ZGmi5ddqOPYvTQRAkvYG+qGliabD\n3vj8fSndOT27NBEASRS9SuZ+/o6JeQUYnGeku2G+oTTRtCiMi2FeAQbmknQ3zKeXJpqOQ9Od+2tK\nE41Hq+HYqzQRwMTZE6zzknTn/m9LE43HxdFIAwyKhqPOJ9Od+xNKE43H89Od2y+WJgKYsGenu1H+\nWmmiaWk1eweWJhqP/aKZBhiMr6W7QT6xNNG0KIiLZX6ZhC3VAWANWhtg393+mP/FMr9Mwh7VAQCA\n8dNwMHQPaozd1HuK6Tq0Mfaj3lOM242NsTv3ngIWTMPB0J3WGDur9xTTdVRj7F97TzFurQug7997\nClgwDQdD99zG2Ft6TzFdhzXGPtt7inG7qDF2v95TwIJpOBi61l0XWxtoFuPwxpiGY77+qzG2X+8p\nYME0HMBqfrUxdmHvKcat9SuVPXtPAQum4WDIWhcsXt97CnblPhHzpeFgEjQcDFnr+o139J4CFusO\njTENB0CPbkz3DowPK000Pe6CuXjvj2fVAJRS7OpZg8W7KBprgFKKXa1fSXf+/6cy0Ejdmu48t36d\nBUvNNRwM1b7VAchDG2N+Ejt/reemuJsuo6PhYKhOaYx9pPcU09a62+XFvacARkHDwVC1Hj//rt5T\nTNt9G2NuugbAqLSu39Ag9+uz6a7BEaWJxufl6c7x+aWJACbGBaP1rkp3DfYvTTQ+N6c7x48rTQQL\n0rpYCYag1WD4vvbLGiyeOWYyHKJmiB7cGLuu9xSwWK0H48FoaTgYomc2xt7dewpYrH9qjP1l7ykA\nJuwb6Z7XfnxpomlyHc1imV+AYjbEw2AdFueEmF+AcjbEw2AdFqc1t39emggWzNXQDJEr94fBOizG\nPkl+2hg3t4yai0YZmns3xm7oPQUszhcaY1f0ngJg4v4w3UPN7ylNNF1OqSxGa14PLk0EMEEfT3dj\n3HquCoun4Zi/98W8AgxCa2O8rTTRdCmM89ea0+eWJgKYKEVuOKzFfL0z5hRgMGyQh8NazFdrPt9a\nmghgwhS54bAW8/PvMZ8Ag/HAdDfIfi5Y5/J01+Og0kTLaWvazcbrKkNB39yHgyF5QmPsw72nYKdL\nGmOt+6Swuh/OGP+jXlNAMQ0HQ9J6QNtHe0/BTt9qjGk41ueuSQ5sjD+n7yAA3O7muCHSkLw43fV4\ne2mi5dP6Trt2A6CYDfOwHJnueny9NNFyeWza3+lDK0NBFQ8LYkhaDYbvaJ0tSW6dMc7utb7PtyTZ\ns+8gMASu4QBmcYRp4y6bMX63PkMA0OaUyvBYk/U7Ku15+1xlKAB2ODjdDfTlpYlINBwb0Zoz88bk\nOaXCUBzeGPt07ynY1fWNsXv0nmJ5fHPG+AN6TQEDpOFgKFpX7n+p9xTs6iONsaf2nmI5PCLJIY3x\nLye5qOcsAMxwbrqHoH+7NBFJ8rvprsu/VQYaMKdSAJbAD9LdUN+rNBFJcqcoomtxZdrz9JDKUAB0\nKWrDZW1W97K056h1a3gAiilqw2VtZts/TqUALBUb7OFqrc3W0kTDMavZuHtlKABm03AM1xfTXZun\nlSYahq+m/b19a2UoAFan4Riul6S7Nu8uTVTvt9L+zrbuWwLAgGg4huu+6a7NT0sT1dojrtsAWFq7\nbrivrY3DLhTX292S9nwcVhkKgLXZdeN9fG0cdqHh2OGDac/FBZWhAFifDyX5cZKjq4PQoeFIHhin\nUgBgoS5Ot8g+qTRR/zQbsAke3gasxfsaYyf1nqLONTPGT+41BQCMXOuXKlPZu39V2p/90spQADBW\nU2w4DoxTKQDQqykW3VnNxl0qQwHAmF2XbuE9tjTRYl2VdrPx2spQADB2f5Fu8f1caaLFeXPazYYb\n0gHAgt0x0zitcmRctwEApVpFeEyPqt8vs5uNuxbmAoBJuTbdQvzO0kTzNavZ+NPKUAAwNcdmvKca\nZjUb36gMBQBT1SrKTylNtHk3pf25floZCgCm7KMZ11GOK+MiUQAYnC1pF+cHVIbaoKszu9nYuzAX\nAJDkJ+kW6FtLE63fjZndbGwrzAUA3ObgtAv1YZWh1mFWo7E9yT0LcwEAu7g+y3fdw52yerPx4Lpo\nAEDLtrSL9vcqQ63iYVm92Ti4LhoAsJqL0i7eF1SGanhvVm829q+LBgCsxawi/rHKUCvMOvWzDKeA\nAIDbzLqAtPrGWSevkmt7khvqogEAG/GSrF7cn9Zjln3SfubLytdFPeYBAObohKxe5K/vIcN5u8mw\nPcnze8gBACzQo7P7gv+hBbzveWt43+1J9l3AewMARdZS/N+zyfe4W5IfrvG9/nGT7wUADNTbs7Zm\n4L+T/NI6/u6r1vh3d74O2PxHAQCG7rqsvTm4PMlZSU7NjruCHpHkD5J8Yx1/Y+frOX18OABgOI7J\n+huGjb5e2dNnAgAG6pQsrtE4rcfPAQAsgcdnfo3Gb/acHQBYMndKcnbW32ScWREW2Lgt1QEAVrh/\nkkclOSrJ7yS5NMnXknw5yRuTXFMXDQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgDH5P7U+GKxvnU5cAAAAAElFTkSuQmCC\n",
			"uuid": ""
		}],
		"name": "确认人",
		"audittype": "sign,card",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 11,
		"longitude": 116.338456
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#手机合并审批，批准人
num5 = workticketid+1
num6 = workticketid+2
ts = tsi+1
#url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid"%(num5,num6,num2)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000006908",
		"latitude": 39.982727,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 24,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\nAKCr/wN5Iq4FvaO17QAAAABJRU5ErkJggg==\n",
			"uuid": ""
		}],
		"name": "批准人",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\nAKCr/wN5Iq4FvaO17QAAAABJRU5ErkJggg==\n",
		"isbrushposition": 1,
		"disporder": 24,
		"longitude": 116.338456
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']