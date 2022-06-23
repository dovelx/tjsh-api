
from tools import tool



case = '天津石化PC-Get接口'

#times
starttime = tool.starttime
endtime = tool.endtime
now = tool.now

#作业任务名称
name = tool.ran_name_with_str()
#print("作业任务名称：",name)

#用例信息变量定义
testsuit = []
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
caseinfo['name'] = 'index-collect/PUB_TERRITORY_SHOW/workTaskTJSH'
caseinfo['isactive'] = 1
#拼写预约URL
#http://v3-test-linux-hse.hd-cloud.com/hse/HSE_WORK_TASK/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_WORK_TASK&0.19129330803343048&contentType=json&ajax=true&tid=2000000002503
url = '/collect/PUB_TERRITORY_SHOW/workTaskTJSH.json?tenantid=2000000002404&0.4004785328808982'
host='https://tjsh.ushayden.com'
caseinfo['url'] = host+url
#动火作业
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 2
caseinfo['name'] = 'index-sy/personal/getIndustry'
caseinfo['isactive'] = 1
#worktaskid=worktaskid+1
#http://v3-test-linux-hse.hd-cloud.com/hse/HSE_WORK_TASK/hse_work_task_submit?parentEntityId=&parentFuncCode=&topEntityId=2000100006956&topFuncCode=HSE_WORK_TASK&dataId=2000100006956&0.4366273384106416&contentType=json&ajax=true&tid=2000000002503
#http://v3-test-linux-hse.hd-cloud.com/hse/HSE_WORK_TASK/hse_work_task_submit?parentEntityId=&parentFuncCode=&topEntityId=2000100006960&topFuncCode=HSE_WORK_TASK&dataId=2000100006960&0.6795796836111767&contentType=json&ajax=true&tid=2000000002503
url = '/sy/personal/getIndustry?0.37393450471783507&ajax=true'
caseinfo['url'] = host+url
#动火作业
data = {}

caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 3
caseinfo['name'] = 'index-sy/personal/getOnlUserCount'
caseinfo['isactive'] = 1
#workticketid = workticketid+1
#http://v3-test-linux-hse.hd-clod.com/hse/HSE_WORK_TICKET_DH/cardSave?parentEntityId=2000100006960&parentFuncCode=HSE_WORK_TASK&topEntityId=2000100006960&topFuncCode=HSE_WORK_TASK&dataId=2000100008242&ts=1624417016735&0.4432067065357832&contentType=json&ajax=true&tid=2000000002503
#http://v3-test-linux-hse.hd-cloud.com/hse/HSE_WORK_TICKET_DH/cardSave?parentEntityId=2000100006959&parentFuncCode=HSE_WORK_TASK&topEntityId=2000100006959&topFuncCode=HSE_WORK_TASK&dataId=2000100008241&ts=1624417658853&0.09235504041001308&contentType=json&ajax=true&tid=2000000002503
url = '/sy/personal/getOnlUserCount?0.9743027357407339&ajax=true'
#动火作业
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

