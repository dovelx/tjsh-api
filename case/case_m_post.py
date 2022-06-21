
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

