
from tools import tool
from globalpkg.global_var import workticketid


case = '天津石化-施工作业票-低风险-申请pc-现场确认-作业处理'

#times
starttime = tool.starttime
endtime = tool.endtime
now = tool.now

#作业任务名称
name = tool.ran_name_with_str()
#print("作业任务名称：",name)

#用例信息变量定义
testsuitmp = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['exresult'] = ''
caseinfo['isactive'] = ''
xkzticketid = workticketid + 1

count =0
#用例信息
caseinfo['id'] = 1
caseinfo['name'] = '施工作业票保存'
caseinfo['isactive'] = 1
#拼写预约URL
#https://tjsh.ushayden.com/m/pub-base_m/a/getConfigs.json
url = '/hse/HSE_WORK_TICKET_GB_SGZY/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_WORK_TICKET_GB_SGZY&0.751973906961098&contentType=json&ajax=true&tid=2000000002404'
host='https://tjsh.ushayden.com'
caseinfo['url'] = host+url
#
data = {
	"tableName": "hse_work_ticket",
	"delaynum": "999",
	"applyunitname": "联合一车间",
	"equipmentname": "",
	"worktype__name": "施工作业",
	"worktype": "xkz",
	"ishas_wtd": "0",
	"iscontractor": "1",
	"worktype_name": "施工作业票",
	"territorialunitid": "2000000009563",
	"istask": "1",
	"territorialunitname": "联合一车间",
	"territorialunitcode": "0001011006",
	"applyunitid": "2000000009563",
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
	"worklevel": "low_risk",
	"other_worktype": "xkz",
	"hassafetyplan": "",
	"hasfacadecheck": "",
	"hasdrivermedical": "",
	"isgas_detection": "",
	"close_type": "",
	"lock_status": "",
	"hse_notice_id": 1000000131646,
	"notice_code": "030000941585",
	"workname": name,
	"equipmentnumber": "0623-1",
	"workunit": 2000000008566,
	"workunitname": "承包商",
	"site": "0623-1",
	"medium": "0623-1",
	"temperature": "0623-1",
	"pressure": "0623-1",
	"workcontent": "0623-1",
	"planstarttime":starttime,
	"planendtime": endtime,
	"other_worktype_name": "施工作业票"
}
caseinfo['data'] =data
testsuitmp.append(caseinfo.copy())

#用例信息
caseinfo['id'] = 2
caseinfo['name'] = '施工作业票提交'
caseinfo['isactive'] = 1
#拼写预约URL
#https://tjsh.ushayden.com
url = '/hse/HSE_WORK_TICKET_GB_SGZY/hse_work_ticket_submit?parentEntityId=&parentFuncCode=&topEntityId=2000000097667&topFuncCode=HSE_WORK_TICKET_GB_SGZY&dataId=%d&ts=1655955383245&0.7786379883662571&contentType=json&ajax=true&tid=2000000002404'%(xkzticketid)
host='https://tjsh.ushayden.com'
caseinfo['url'] = host+url
#
data = {
	"tableName": "hse_work_ticket",
	"proposer_id": "",
	"otherattaches": "",
	"owner_id": "",
	"relevantdoc": "",
	"jsa_code": "",
	"relation": "",
	"territorialdeptid": 2000000009557,
	"workprojectid": "",
	"owner_name": "",
	"tasktype": "",
	"proposer": "",
	"territorialdeptcode": "0000000E",
	"equipmentname": "",
	"close_time": "",
	"invoicingunitname": "",
	"invoicingunit": "",
	"eqp_id": "",
	"other_worktype": "",
	"hse_notice_id": 1000000131646,
	"notice_code": "030000941585",
	"guid": "",
	"work_position_point": "",
	"workprojectname": "",
	"pipeline_level": "",
	"replacement": "",
	"territorialdeptname": "炼油部",
	"is_send_check_gas": "",
	"radiosourcenum": "",
	"register_time": "",
	"iscontractor": "1",
	"risk_rank": "",
	"meqp_code": "",
	"jsaid": "",
	"audit_starttime": "",
	"audit_endtime": "",
	"clause": "",
	"worktype__name": "施工作业",
	"safedistance": "",
	"meqp_id": "",
	"workunit_person_name": "",
	"issjtssxzy": "",
	"isupgradedh": "",
	"isdzdh": "",
	"isrecord": "",
	"con_personid": "",
	"eqp_code": "",
	"excavation_eqp": "",
	"territorialunitcode": "0001011006",
	"workunit_person_id": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 2000000119297,
	"created_dt": now,
	"updated_by": 2000000119297,
	"updated_dt": now,
	"df": 0,
	"tenantid": 2000000002404,
	"ts": 1655955383245,
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
	"isupgrade": 0,
	"isfireday": 0,
	"isdue": 0,
	"operator": "",
	"worktimeconsum": "",
	"device_id": "",
	"isfillticket": "",
	"task_pause": "",
	"projecttype": "repaire",
	"is_pause": 0,
	"workticketid": xkzticketid,
	"worktaskid": "",
	"equipmentnumber": "0623-1",
	"worktype": "xkz",
	"territorialunitid": 2000000009563,
	"territorialunitname": "联合一车间",
	"applyunitid": 2000000009563,
	"applyunitname": "联合一车间",
	"worknumber": "",
	"worklevel": "low_risk",
	"site": "0623-1",
	"workway": "",
	"planstarttime": starttime,
	"planendtime": endtime,
	"actualstarttime": "",
	"actualendtime": "",
	"otherwork": "",
	"workname": name,
	"workcontent": "0623-1",
	"workunit": 2000000008566,
	"workunitname": "承包商",
	"workstatus": "draft",
	"equipmentpipename": "",
	"medium": "0623-1",
	"temperature": "0623-1",
	"pressure": "0623-1",
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
	"created_by_name": "魏巍",
	"updated_by_name": "魏巍",
	"closereason": "",
	"gastestaging": "",
	"blindplate_worktype": "",
	"gasket_material": "",
	"gasket_spec": "",
	"close_type": "",
	"delaynum": 999,
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
	"work_position_id": "",
	"isgas_detection": "0",
	"gas_aging": "",
	"isqualgasdetection": "",
	"dig_size_l": "",
	"dig_size_w": "",
	"dig_size_h": "",
	"attaches": "",
	"lock_status": "",
	"lock_equipment_id": "",
	"dl_uuid": "",
	"dl_time": "",
	"level_upgrade": "",
	"loadgoodsname": "",
	"loadhigh": "",
	"worktask_name": "",
	"worktype_name": "施工作业票",
	"dz_craneno": "",
	"gas_standard_type": "",
	"isproprietor": "",
	"worksite": "",
	"workticketmbcdid": "",
	"isstoppower": "",
	"work_position_name": "",
	"gas_detector_no": "",
	"additional_requirements": "",
	"worklevel_org": "",
	"wf_current_nodeid": "",
	"wf_audit_time": "",
	"wf_current_user": "",
	"wf_audit_state": "0",
	"wf_create_user": 2000000119297,
	"wf_instance": "",
	"wf_type": "",
	"isabnormal": "",
	"abnormaltype": "",
	"ishas_wtd": "0",
	"istask": ""
}
caseinfo['data'] =data
testsuitmp.append(caseinfo.copy())