# caseinfo['id'] = 4
# caseinfo['name'] = '/allowAccess/getHDConfigBycode'
# caseinfo['isactive'] = 1
# #workticketid = workticketid+1
# #http://v3-test-linux-hse.hd-cloud.com/hse/HSE_WORK_TICKET_DH/hse_work_ticket_submit?parentEntityId=2000100007052&parentFuncCode=HSE_WORK_TASK&topEntityId=2000100007052&topFuncCode=HSE_WORK_TASK&dataId=2000100008352&ts=1624425675527&0.9097665751101249&contentType=json&ajax=true&tid=2000000002503
# #http://v3-test-linux-hse.hd-cloud.com/hse/HSE_WORK_TICKET_DH/hse_work_ticket_submit?parentEntityId=2000100007051&parentFuncCode=HSE_WORK_TASK&topEntityId=2000100007051&topFuncCode=HSE_WORK_TASK&dataId=2000100008351&ts=1624425468636&0.23738799471216576&contentType=json&ajax=true&tid=2000000002503
# url = '/allowAccess/getHDConfigBycode?code=multi_func_layout&ajax=true'
# caseinfo['url'] =host + url
# #动火作业
# data = {
# 	"tableName": "hse_work_ticket",
# 	"clause": "",
# 	"tasktype": "",
# 	"otherattaches": "",
# 	"radiosourcenum": "",
# 	"relevantdoc": "",
# 	"safedistance": "",
# 	"relation": "",
# 	"issjtssxzy": "",
# 	"isupgradedh": "",
# 	"isdzdh": "",
# 	"risk_rank": "",
# 	"isrecord": "",
# 	"guid": "",
# 	"excavation_eqp": "",
# 	"territorialunitcode": "0001",
# 	"ticketdealphoto": "",
# 	"pipeline_level": "",
# 	"replacement": "",
# 	"dataStatus": 0,
# 	"ver": 1,
# 	"created_by": 2000000017571,
# 	"created_dt": starttime,
# 	"updated_by": 2000000017571,
# 	"updated_dt": starttime,
# 	"df": 0,
# 	"tenantid": 2000000002503,
# 	"ts": 1624425468636,
# 	"istaskpause": 0,
# 	"classgroup": "",
# 	"isend": "",
# 	"end_reason": "",
# 	"end_dt": "",
# 	"groundwire_num": "",
# 	"groupknife_num": "",
# 	"groundwire_code": "",
# 	"othercontent": "",
# 	"sent_overdueclose_message": 0,
# 	"isupgrade": 0,
# 	"isfireday": 0,
# 	"isdue": "0",
# 	"operator": "",
# 	"worktimeconsum": "",
# 	"device_id": "",
# 	"isfillticket": "",
# 	"task_pause": "",
# 	"projecttype": "",
# 	"is_pause": 0,
# 	"workticketid": workticketid,
# 	"worktaskid": worktaskid,
# 	"equipmentnumber": "",
# 	"worktype": "dh",
# 	"territorialunitid": 2000000009055,
# 	"territorialunitname": "现场总管演示租户",
# 	"applyunitid": 2000000009055,
# 	"applyunitname": "现场总管演示租户",
# 	"worknumber": "",
# 	"worklevel": "gb_dh_workLevel02",
# 	"site": "测试地点-1",
# 	"workway": "gb_dhfs01",
# 	"planstarttime": starttime,
# 	"planendtime": endtime,
# 	"actualstarttime": "",
# 	"actualendtime": "",
# 	"otherwork": "",
# 	"workname": name,
# 	"workcontent": "",
# 	"workunit": 2000000009055,
# 	"workunitname": "现场总管演示租户",
# 	"workstatus": "draft",
# 	"equipmentpipename": "",
# 	"medium": "",
# 	"temperature": "",
# 	"pressure": "",
# 	"blindplate_material": "",
# 	"blindplate_spec": "",
# 	"blindplate_code": "",
# 	"blindplate_mapandcode": "",
# 	"workhighly": "",
# 	"objectmass": "",
# 	"poweraccesspoint": "",
# 	"workvoltage": "",
# 	"equipmentandpower": "",
# 	"otherunit": "",
# 	"workreason": "",
# 	"isharmconfirm": "",
# 	"ismeasureconfirm": "",
# 	"isgascomplate": "",
# 	"issigncomplate": "",
# 	"created_by_name": "admin2021",
# 	"updated_by_name": "admin2021",
# 	"closereason": "",
# 	"gastestaging": "",
# 	"blindplate_worktype": "",
# 	"gasket_material": "",
# 	"gasket_spec": "",
# 	"close_type": "",
# 	"delaynum": 0,
# 	"beendelaynum": 0,
# 	"isppeconfirm": "",
# 	"invalidreason": "",
# 	"hassafetyplan": "",
# 	"hashseplan": "",
# 	"hasemergencyplan": "",
# 	"hasdrawpaper": "",
# 	"haschecklist": "",
# 	"hasrescueplan": "",
# 	"loadradius": "",
# 	"loaddegree": "",
# 	"loadrate": "",
# 	"objectnorm": "",
# 	"loadmass": "",
# 	"haslineopensitemap": "",
# 	"radiosourcetype": "",
# 	"sourcecode": "",
# 	"sourcestrength": "",
# 	"suprange": "",
# 	"controlrange": "",
# 	"drawshow": "",
# 	"hashookcheck": "",
# 	"hasfacadecheck": "",
# 	"hasdrivermedical": "",
# 	"objectname": "",
# 	"cancelreason": "",
# 	"hidesituation": "",
# 	"work_position_id": 2000000003328,
# 	"isgas_detection": "1",
# 	"gas_aging": 2,
# 	"isqualgasdetection": "",
# 	"dig_size_l": "",
# 	"dig_size_w": "",
# 	"dig_size_h": "",
# 	"attaches": "",
# 	"lock_status": "0",
# 	"lock_equipment_id": "",
# 	"dl_uuid": "",
# 	"dl_time": "",
# 	"level_upgrade": 0,
# 	"loadgoodsname": "",
# 	"loadhigh": "",
# 	"worktask_name": name,
# 	"worktype_name": "动火作业",
# 	"dz_craneno": "",
# 	"gas_standard_type": "",
# 	"isproprietor": "",
# 	"worksite": "",
# 	"workticketmbcdid": "",
# 	"isstoppower": "",
# 	"work_position_name": "奥体中心",
# 	"gas_detector_no": "",
# 	"additional_requirements": "",
# 	"worklevel_org": "",
# 	"wf_current_nodeid": "",
# 	"wf_audit_time": "",
# 	"wf_current_user": "",
# 	"wf_audit_state": "0",
# 	"wf_create_user": 2000000017571,
# 	"wf_instance": "",
# 	"wf_type": "",
# 	"isabnormal": "",
# 	"abnormaltype": "",
# 	"ishas_wtd": ""
# }
# caseinfo['data'] =data
# testsuit.append(caseinfo.copy())

