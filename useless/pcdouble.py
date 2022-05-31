__author__ = 'David'
#time 2020-6-2 10:40 PC端主流程-双票
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
import datetime
import json
import configparser
import sys

#from globalpkg.mydb import MyDB
#from globalpkg.log import logger
from globalpkg.global_var import *
#from globalpkg.global_function import run_testcase_by_id
#from globalpkg.global_function import get_http_conf_of_project

#from config.runmodeconfig import RunModeConfig
#from testsuite import TestSuite
#from testplan import TestPlan
#from testproject import TestProject
from htmlreporter import HtmlReport
from globalpkg.global_var import executed_history_id
from sendmail import MyMail


#临时cookies
cookies={'JSESSIONID': 'DB7520665A4F144E5FE0AFE8A3DBEF19Xrovjn'}
logger.info("-----------------------------------------------------------------------------------------------------------------------------------")
logger.info("-----------------------------------------------------------------------------------------------------------------------------------")
logger.info("-----------------------------------------------------------------------------------------------------------------------------------")
logger.info("-----------------------------------------------auto_run_start----------------------------------------------------------------------")
logger.info("-----------------------------------------------------------------------------------------------------------------------------------")
logger.info("-----------------------------------------------------------------------------------------------------------------------------------")
logger.info("-----------------------------------------------------------------------------------------------------------------------------------")
#作业预约作业任务名称随机数生成函数
def ranstr(num):
    salt = ''.join(random.sample(string.ascii_letters+string.digits,num))
    return  salt
name = "Created_by_Python_"+ranstr(6)
print("作业预约名称",name)
logger.info("作业预约名称%s",name)
#获取当前时间，为作业预约提供时间变量
now = datetime.datetime.now()
now1 = now + datetime.timedelta(minutes=5)
now2 = now + datetime.timedelta(minutes=10)
fnow1 = now1.strftime("%Y-%m-%d %H:%M:%S")
fnow2 = now2.strftime("%Y-%m-%d %H:%M:%S")
now =now.strftime("%Y-%m-%d %H:%M:%S")


#用例信息变量定义
testsuit = []
caseinfo = {}

caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ''

# 记录测试开始时间
start_time = datetime.datetime.now()

create_testcase_reporter_tb_sql = 'CREATE TABLE IF NOT EXISTS ' + testcase_report_tb + '\
                                         (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,\
                                          executed_history_id varchar(50) NOT NULL,\
                                          testcase_id int NOT NULL,\
                                          testcase_name varchar(40) NOT NULL,\
                                          testsuit varchar(40),\
                                          testplan varchar(40),\
                                          project varchar(40),\
                                          runresult varchar(20),\
                                          runtime datetime,\
                                          case_exec_history_id varchar(50), \
                                          tc_external_id varchar(50))'
create_case_step_reporter_tb_sql = 'CREATE TABLE IF NOT EXISTS ' + case_step_report_tb + '\
                                         (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,\
                                          executed_history_id varchar(50) NOT NULL,\
                                          testcase_id int NOT NULL,\
                                          testcase_name varchar(40) NOT NULL,\
                                          testplan varchar(40) NOT NULL,\
                                          project varchar(40) NOT NULL,\
                                          step_id int,\
                                          step_num int NOT NULL,\
                                          step_action varchar(1000), \
                                          expected_results varchar(1000),\
                                          runresult varchar(10),\
                                          reason varchar(2000),\
                                          protocol_method varchar(40) ,\
                                          protocol varchar(40),\
                                          host varchar(40),\
                                          port int,\
                                          runtime datetime)'

logger.info('正在创建测试用例报告报表')
testdb.execute_create(create_testcase_reporter_tb_sql)

logger.info('正在创建测试步骤报告报表')
testdb.execute_create(create_case_step_reporter_tb_sql)


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



#预约列表用例信息
caseid = 1
casename = '预约列表接口获取'
count =1

caseinfo['id'] = caseid
caseinfo['name'] = casename

#预约列表接口地址
url1 = 'http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/getMetaData?0.3897117454385264&contentType=json&ajax=true&tid=1'
url1 = 'http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/getMetaData?0.3897117454385264&contentType=json&ajax=true&tid=1'
#请求头
headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'csrf': '6363382b59f6435eb243fab57ea5a5e0',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Content-Type': 'text/plain',
    }
