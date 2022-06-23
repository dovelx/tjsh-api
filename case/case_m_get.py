
from tools import tool



case = '天津石化APP-首页接口'

#times
starttime = tool.starttime
endtime = tool.endtime
now = tool.now

#作业任务名称
name = tool.ran_name_with_str()
#print("作业任务名称：",name)

#用例信息变量定义
testsuitmg = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['exresult'] = ''
caseinfo['isactive'] = ''

count =0
#用例信息
caseinfo['id'] = 1
caseinfo['name'] = 'index-/m/pub-base_m/a/getConfigs'
caseinfo['isactive'] = 1
#拼写预约URL
#https://tjsh.ushayden.com/m/pub-base_m/a/getConfigs.json
url = '/m/pub-base_m/a/getConfigs.json'
host='https://tjsh.ushayden.com'
caseinfo['url'] = host+url
#动火作业
data = {}
caseinfo['data'] =data
testsuitmg.append(caseinfo.copy())

caseinfo['id'] = 2
caseinfo['name'] = 'index-/m/hse_m/HSE_WORK_TICKET_M/project_implementation_allowAccess'
caseinfo['isactive'] = 1
#拼写预约URL
#https://tjsh.ushayden.com/m/pub-base_m/a/getConfigs.json
url = '/m/hse_m/HSE_WORK_TICKET_M/project_implementation_allowAccess.json'
host='https://tjsh.ushayden.com'
caseinfo['url'] = host+url
#动火作业
data = {}
caseinfo['data'] =data
testsuitmg.append(caseinfo.copy())

caseinfo['id'] = 3
caseinfo['name'] = 'index-/m/hse_m/HSE_WORK_TICKET_M/job_implementation_allowAccess'
caseinfo['isactive'] = 1
#拼写预约URL
#https://tjsh.ushayden.com/m/pub-base_m/a/getConfigs.json
url = '/m/hse_m/HSE_WORK_TICKET_M/job_implementation_allowAccess.json'
host='https://tjsh.ushayden.com'
caseinfo['url'] = host+url
#动火作业
data = {}
caseinfo['data'] =data
testsuitmg.append(caseinfo.copy())

caseinfo['id'] = 4
caseinfo['name'] = 'index-/m/hse_m/HSE_WORK_TICKET_M/job_implementation_allowAccess'
caseinfo['isactive'] = 1
#拼写预约URL
#https://tjsh.ushayden.com/m/pub-base_m/a/getConfigs.json
url = '/m/hse_m/HSE_WORK_TICKET_M/job_implementation_allowAccess.json'
host='https://tjsh.ushayden.com'
caseinfo['url'] = host+url
#动火作业
data = {}
caseinfo['data'] =data
testsuitmg.append(caseinfo.copy())


caseinfo['id'] = 5
caseinfo['name'] = 'hse-m-sgzypsp-/m/hse_m/HSE_WORK_TICKET_GB_SGZY_SCENE_CONFIRM_M/getMetaData'
caseinfo['isactive'] = 1
#拼写预约URL
#https://tjsh.ushayden.com/m/pub-base_m/a/getConfigs.json
url = '/m/hse_m/HSE_WORK_TICKET_GB_SGZY_SCENE_CONFIRM_M/getMetaData.json'
host='https://tjsh.ushayden.com'
caseinfo['url'] = host+url
#动火作业
data = {}
caseinfo['data'] =data
testsuitmg.append(caseinfo.copy())

caseinfo['id'] = 6
caseinfo['name'] = 'hse-m-sgzypsp-/m/hse_m/HSE_WORK_TICKET_GB_SGZY_SCENE_CONFIRM_M/listQuery'
caseinfo['isactive'] = 1
#拼写预约URL
#https://tjsh.ushayden.com/m/pub-base_m/a/getConfigs.json
url = '/m/hse_m/HSE_WORK_TICKET_GB_SGZY_SCENE_CONFIRM_M/listQuery.json?queryType=2&level=2&page=1&rows=10&extWhere=Q6Zaz3EfE6%2FC2NWxVpwkp%2Bvrw83WKZUWxkmr%2FSNwA7I%3D'
host='https://tjsh.ushayden.com'
caseinfo['url'] = host+url
#动火作业
data = {}
caseinfo['data'] =data
testsuitmg.append(caseinfo.copy())