caseinfo['id'] = 5
caseinfo['name'] = 'index-common/getUserAndConfInfo'
caseinfo['isactive'] = 1
#workticketid = workticketid+1
#http://v3-test-linux-hse.hd-cloud.com/hse/HSE_WORK_TICKET_DH/hse_work_ticket_submit?parentEntityId=2000100007052&parentFuncCode=HSE_WORK_TASK&topEntityId=2000100007052&topFuncCode=HSE_WORK_TASK&dataId=2000100008352&ts=1624425675527&0.9097665751101249&contentType=json&ajax=true&tid=2000000002503
#http://v3-test-linux-hse.hd-cloud.com/hse/HSE_WORK_TICKET_DH/hse_work_ticket_submit?parentEntityId=2000100007051&parentFuncCode=HSE_WORK_TASK&topEntityId=2000100007051&topFuncCode=HSE_WORK_TASK&dataId=2000100008351&ts=1624425468636&0.23738799471216576&contentType=json&ajax=true&tid=2000000002503
url = '/common/getUserAndConfInfo?0.00841243796240998&ajax=true'
caseinfo['url'] =host + url
#动火作业
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 6
caseinfo['name'] = 'index-portal/MSG_NOTICE_PORTAL/qryNotice'
caseinfo['isactive'] = 1
#workticketid = workticketid+1
#http://v3-test-linux-hse.hd-cloud.com/hse/HSE_WORK_TICKET_DH/hse_work_ticket_submit?parentEntityId=2000100007052&parentFuncCode=HSE_WORK_TASK&topEntityId=2000100007052&topFuncCode=HSE_WORK_TASK&dataId=2000100008352&ts=1624425675527&0.9097665751101249&contentType=json&ajax=true&tid=2000000002503
#http://v3-test-linux-hse.hd-cloud.com/hse/HSE_WORK_TICKET_DH/hse_work_ticket_submit?parentEntityId=2000100007051&parentFuncCode=HSE_WORK_TASK&topEntityId=2000100007051&topFuncCode=HSE_WORK_TASK&dataId=2000100008351&ts=1624425468636&0.23738799471216576&contentType=json&ajax=true&tid=2000000002503
url = '/portal/MSG_NOTICE_PORTAL/qryNotice?0.12908528478772152&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
#动火作业
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 4
caseinfo['name'] = 'index-portal/MSG_NOTICE_PORTAL/qryNotice'
caseinfo['isactive'] = 1
#workticketid = workticketid+1
#http://v3-test-linux-hse.hd-cloud.com/hse/HSE_WORK_TICKET_DH/hse_work_ticket_submit?parentEntityId=2000100007052&parentFuncCode=HSE_WORK_TASK&topEntityId=2000100007052&topFuncCode=HSE_WORK_TASK&dataId=2000100008352&ts=1624425675527&0.9097665751101249&contentType=json&ajax=true&tid=2000000002503
#http://v3-test-linux-hse.hd-cloud.com/hse/HSE_WORK_TICKET_DH/hse_work_ticket_submit?parentEntityId=2000100007051&parentFuncCode=HSE_WORK_TASK&topEntityId=2000100007051&topFuncCode=HSE_WORK_TASK&dataId=2000100008351&ts=1624425468636&0.23738799471216576&contentType=json&ajax=true&tid=2000000002503
url = '/portal/MSG_NOTICE_PORTAL/qryNotice?0.12908528478772152&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
#动火作业
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 7
caseinfo['name'] = 'tzd-hse/HSE_NOTICE/getMetaData'
caseinfo['isactive'] = 1
url = '/hse/HSE_NOTICE/getMetaData?isself=0&0.3519070469565644&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
#动火作业
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 8
caseinfo['name'] = 'tzd-hse/MSG_NOTICE_PORTAL/qryNotice'
caseinfo['isactive'] = 1
url = '/hse/MSG_NOTICE_PORTAL/qryNotice?0.11309662220340178&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
#动火作业
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 9
caseinfo['name'] = 'tzd-hse/HSE_NOTICE/cardRead'
caseinfo['isactive'] = 1
url = '/hse/HSE_NOTICE/cardRead?parentEntityId=&parentFuncCode=&topEntityId=1000000131632&topFuncCode=HSE_NOTICE&dataId=1000000131631&editId=1000000131632&0.19542753565936066&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
#动火作业
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 10
caseinfo['name'] = 'tzd-hse/HSE_NOTICE/listQuery'
caseinfo['isactive'] = 1
url = '/hse/HSE_NOTICE/listQuery?parentEntityId=&parentFuncCode=&topEntityId=1000000131632&topFuncCode=HSE_NOTICE&dataId=1000000131632&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22notice_type%22%3Anull%2C%22notice_status%22%3Anull%2C%22fault_code_group%22%3Anull%2C%22notice_desc%22%3A%22%E7%94%B5%22%7D&page=1&rows=50&0.8007681693742965&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
#动火作业
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 11
caseinfo['name'] = 'sgzyp-hse/HSE_WORK_TICKET_GB_SGZY/getMetaData'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_TICKET_GB_SGZY/getMetaData?isself=0&0.5101290904051929&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 12
caseinfo['name'] = 'sgzyp-hse/HSE_WORK_TICKET_GB_SGZY/listQuery'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_TICKET_GB_SGZY/listQuery?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_TICKET_GB_SGZY&queryParam=%7B%22tableName%22%3Anull%2C%22workstatus%22%3A%22draft%2Cinaudit%2CinJob%2CsceneConfirm%22%2C%22workname%22%3A%22%E6%B5%8B%E8%AF%95%22%7D&page=1&rows=50&0.9313465152874421&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 13
caseinfo['name'] = '施工作业票送交'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_TICKET_GB_SGZY/wfSendShow?parentEntityId=&parentFuncCode=&topEntityId=2000000095900&topFuncCode=HSE_WORK_TICKET_GB_SGZY&dataId=2000000095900&ts=1655518105577&0.4238209574662122&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 14
caseinfo['name'] = 'jsa-hse/HSE_JSA_TEMPLETE_NEW/listQuery'
caseinfo['isactive'] = 1
url = '/hse/HSE_JSA_TEMPLETE_NEW/listQuery?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_JSA_TEMPLETE_NEW&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22temp_type%22%3Anull%2C%22temp_name%22%3A%22%E7%89%B9%E6%AE%8A%22%7D&page=1&rows=50&0.024042099433414954&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
#testsuit.append(caseinfo.copy())

