#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = ''

import configparser
import os
import time
from useless.pyh import *
from globalpkg.log import logger
from globalpkg.global_var import testdb
from globalpkg.global_var import testcase_report_tb
from globalpkg.global_var import other_tools

executed_history_id = time.strftime('%Y%m%d', time.localtime())  # 流水记录编号

class CollectResult:
    def __init__(self):
        #self.title = title                                       # 网页标签名称
        #self.head = head                                         # 标题
        #self.filename = 'testrepot.html'   # 结果文件名
        #self.dir = './testreport/'         # 结果文件目录
        self.time_took = '00:00:00'         # 测试耗时
        self.success_num = 0                  # 测试通过的用例数
        self.fail_num = 0                     # 测试失败的用例数
        self.error_num = 0                    # 运行出错的用例数
        self.block_num = 0                    # 未运行的测试用例总数
        self.case_total = 0                   # 运行测试用例总数


    # 计算测试结果
    def calc(self):

        logger.info('正在查询测试用例总数')
        query = 'SELECT count(testcase_id) FROM ' + testcase_report_tb + ' WHERE executed_history_id like \'%' + executed_history_id + '%\''
        logger.info("query: %s",query)
        #data = (executed_history_id,)
        data = ''
        result = testdb.select_one_record(query, data)
        logger.info('查询结果%s',result)
        self.case_total = result[0][0]

        logger.info('正在查询执行通过的用例数')
        query = 'SELECT count(testcase_id) FROM ' + testcase_report_tb + ' WHERE runresult = \'Pass\' AND executed_history_id like \'%' + executed_history_id + '%\''

        data = ""
        logger.info('query info%s', query)
        result = testdb.select_one_record(query, data)
        logger.info('no2 %s',result)
        self.success_num = result[0][0]

        logger.info('正在查询执行失败的用例数')
        query = 'SELECT count(testcase_id) FROM ' + testcase_report_tb + ' WHERE runresult = \'Fail\' AND executed_history_id like \'%' + executed_history_id + '%\''
        data = ''
        result = testdb.select_one_record(query, data)
        self.fail_num = result[0][0]

        logger.info('正在查询执行出错的用例数')
        query = 'SELECT count(testcase_id) FROM ' + testcase_report_tb + ' WHERE runresult = \'Error\' AND executed_history_id like \'%' + executed_history_id + '%\''
        data = ''
        result = testdb.select_one_record(query, data)
        self.error_num = result[0][0]

        logger.info('正在查询未执行的用例数')
        query = 'SELECT count(testcase_id) FROM ' + testcase_report_tb + ' WHERE runresult = \'Block\' AND executed_history_id like \'%' + executed_history_id + '%\''
        data = ''
        result = testdb.select_one_record(query, data)
        self.block_num = result[0][0]

        logger.info("天津项目API-TEST执行结果:用例总数%s,执行失败%s，失败率：%s/%s",self.case_total,self.error_num,self.error_num,self.case_total)
if __name__ == "__main__":
    CollectResult()