logger.info('正在执行测试用例==ID=%d,name=%s',caseid,casename)
#请求接口
rs=requests.get(url1, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)


#获取接口返回状态
status= data['status']

if status == 3200:

    #print("获取列表成功", status)
    caseinfo['result'] = "Pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", casename,data)
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
print("作业预约新增ID:",num)
logger.info("作业预约新增ID:%s",num)
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
logger.info('正在执行测试用例==ID=%d,name=%s',caseid,casename)
#请求作业预约保存接口
rs=requests.post(url2, json = formdatanew, headers = headers,cookies=cookies)
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
    #print("作业预约成功", sta)
    caseinfo['result'] = "Pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", casename, data)
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

    #print("获取列表成功", status)
    caseinfo['result'] = "Pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("送交结果,运行状态%s", data)
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

    #print("获取列表成功", status)
    caseinfo['result'] = "Pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("审批结果%s", data)
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

    #print("获取列表成功", status)
    caseinfo['result'] = "Pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", casename, data)
#收集用例执行信息
testsuit.append(caseinfo.copy())
#获取worktaskid
data = data['data']['data']['worktaskid']
print("安全分析和交底_worktaskid",data)
logger.info("安全分析和交底_worktaskid:%ss",data)
worktaskid = data
#安全步骤URL请求ID
num1 = worktaskid
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

    #print("获取列表成功", status)
    caseinfo['result'] = "Pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", casename, data)
#收集用例执行信息
testsuit.append(caseinfo.copy())
#print (sta)
a = data['data']["voset"]["voList"]
b =[]
for i in range(len(a)):

    if a[i]['worktaskid'] !="" and a[i]['worktaskid'] !="None":
        b.append(a[i]['worktaskid'])
#print (b)

#print ("安全分析列表使用ID:",num1)

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

    #print("获取列表成功", status)
    caseinfo['result'] = "Pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", casename, data)
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
#print("num1:",num1)
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

    #print("获取列表成功", status)
    caseinfo['result'] = "Pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", casename, data)
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
print ("送交ID:",num1)
logger.info("送交ID:%s",num1)
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
'''
data = {
	"tableName": "hse_safety_disclosure",
	"additional_content": null,
	"confirm_content": "1、已清楚作业区域及周边生产作业情况\r\n2、已清楚本次作业的安全风险（JSA）\r\n3、已清楚本次作业的具体安全要求（作业许可证中的控制措施）\r\n4、已对本次作业现场安全措施进行了检查确认\r\n5、已清楚本次作业涉及的作业许可证的有限期限 \r\n6、已掌握个人防护用具正确佩戴使用方法\r\n7、已清楚突发情况下的应急避险方法",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": "2020-06-02 09:56:33",
	"updated_by": 1000,
	"updated_dt": "2020-06-02 09:56:33",
	"df": 0,
	"tenantid": 1,
	"ts": null,
	"safeclarid": 2000000002001,
	"projecttype": null,
	"safe_name": "自动化测试用不要删除",
	"worktype": "aqjd",
	"workstatus": "draft",
	"scopeandenv": null,
	"workrisk": null,
	"preventmeasure": null,
	"emermeasure": null,
	"othermatter": null,
	"safe_content": null,
	"safe_clar_temp_id": 2000000001050,
	"safe_clar_temp_name": null,
	"worktaskid": 2000000001984,
	"work_position_id": 2000000002019
}
'''
#请求接口
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    #print("获取列表成功", status)
    caseinfo['result'] = "Pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("安全交底错误信息%s",data)
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

    #print("获取列表成功", status)
    caseinfo['result'] = "Pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("安全提交错误信息%s", data)
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
	"jsaid": 2000000001860,
	"work_appoint_id": 2000000001860,
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
#请求接口
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    #print("获取列表成功", status)
    caseinfo['result'] = "Pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", casename, data)
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

    #print("获取列表成功", status)
    caseinfo['result'] = "Pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", casename, data)
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
print("作业任务列表ID:",num2)
logger.info("作业任务列表ID:%s",num2)
#作业任务提交
#作业任务提交接口用例信息

