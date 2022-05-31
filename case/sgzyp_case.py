#from globalpkg.global_var import sql_query_jsa_step_harm_id
from tools import tool


case = '天津预发布环境-PC-施工作业票'

#times
starttime = tool.starttime
endtime = tool.endtime
now = tool.now

#作业任务名称
name = tool.ran_name_with_str()
print("施工作业名称：",name)

#用例信息变量定义
testsuit_sgzyp = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = ''
caseinfo['isactive'] = ''

count =0
host='https://tjsh.ushayden.com'
#用例信息
caseinfo['id'] = 1
caseinfo['name'] = '施工作业票保存'
caseinfo['isactive'] = 1
#拼写预约URL
#http://v3-test-linux-hse.hd-cloud.com/hse/HSE_WORK_TASK/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_WORK_TASK&0.19129330803343048&contentType=json&ajax=true&tid=2000000002503
url = '/hse/HSE_WORK_TICKET_GB_SGZY/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_WORK_TICKET_GB_SGZY&0.7809621619087208&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] = host+ url
#施工作业票草稿数据
data = {
	"tableName": "hse_work_ticket",
	"delaynum": "999",
	"applyunitname": "天津石化公司",
	"equipmentname": "",
	"worktype__name": "施工作业",
	"worktype": "xkz",
	"ishas_wtd": "0",
	"worktype_name": "施工作业票",
	"territorialunitid": "2000000008565",
	"istask": "1",
	"territorialunitname": "天津石化公司",
	"territorialunitcode": "0001",
	"applyunitid": "2000000008565",
	"ticketdealphoto": "0",
	"workstatus": "draft",
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": 0,
	"tenantid": 2000000002404,
	"ts": "",
	"tasktype": "",
	"projecttype": "repaire",
	"worklevel": "high_risk",
	"iscontractor": "0",
	"other_worktype": "xkz,dh,sx,mbcd,gc,dz,lsyd,dt,fcgzy",
	"hassafetyplan": "",
	"hasfacadecheck": "",
	"hasdrivermedical": "",
	"isgas_detection": "",
	"close_type": "",
	"lock_status": "",
	"hse_notice_id": 1000000131631,
	"notice_code": "030000939252",
	"workname": "name",
	"equipmentnumber": "weihao",
	"workunit": 2000000008565,
	"workunitname": "天津石化公司",
	"site": "location",
	"medium": "jiezhi",
	"temperature": "22",
	"pressure": "1024",
	"workcontent": "content",
	"planstarttime": starttime,
	"planendtime": endtime,
	"other_worktype_name": "施工作业票,动火作业,受限空间,盲板抽堵,高处作业,吊装作业,临时用电,动土作业,非常规作业"
}
caseinfo['data'] =data
testsuit_sgzyp.append(caseinfo.copy())

caseinfo['id'] = 2
caseinfo['name'] = 'JSA模板保存'
caseinfo['isactive'] = 1
#拼写URL
#http://v3-test-linux-hse.hd-cloud.com/hse/HSE_WORK_TASK/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_WORK_TASK&0.19129330803343048&contentType=json&ajax=true&tid=2000000002503
url = '/hse/HSE_JSA_TEMPLETE_NEW/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_JSA_TEMPLETE_NEW&0.5418943903112656&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] = host+ url
#JSA模板数据
data = {
	"tableName": "hse_jsa_templete",
	"temp_type": "aqfx",
	"isnew": "1",
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": 0,
	"tenantid": 2000000002404,
	"ts": "",
	"isenable": "1",
	"orgname": "天津石化公司",
	"orgid": 2000000008565,
	"temp_name": name
}
caseinfo['data'] =data
testsuit_sgzyp.append(caseinfo.copy())

caseinfo['id'] = 3
caseinfo['name'] = 'JSA步骤保存'
caseinfo['isactive'] = 1
#拼写URL
#http://v3-test-linux-hse.hd-cloud.com/hse/HSE_WORK_TASK/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_WORK_TASK&0.19129330803343048&contentType=json&ajax=true&tid=2000000002503
url = '/hse/HSE_JSA_TEMP_STEP_NEW/cardSave?parentEntityId=2000000000280&parentFuncCode=HSE_JSA_TEMPLETE_NEW&topEntityId=2000000000280&topFuncCode=HSE_JSA_TEMPLETE_NEW&0.9834370508103107&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] = host+ url
#JSA模板数据
data = {
	"tableName": "hse_jsa_temp_step",
	"jsa_templete_id": 2000000000280,
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": 0,
	"tenantid": 2000000002404,
	"ts": "",
	"worktype": "",
	"step_name": name,
	"step_code": "1"
}
caseinfo['data'] =data
testsuit_sgzyp.append(caseinfo.copy())