caseinfo['id'] = 15
caseinfo['name'] = 'jsa-hse/HSE_WORK_TICKET_GB_SGZY/cardAdd'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_TICKET_GB_SGZY/cardAdd?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_TICKET_GB_SGZY&0.21734052417673566&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 16
caseinfo['name'] = 'hse-hse/HSE_WORK_TASK/getMetaData'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_TASK/getMetaData?0.9966394759205981&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 17
caseinfo['name'] = 'hse-hse/HSE_WORK_TASK/listQuery'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_TASK/listQuery?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_TASK&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22workstatus%22%3Anull%2C%22workname%22%3A%22%E6%B5%8B%E8%AF%95%22%7D&page=1&rows=50&0.9498687915108064&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 18
caseinfo['name'] = 'hse-hse/HSE_WORK_TASK/cardAdd'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_TASK/cardAdd?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_TASK&0.5990031048467857&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 19
caseinfo['name'] = 'zyyydjb-hse/HSE_WORK_APPOINTMENT_REGISTRATION/getMetaData'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_APPOINTMENT_REGISTRATION/getMetaData?isself=0&0.5480530672746282&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 20
caseinfo['name'] = 'lsyd-hse/HSE_WORK_TICKET_LSYD_READ/listQuery'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_TICKET_LSYD_READ/listQuery?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_TICKET_LSYD_READ&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22workstatus%22%3A%22close%22%2C%22invoicingunit%22%3Anull%2C%22invoicingunitname%22%3Anull%7D&page=1&rows=50&0.7419006655383926&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 21
caseinfo['name'] = 'rwtz-hse/HSE_WORK_TASK_ACCOUNT/getMetaData'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_TASK_ACCOUNT/getMetaData?isself=0&0.965009138270795&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 22
caseinfo['name'] = 'rwtz-hse/HSE_WORK_TASK_ACCOUNT/listQuery'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_TASK_ACCOUNT/listQuery?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_TASK_ACCOUNT&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22worktickettype%22%3Anull%2C%22workname%22%3A%22%E6%B5%8B%E8%AF%95%22%7D&page=1&rows=50&0.3953742091178154&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 23
caseinfo['name'] = 'zyptz-hse/HSE_WORK_TICKET_ACCOUNT/getMetaData'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_TICKET_ACCOUNT/getMetaData?isself=0&0.7851079264033038&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 24
caseinfo['name'] = 'zyptz-hse/HSE_WORK_TICKET_ACCOUNT/listQuery'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_TICKET_ACCOUNT/listQuery?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_TICKET_ACCOUNT&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22worktype%22%3Anull%2C%22close_type%22%3Anull%2C%22workstatus%22%3Anull%2C%22workname%22%3A%22%E6%B5%8B%E8%AF%95%22%7D&page=1&rows=50&0.8850491451191946&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 25
caseinfo['name'] = 'zyptz-hse/HSE_WORK_TICKET_XKZ_GB/cardRead'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_TICKET_XKZ_GB/cardRead?parentEntityId=2000000067064&parentFuncCode=HSE_WORK_TICKET_ACCOUNT&topEntityId=2000000067064&topFuncCode=HSE_WORK_TICKET_ACCOUNT&editId=2000000067064&0.7268140995999566&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
#testsuit.append(caseinfo.copy())