casename = '作业任务提交'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename
##作业任务提交URL,使用作业任务列表IDnum2
url =  'http://192.168.6.27:6030/hse/HSE_WORK_TASK_MCQ/hse_work_task_submit?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=%d&0.7819922897402813&contentType=json&ajax=true&tid=1'%(num2,num2)
#url1= 'http://192.168.6.27:6030/hse/HSE_WORK_TICKET_XKZ/cardSave?parentEntityId=2000000004176&parentFuncCode=HSE_WORK_TASK_MCQ&topEntityId=2000000004176&topFuncCode=HSE_WORK_TASK_MCQ&dataId=2000000005557&ts=1590655157270&0.9150744998075542&contentType=json&ajax=true&tid=1'
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

    #print("获取列表成功", status)
    caseinfo['result'] = "Pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", casename, data)
#收集用例执行信息
testsuit.append(caseinfo.copy())

#作业许可证保存
#作业票ID
num3 = 2000000005657+2
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TICKET_XKZ/cardSave?parentEntityId=%d&parentFuncCode=HSE_WORK_TASK_MCQ&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=%d&ts=1590652813735&0.27372678355625824&contentType=json&ajax=true&tid=1'%(num2,num2,num3)
#url = 'http://192.168.6.27:6030/hse/HSE_WORK_TICKET_XKZ/cardSave?parentEntityId=%d&parentFuncCode=HSE_WORK_TASK_MCQ&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=2000000005573&ts=1590656443277&0.7178753893110355&contentType=json&ajax=true&tid=1'%(num2,num2)
#print(url)
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
	"worker": "9",
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
#请求接口
'''
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
rs.encoding='utf-8'
cc = str(rs.content, 'utf8')
print ("作业许可证保存",cc)
'''
#作业许可证提交
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TICKET_XKZ/hse_work_ticket_submit?parentEntityId=%d&parentFuncCode=HSE_WORK_TASK_MCQ&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=%d&ts=1590653538571&0.23372369575241692&contentType=json&ajax=true&tid=1'%(num2,num2,num3)
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
	"ts": 1590653538571,
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
#rs=requests.post(url, json = data, headers = headers,cookies=cookies)
#rs.encoding='utf-8'
#cc = str(rs.content, 'utf8')
#print (cc)
#driver.close()
#driver.quit()
logger.info('正在初始化数据库[名称：TESTDB]对象')
testdb = MyDB('./config/dbconfig.conf', 'TESTDB')
#用例执行
for i in range(len(testsuit)):
    # 构造测试步骤对象
    step_id = 1
    step_number = 1
    step_action = ''
    testcase_name = testsuit[i]['name']
    testcase_steps = 1
    testcase_isactive = 1
    testsuite_id = 1
    testsuite_name = "作业许可"
    testplan = "plan1"
    project_name = "changqing"
    testcase_id = testsuit[i]['id']
    testproject = 'changqing'
    preconditions = ''
    host = "192.168.6.27"
    port = "6030"
    #case_executed_history_id = "20200602083321"
    case_executed_history_id = time.strftime('%Y%m%d%H%M%S', time.localtime())
    expected_results = ""
    tc_external_id = 1
    sql_insert = 'INSERT INTO ' + case_step_report_tb + '(executed_history_id, testcase_id, testcase_name, testplan, project, step_id, step_num, protocol_method, protocol, host, port, ' \
														'step_action, expected_results, runresult, reason, runtime)' \
														' VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    data = (case_executed_history_id, testcase_id, testcase_name, testplan, testproject, step_id,
				step_number, '无', 'http', host, port,
				step_action, expected_results, 'Unexecuted', '', '0000-00-00 00:00:00')
    logger.info('记录测试步骤到测试步骤报告表')
    testdb.execute_insert(sql_insert, data)


    fail_or_error_reason = ''
    protocol_method = "Post"
    #run_time =""
    run_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # 记录运行时间
    #logger.info("===================运行时间===========================")
    #print(run_time)
    action_of_step=""
    if testsuit[i]['result'] == "Pass":
        result_of_step ="Pass"
    else:
        result_of_step = "Fail"
    sql_update = 'UPDATE ' + case_step_report_tb + ' SET runresult=\"%s\",reason=\"%s\", protocol_method=\"%s\", runtime=\"%s\",' \
														   'step_action=\"%s\", expected_results=\"%s\"' \
														   ' WHERE executed_history_id = %s AND testcase_id = %s AND step_id = %s' \
														   ' AND project=\'%s\' AND testplan=\'%s\'  AND runtime=\'%s\''
    data = ("pass", fail_or_error_reason, protocol_method, run_time, action_of_step, result_of_step,
					str(case_executed_history_id), testcase_id, step_id,
					testproject, testplan, '0000-00-00 00:00:00')
    logger.info('正在更新步骤执行结果')
    testdb.execute_update(sql_update, data)

    logger.info('测试用例[id=%s, name=%s]执行成功' % (testcase_id, testcase_name))
