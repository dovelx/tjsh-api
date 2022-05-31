#hse_work_task  worktaskid

#
# #from globalpkg.log import logger
# #from globalpkg.global_var import testdb_test
# from globalpkg.global_var import case_step_report_tb
# from globalpkg.global_var import testcase_report_tb
# from globalpkg.global_var import executed_history_id
# #from cmain import executed_history_id
# from globalpkg.global_var import other_tools
# import time
# import sys
# import random
# import datetime
# import string

#from globalpkg.log import logger
from globalpkg.mydb import MyDB
#from globalpkg.mytestlink import TestLink
#from globalpkg.othertools import OtherTools
#from tools import sqls
from tools.gethost import pro
#projectname = pro()

# logger.info('正在初始化数据库[名称：TESTDB]对象')
# testdb = MyDB('./config/dbconfig.conf', 'TESTDB')
# #长庆项目库
# logger.info('正在初始化数据库[名称：%s]对象',projectname)
testdb_test = MyDB('./config/dbconfig.conf', "CHANGLING")


def sql_query_worktaskid(name):
    sql_query_work_appointid = 'SELECT worktaskid from hse_work_task WHERE workname like "name";'
    hse_work_task = "hse_work_task"
    #logger.info('正在查询worktaskid')
    query = 'SELECT worktaskid FROM ' + hse_work_task + ' WHERE workname = %s'
    data = (name)
    result = testdb_test.select_one_record(query, data)
    worktaskid = result[0][0]
    #logger.info("===关闭数据库=============")
    testdb_test.close()
    return worktaskid

def sql_query_workticketid(date):
    hse_work_ticket = "hse_work_ticket"
    #select workticketid from hse_work_ticket where created_dt = "2020-06-29 15:55:24" and worktype = "lsyd";
    #logger.info('正在查询worktaskid')
    query = 'SELECT workticketid FROM ' + hse_work_ticket + ' WHERE created_dt = %s and worktype = "lsyd" '
    date = (date,)
    result = testdb_test.select_one_record(query, date)
    print("result",result)
    workticketid = result[0][0]
    #logger.info("===关闭数据库=============")
    testdb_test.close()
    return workticketid

if __name__ == '__main__':
    dt =  "2020-06-29 15:55:24"
    print(sql_query_workticketid(dt))