caseinfo['id'] = 7
caseinfo['name'] = 'hse-m-sgzypsp-/m/hse_m/HSE_WORK_TICKET_GB_SGZY_SCENE_CONFIRM_M/listQuery'
caseinfo['isactive'] = 1
#拼写预约URL
#https://tjsh.ushayden.com/m/pub-base_m/a/getConfigs.json
url = '/m/hse_m/HSE_WORK_TICKET_GB_SGZY_SCENE_CONFIRM_M/listQuery.json?queryType=2&level=2&page=1&rows=10&extWhere=Q6Zaz3EfE6%2FC2NWxVpwkp%2Bvrw83WKZUWxkmr%2FSNwA7I%3D'
host='https://tjsh.ushayden.com'
caseinfo['url'] = host+url
#动火作业
data = {}
caseinfo['data'] =data
testsuitmg.append(caseinfo.copy())

caseinfo['id'] = 8
caseinfo['name'] = 'gfx-pzcj-/m/hse_m/HSE_WORKAPPLY_GB_M/getMetaData.json'
caseinfo['isactive'] = 1
#拼写预约URL
#https://tjsh.ushayden.com/m/pub-base_m/a/getConfigs.json
url = '/m/hse_m/HSE_WORKAPPLY_GB_M/getMetaData.json'
host='https://tjsh.ushayden.com'
caseinfo['url'] = host+url
#动火作业
data = {}
caseinfo['data'] =data
testsuitmg.append(caseinfo.copy())

caseinfo['id'] = 9
caseinfo['name'] = 'gfx-pzcj-/m/hse_m/HSE_WORKAPPLY_GB_M/listQuery'
caseinfo['isactive'] = 1
#拼写预约URL
#https://tjsh.ushayden.com/m/pub-base_m/a/getConfigs.json
url = '/m/hse_m/HSE_WORKAPPLY_GB_M/listQuery.json?queryType=2&level=2&page=1&rows=10'
host='https://tjsh.ushayden.com'
caseinfo['url'] = host+url
#动火作业
data = {}
caseinfo['data'] =data
testsuitmg.append(caseinfo.copy())

caseinfo['id'] = 10
caseinfo['name'] = '高风险作业-pzcj-/m/hse_m/HSE_WORKAPPLY_GB_M/cardAdd'
caseinfo['isactive'] = 1
#拼写预约URL
#https://tjsh.ushayden.com/m/pub-base_m/a/getConfigs.json
url = '/m/hse_m/HSE_WORKAPPLY_GB_M/cardAdd.json'
host='https://tjsh.ushayden.com'
caseinfo['url'] = host+url
#动火作业
data = {}
caseinfo['data'] =data
testsuitmg.append(caseinfo.copy())

caseinfo['id'] = 10
caseinfo['name'] = '作业预约-/m/hse_m/HSE_WORK_TICKET_GB_SGZY_ADD_M/getMetaData.json'
caseinfo['isactive'] = 1
#拼写预约URL
#https://tjsh.ushayden.com/m/pub-base_m/a/getConfigs.json
url = '/m/hse_m/HSE_WORK_TICKET_GB_SGZY_ADD_M/getMetaData.json'
host='https://tjsh.ushayden.com'
caseinfo['url'] = host+url
#动火作业
data = {}
caseinfo['data'] =data
testsuitmg.append(caseinfo.copy())


caseinfo['id'] = 11
caseinfo['name'] = '现场确认-listQuery'
caseinfo['isactive'] = 1
#拼写预约URL
#https://tjsh.ushayden.com/m/hse_m/HSE_WORK_TICKET_GB_SGZY_M/listQuery.json?queryType=2&level=2&page=1&rows=10&queryParam=%7B%7D&extWhere=Q6Zaz3EfE6%2F5oXxRr29vzPBy2yiPTEll
url = '/m/hse_m/HSE_WORK_TICKET_GB_SGZY_M/listQuery.json?queryType=2&level=2&page=1&rows=10&queryParam=%7B%7D&extWhere=Q6Zaz3EfE6%2F5oXxRr29vzPBy2yiPTEll'
host='https://tjsh.ushayden.com'
caseinfo['url'] = host+url
#动火作业
data = {}
caseinfo['data'] =data
testsuitmg.append(caseinfo.copy())

# caseinfo['id'] = 12
# caseinfo['name'] = '作业处理-作业关闭'
# caseinfo['isactive'] = 1
# #拼写预约URL
# #https://tjsh.ushayden.com/m/hse_m/HSE_WORK_TICKET_GB_SGZY_M/listQuery.json?queryType=2&level=2&page=1&rows=10&queryParam=%7B%7D&extWhere=Q6Zaz3EfE6%2F5oXxRr29vzPBy2yiPTEll
# url = '/m/hse_m/HSE_WORKTASK_INJOB_M/closeTicketDisplay.json?workticketid=%d&workType=xkz&worklevel=low_risk&tabtype=close&auditfunccode=close'
# host='https://tjsh.ushayden.com'
# caseinfo['url'] = host+url
# #动火作业
# data = {}
# caseinfo['data'] =data
# testsuitmg.append(caseinfo.copy())