#结果处理
for i in range(len(testsuit)):
    #print(testsuit[i])
    # 构造测试用例对象
    testcase_name = testsuit[i]['name']
    testcase_steps = 1
    testcase_isactive = 1
    testsuite_id = 1
    testsuite_name= "作业许可"
    testplan =  "plan1"
    project_name = "changqing"
    testcase_id = testsuit[i]['id']
    preconditions =''
    tc_external_id = 1
    #executed_history_id = "20200602083913"
    #executed_history_id = time.strftime('%Y%m%d%H%M%S', time.localtime())
	#testcase_obj = TestCase(testcase_id, testcase_name, testcase_steps, testcase_isactive, project_name, testsuite_id, tc_external_id, preconditions)
    try:
        sql_insert = 'INSERT INTO ' + testcase_report_tb + '(executed_history_id, testcase_id, testcase_name, testsuit, testplan, project, runresult, runtime, tc_external_id)' \
														   ' VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        data = (executed_history_id, testcase_id, testcase_name, testsuite_name, testplan, project_name, 'Unexecuted',
				'0000-00-00 00:00:00', tc_external_id)
        logger.info('记录测试用例到测试用例报表')
        testdb.execute_insert(sql_insert, data)

        #logger.info('开始执行测试用例[id=%s，name=%s]' % (testcase_id, testcase_name))
        run_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # 记录运行时间
        case_executed_history_id = time.strftime('%Y%m%d%H%M%S', time.localtime())  # 流水记录编号
        if testsuit[i]['result'] == "Pass":
            testcase_run_result = "Pass"
        else:
            testcase_run_result = "Fail"
        #testcase_run_result = testsuit[i]['result']

        logger.info('正在更新用例执行结果')
        sql_update = 'UPDATE ' + testcase_report_tb + ' SET runresult=\"%s\", runtime=\"%s\",' \
                                             ' case_exec_history_id=\"%s\"' \
                                             ' WHERE executed_history_id = %s and testcase_id = %s' \
                                              ' AND project=\'%s\' AND testplan=\'%s\''
        data = (testcase_run_result, run_time, str(case_executed_history_id), executed_history_id, testcase_id, project_name,
        testplan)
        testdb.execute_update(sql_update, data)
    except Exception as e:
        logger.error('运行用例出错 %s' % e)

logger.info('接口测试已执行完成，正在关闭数据库连接')
testdb.close()
# 记录测试结束时间
end_time = datetime.datetime.now()
# 构造测试报告
html_report = HtmlReport('test report', 'ushayden_interface_autotest_report')
html_report.set_time_took(str(end_time - start_time))  # 计算测试消耗时间

# 读取测试报告路径及文件名
config = configparser.ConfigParser()
config.read('./config/report.conf', encoding='utf-8')
dir_of_report = config['REPORT']['dir_of_report']
report_name = config['REPORT']['report_name']

# 设置报告生成路
html_report.mkdir_of_report(dir_of_report)

# 生成测试报告
html_report.generate_html(report_name)

logger.info('生成测试报告成功')

mymail = MyMail('./config/mail.conf')
mymail.connect()
mymail.login()
mail_content = 'Hi，附件为接口测试报告，烦请查阅'
mail_tiltle = '【测试报告】接口测试报告' + str(executed_history_id)
logger.info(html_report.get_filename())
attachments = set([html_report.get_filename()])

logger.info('正在发送测试报告邮件...')
mymail.send_mail(mail_tiltle, mail_content, attachments)
mymail.quit()

logger.info('发送邮件成功')
logger.info("-----------------------------------------------END----------------------------------------------------------------------")