caseinfo['id'] = 26
caseinfo['name'] = 'gbyczyptz-hse/HSE_WORK_TICKET_ACCOUNT_CLOSEEXCEPTION/getMetaData'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_TICKET_ACCOUNT_CLOSEEXCEPTION/getMetaData?isself=0&0.09270167578639743&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 27
caseinfo['name'] = 'gbyczyptz-hse/HSE_WORK_TICKET_ACCOUNT_CLOSEEXCEPTION/listQuery'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_TICKET_ACCOUNT_CLOSEEXCEPTION/listQuery?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_TICKET_ACCOUNT_CLOSEEXCEPTION&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22worktype%22%3Anull%2C%22level_upgrade%22%3Anull%2C%22close_type%22%3Anull%2C%22workname%22%3A%22%E6%B5%8B%E8%AF%95%22%7D&page=1&rows=50&0.17589674427268354&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 28
caseinfo['name'] = 'gbyczyptz-hse/HSE_WORK_TICKET_SX_CLOSE/cardRead'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_TICKET_SX_CLOSE/cardRead?parentEntityId=2000000067060&parentFuncCode=HSE_WORK_TICKET_ACCOUNT_CLOSEEXCEPTION&topEntityId=2000000067060&topFuncCode=HSE_WORK_TICKET_ACCOUNT_CLOSEEXCEPTION&editId=2000000067060&0.6421611070572617&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 29
caseinfo['name'] = 'cbscj-hse/HSE_WORK_APPOINT_CONTRACTOR_UNDERTAKE/getMetaData'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_APPOINT_CONTRACTOR_UNDERTAKE/getMetaData?isself=0&0.2911704843199747&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 30
caseinfo['name'] = 'cbscj-hse/HSE_WORK_APPOINT_CONTRACTOR_UNDERTAKE/listQuery'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_APPOINT_CONTRACTOR_UNDERTAKE/listQuery?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_APPOINT_CONTRACTOR_UNDERTAKE&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22wf_audit_state%22%3Anull%2C%22workname%22%3A%22%E6%B5%8B%E8%AF%95%22%7D&page=1&rows=50&0.8908583149251241&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 31
caseinfo['name'] = 'cbscj-hse/HSE_WORK_APPOINT_CONTRACTOR_UNDERTAKE/cardAdd'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_APPOINT_CONTRACTOR_UNDERTAKE/cardAdd?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_APPOINT_CONTRACTOR_UNDERTAKE&0.41046879927480573&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 32
caseinfo['name'] = 'cbscj-hse/HSE_WORK_APPOINT_CONTRACTOR_UNDERTAKE/cardRead'
caseinfo['isactive'] = 1
url = '/hse/HSE_WORK_APPOINT_CONTRACTOR_UNDERTAKE/cardRead?parentEntityId=&parentFuncCode=&topEntityId=2000000000920&topFuncCode=HSE_WORK_APPOINT_CONTRACTOR_UNDERTAKE&dataId=2000000000920&editId=2000000000920&0.06493400829743701&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 33
caseinfo['name'] = 'mbcd-hse/HSE_TICKET_MBCD/getMetaData'
caseinfo['isactive'] = 1
url = '/hse/HSE_TICKET_MBCD/getMetaData?isself=0&0.5326787792030729&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 34
caseinfo['name'] = 'mbcd-hse/HSE_TICKET_MBCD/listQuery'
caseinfo['isactive'] = 1
url = '/hse/HSE_TICKET_MBCD/listQuery?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_TICKET_MBCD&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22workstatus%22%3Anull%2C%22device%22%3A%22%E6%B5%8B%E8%AF%95%22%7D&page=1&rows=50&0.9133451988422372&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 35
caseinfo['name'] = 'mbcd-hse/HSE_TICKET_MBCD/cardAdd'
caseinfo['isactive'] = 1
url = '/hse/HSE_TICKET_MBCD/cardAdd?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_TICKET_MBCD&0.6087652833042487&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 36
caseinfo['name'] = '申请人资质台账进入-sy/SY_USER_PERSONAPTITUDE_HSE_SQR/getMetaData'
caseinfo['isactive'] = 1
url = '/sy/SY_USER_PERSONAPTITUDE_HSE_SQR/getMetaData?isself=0&0.5033707577229438&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 37
caseinfo['name'] = '申请人资质台账查看-sy/SY_USER_PERSONAPTITUDE_HSE_SQR/cardRead'
caseinfo['isactive'] = 1
url = '/sy/SY_USER_PERSONAPTITUDE_HSE_SQR/cardRead?parentEntityId=&parentFuncCode=&topEntityId=2000000000160&topFuncCode=SY_USER_PERSONAPTITUDE_HSE_SQR&editId=2000000000160&0.46634425572260807&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 38
caseinfo['name'] = '申请人资质台账添加-sy/SY_USER_PERSONAPTITUDE_HSE_SQR/cardAdd'
caseinfo['isactive'] = 1
url = '/sy/SY_USER_PERSONAPTITUDE_HSE_SQR/cardAdd?parentEntityId=&parentFuncCode=&topEntityId=2000000000160&topFuncCode=SY_USER_PERSONAPTITUDE_HSE_SQR&dataId=2000000000160&0.36665322130135936&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 39
caseinfo['name'] = '作业人资质台账进入-sy/SY_USER_PERSONAPTITUDE_HSE_ZYR/getMetaData'
caseinfo['isactive'] = 1
url = '/sy/SY_USER_PERSONAPTITUDE_HSE_ZYR/getMetaData?isself=0&0.965675804344089&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 40
caseinfo['name'] = '作业人资质台账查看-sy/SY_USER_PERSONAPTITUDE_HSE_ZYR/cardRead'
caseinfo['isactive'] = 1
url = '/sy/SY_USER_PERSONAPTITUDE_HSE_ZYR/cardRead?parentEntityId=&parentFuncCode=&topEntityId=2000000019954&topFuncCode=SY_USER_PERSONAPTITUDE_HSE_ZYR&dataId=2000000019954&editId=2000000019954&0.857790990075997&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 41
caseinfo['name'] = '作业人资质台账添加-sy/SY_USER_PERSONAPTITUDE_HSE_ZYR/cardAdd'
caseinfo['isactive'] = 1
url = '/sy/SY_USER_PERSONAPTITUDE_HSE_ZYR/cardAdd?parentEntityId=&parentFuncCode=&topEntityId=2000000019954&topFuncCode=SY_USER_PERSONAPTITUDE_HSE_ZYR&dataId=2000000019954&0.47308813775301783&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())


