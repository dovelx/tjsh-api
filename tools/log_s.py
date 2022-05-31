#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = ''

import time
import sys
import random
import datetime
import string

from globalpkg.log import logger
from globalpkg.mydb import MyDB
#from globalpkg.mytestlink import TestLink
from globalpkg.othertools import OtherTools
from tools import sqls
from tools.gethost import pro

projectname = pro()

logger.info('正在初始化数据库[名称：TESTDB]对象')
testdb = MyDB('./config/dbconfig.conf', 'TESTDB')
#长庆项目库
logger.info('正在初始化数据库[名称：%s]对象',projectname)
testdb_test = MyDB('./config/dbconfig.conf', projectname)

#操作hse_work_ticket表，获取workticketid获取

sql_query_ticket = sqls.ticket
sql_query_ts = sqls.ts
sql_query_worktaskid = sqls.worktaskid
sql_query_worktaskid1 = sqls.worktaskid1
sql_query_work_appoint_id =sqls.appoint_id
sql_query_work_jsaid = sqls.sql_query_work_jsaid
sql_query_work_safeclarid = sqls.sql_query_work_safeclarid
sql_query_work_appointid = sqls.sql_query_work_appointid
logger.info('开始数据库查询')

#
temp = testdb_test.select_one_record(sql_query_ticket)
workticketid = temp[0]
#作业票数据库当前ID-workticketid
workticketid = workticketid[0]
print("table-hse_work_ticket:workticketid",workticketid)

#
temp = testdb_test.select_one_record(sql_query_ts)
#获取TS
ts = temp[0][0]
#print(ts)
ts = ts.decode('utf-8')
#TS ID
tsi = int(ts)
print("table-hse_work_ticket:TS",ts)

#
temp = testdb_test.select_one_record(sql_query_worktaskid)
worktaskid = temp[0]
#worktaskid
worktaskid = worktaskid[0]
print("table-hse_work_task:worktaskid(作业任务提交)",worktaskid)

#
temp = testdb_test.select_one_record(sql_query_worktaskid1)
sql_query__worktaskid1 = temp[0]
#worktaskid
worktaskid1 = sql_query__worktaskid1[0]
print("table-hse_work_ticket:worktaskid1（现场确认）",worktaskid1)

temp = testdb_test.select_one_record(sql_query_work_jsaid)
#print(temp)
jsaid = temp[0]
#jsaid
jsaid = jsaid[0]
print("table-hse_safety_analysis :jsaid",jsaid)

temp = testdb_test.select_one_record(sql_query_work_safeclarid)
#print(temp)
safeclarid = temp[0]
#jsaid
safeclarid = safeclarid[0]
print("table-hse_safety_disclosure :safeclarid",safeclarid)

#
temp = testdb_test.select_one_record(sql_query_work_appointid)
#print(temp)
sql_query_work_appointid = temp[0]
#jsaid
sql_query_work_appointid = sql_query_work_appointid[0]
print("table-hse_work_appoint：work_appointid",sql_query_work_appointid)

#
temp = testdb_test.select_one_record(sqls.sql_query_jsa_step_harm_id)
#print(temp)
sql_query_jsa_step_harm_id = temp[0]
#jsaid
sql_query_jsa_step_harm_id = sql_query_jsa_step_harm_id[0]
print("table-hap_hse_clsh：sql_query_jsa_step_harm_id",sql_query_jsa_step_harm_id)

#
temp = testdb_test.select_one_record(sqls.sql_query_jsastepid)
#print(temp)
sql_query_jsastepid = temp[0]
#jsaid
sql_query_jsastepid = sql_query_jsastepid[0]
print("table-hse_safety_analysis_harm：sql_query_jsastepid",sql_query_jsastepid)

#
temp = testdb_test.select_one_record(sqls.sql_query_jsa_step_measure_id)
#print(temp)
sql_query_jsa_step_measure_id = temp[0]
#jsaid
sql_query_jsa_step_measure_id = sql_query_jsa_step_measure_id[0]
print("table-hse_safety_analysis_measure：sql_query_jsa_step_measure_id",sql_query_jsa_step_measure_id)
logger.info("===关闭数据库=============")
testdb_test.close()
'''
logger.info('正在获取testlink')
mytestlink = TestLink().get_testlink()
'''

other_tools = OtherTools()

executed_history_id = time.strftime('%Y%m%d%H%M%S', time.localtime())  # 流水记录编号
# testcase_report_tb = 'testcase_report_tb' + str(executed_history_id)
# case_step_report_tb = 'case_step_report_tb' + str(executed_history_id)
testcase_report_tb = 'testcase_report_tb'
case_step_report_tb = 'case_step_report_tb'
