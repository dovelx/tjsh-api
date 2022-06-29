#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = ''

import time
from globalpkg.log import logger
from globalpkg.mydb import MyDB
from tools.gethost import pro

def CollectResult():
    projectname = pro()

    testcase_report_tb = 'testcase_report_tb'
    case_step_report_tb = 'case_step_report_tb'
    executed_history_id = time.strftime('%Y%m%d', time.localtime())  # 流水记录编号

    logger.info('正在初始化数据库[名称：TESTDB]对象')
    testdb = MyDB('./config/dbconfig.conf', 'TESTDB')
    #项目库
    logger.info('正在初始化数据库[名称：%s]对象',projectname)
    testdb_test = MyDB('./config/dbconfig.conf', projectname)

    logger.info('开始数据库查询')

    #

    logger.info('正在查询测试用例总数')
    query = 'SELECT count(testcase_id) FROM ' + testcase_report_tb + ' WHERE executed_history_id like \'%' + executed_history_id + '%\''
    logger.info("query: %s", query)
    # data = (executed_history_id,)
    data = ''
    result = testdb.select_one_record(query, data)
    logger.info('查询结果%s', result)
    case_total = result[0][0]

    logger.info('正在查询执行通过的用例数')
    query = 'SELECT count(testcase_id) FROM ' + testcase_report_tb + ' WHERE runresult = \'Pass\' AND executed_history_id like \'%' + executed_history_id + '%\''

    data = ""
    logger.info('query info%s', query)
    result = testdb.select_one_record(query, data)
    logger.info('no2 %s', result)
    success_num = result[0][0]

    logger.info('正在查询执行失败的用例数')
    query = 'SELECT count(testcase_id) FROM ' + testcase_report_tb + ' WHERE runresult = \'Fail\' AND executed_history_id like \'%' + executed_history_id + '%\''
    data = ''
    result = testdb.select_one_record(query, data)
    fail_num = result[0][0]

    logger.info('正在查询执行出错的用例数')
    query = 'SELECT count(testcase_id) FROM ' + testcase_report_tb + ' WHERE runresult = \'Error\' AND executed_history_id like \'%' + executed_history_id + '%\''
    data = ''
    result = testdb.select_one_record(query, data)
    error_num = result[0][0]

    logger.info('正在查询未执行的用例数')
    query = 'SELECT count(testcase_id) FROM ' + testcase_report_tb + ' WHERE runresult = \'Block\' AND executed_history_id like \'%' + executed_history_id + '%\''
    data = ''
    result = testdb.select_one_record(query, data)
    block_num = result[0][0]
    #error_num = 22
    #print(format(float(a) / float(b), '.2f'))
    err_per = error_num * 100 / case_total
    err_per = format(err_per,'.2f')
    #logger.info("执行结果:用例总数：%s 个,执行失败：%s 个，失败率：%s %%", case_total, error_num, err_per)
    result_com = ' 接口测试结果: 用例总数：'+ str(case_total) + ' 个,执行失败：' + str(error_num) + ' 个，失败率：' + str(err_per) + ' %。'
    logger.info("%s",result_com)
    logger.info("===关闭数据库=============")
    testdb_test.close()
    return result_com
if __name__ == "__main__":
    res = CollectResult()
    print(res)