caseinfo['id'] = 42
caseinfo['name'] = '监护人资质台账进入-sy/SY_USER_PERSONAPTITUDE_HSE_JHR/getMetaData'
caseinfo['isactive'] = 1
url = '/sy/SY_USER_PERSONAPTITUDE_HSE_JHR/getMetaData?isself=0&0.26076720793894625&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 43
caseinfo['name'] = '监护人资质台账查看-sy/SY_USER_PERSONAPTITUDE_HSE_JHR/cardRead'
caseinfo['isactive'] = 1
url = '/sy/SY_USER_PERSONAPTITUDE_HSE_JHR/cardRead?parentEntityId=&parentFuncCode=&topEntityId=2000000000699&topFuncCode=SY_USER_PERSONAPTITUDE_HSE_JHR&editId=2000000000699&0.12538968393758565&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 44
caseinfo['name'] = '监护人资质台账添加-sy/SY_USER_PERSONAPTITUDE_HSE_JHR/cardAdd'
caseinfo['isactive'] = 1
url = '/sy/SY_USER_PERSONAPTITUDE_HSE_JHR/cardAdd?parentEntityId=&parentFuncCode=&topEntityId=2000000000699&topFuncCode=SY_USER_PERSONAPTITUDE_HSE_JHR&dataId=2000000000699&0.8772704820331805&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 45
caseinfo['name'] = '批准人资质台账进入-sy/SY_USER_PERSONAPTITUDE_HSE_PZR/getMetaData'
caseinfo['isactive'] = 1
url = '/sy/SY_USER_PERSONAPTITUDE_HSE_PZR/getMetaData?isself=0&0.3360141982327147&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 46
caseinfo['name'] = '批准人资质台账查看-sy/SY_USER_PERSONAPTITUDE_HSE_PZR/cardRead'
caseinfo['isactive'] = 1
url = '/sy/SY_USER_PERSONAPTITUDE_HSE_PZR/cardRead?parentEntityId=&parentFuncCode=&topEntityId=2000000019974&topFuncCode=SY_USER_PERSONAPTITUDE_HSE_PZR&dataId=2000000019974&editId=2000000019974&0.5735577424849185&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 47
caseinfo['name'] = '批准人资质台账添加-sy/SY_USER_PERSONAPTITUDE_HSE_PZR/cardAdd'
caseinfo['isactive'] = 1
url = '/sy/SY_USER_PERSONAPTITUDE_HSE_PZR/cardAdd?parentEntityId=&parentFuncCode=&topEntityId=2000000019974&topFuncCode=SY_USER_PERSONAPTITUDE_HSE_PZR&dataId=2000000019974&0.4692925367905503&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())

caseinfo['id'] = 48
caseinfo['name'] = 'PC-票证浏览'
caseinfo['isactive'] = 1
#https://tjsh.ushayden.com/rqreports/hse/HSE_WORK_TICKET_GC/reportCommonShow?rpx=HSE_PRESET_GCZY_GB_NTICKET.rpx&workticketid=2000000097610&worktype=gc&dzqm_url=http://hse.hayden.com:80&uuid=4fe165cade8f424b81d76271c83c33c9klItWhUnCrtsBLxyMmBdOSAhttncYL
url = '/sy/SY_USER_PERSONAPTITUDE_HSE_PZR/cardAdd?parentEntityId=&parentFuncCode=&topEntityId=2000000019974&topFuncCode=SY_USER_PERSONAPTITUDE_HSE_PZR&dataId=2000000019974&0.4692925367905503&contentType=json&ajax=true&tid=2000000002404'
caseinfo['url'] =host + url
data = {}
caseinfo['data'] =data
#testsuit.append(caseinfo.copy())