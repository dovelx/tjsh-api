#from globalpkg.global_var import sql_query_jsa_step_harm_id
from tools import tool
from globalpkg.global_var import worktaskid
from globalpkg.global_var import workticketid


case = '天津预发布环境-PC-盲板抽堵'

#times
starttime = tool.starttime
endtime = tool.endtime
now = tool.now
code = tool.ran_code_with_str()

#作业任务名称
name = tool.ran_name_with_str()
#print("施工作业名称：",name)

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
worktaskid = worktaskid + 1
dhworkticketid = workticketid + 4
sxticketid = workticketid + 5
lsydticketid = workticketid + 2
dtworkid = workticketid + 3
mbcdticketid = workticketid + 6
dzticketid = workticketid + 7
gcticketid = workticketid + 8
xkzticketid = workticketid + 1
#用例信息
caseinfo['id'] = 1
caseinfo['name'] = '盲板抽堵-add'
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
	"workname": name,
	"equipmentnumber": "weihao-data",
	"workunit": 2000000008565,
	"workunitname": "天津石化公司",
	"site": "api-didian",
	"medium": "介质",
	"temperature": "33",
	"pressure": "1024",
	"workcontent": "挖掘机",
	"planstarttime": starttime,
	"planendtime": endtime,
	"other_worktype_name": "施工作业票,动火作业,受限空间,盲板抽堵,高处作业,吊装作业,临时用电,动土作业,非常规作业"
}
caseinfo['data'] =data
testsuit_sgzyp.append(caseinfo.copy())




#用例信息
caseinfo['id'] = 2
caseinfo['name'] = '盲板管理-保存'
caseinfo['isactive'] = 1
#拼写预约URL
#http://v3-test-linux-hse.hd-cloud.com/hse/HSE_WORK_TASK/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_WORK_TASK&0.19129330803343048&contentType=json&ajax=true&tid=2000000002503
url = '/hse/HSE_TICKET_MBCD/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_TICKET_MBCD&0.2550397275279832&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] = host+ url
#
data = {
	"tableName": "hse_ticket_mbcd",
	"columnValues": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": "0",
	"tenantid": 2000000002404,
	"ts": "",
	"blind_type": "",
	"workstatus": "",
	"normalproductionstatus": "",
	"commenceperiodstatus": "",
	"downmaintenancestatus": "",
	"mbcdnumber": code,
	"territorialunitid": 2000000008565,
	"territorialunitname": "天津石化公司",
	"territorialunitcode": "0001",
	"medium": "油气",
	"temperature": "34",
	"pressure": "1024",
	"worksite": "未知"
}
caseinfo['data'] =data
testsuit_sgzyp.append(caseinfo.copy())