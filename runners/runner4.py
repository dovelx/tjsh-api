#pc get 和post
from tools.datas import *
from tools import method
from globalpkg.global_var import *
import time
from tools.gethost import pro
#post.p(caseinfo,url2,headers,cookies,data)
def runcase(testsuit,cookies):

    print(cookies)
    print('用例总数：',len(testsuit))
    for i in range(len(testsuit)):

        caseinfo = testsuit[i]
        logger.info("执行用例id=%s,name=%s",caseinfo['id'],caseinfo['name'] )
        if caseinfo['flag'] == "get":
            result = method.gh(caseinfo,gheaders,cookies)
        elif caseinfo['flag'] == "post":
            result = method.pa(caseinfo, headers, cookies)
        logger.info("执行用例[id=%s,name=%s]执行结果:%s", caseinfo['id'], caseinfo['name'],result)

        #插入执行情况
        # 构造测试步骤对象
        step_id = 1
        step_number = 1
        step_action = ''
        testcase_name = testsuit[i]['name']
        # testcase_steps = 1
        # testcase_isactive = 1
        # testsuite_id = 1
        # testsuite_name = "作业许可"
        testplan = "Plan1"
        #project_name = "changqing"
        testcase_id = testsuit[i]['id']
        testproject = pro()
        #preconditions = ''
        host = ""
        port = ""

        case_executed_history_id = time.strftime('%Y%m%d%H%M%S', time.localtime())
        expected_results = ""
        #tc_external_id = 1
        sql_insert = 'INSERT INTO ' + case_step_report_tb + '(executed_history_id, testcase_id, testcase_name, testplan, project, step_id, step_num, protocol_method, protocol, host, port, ' \
                                                            'step_action, expected_results, runresult, reason, runtime)' \
                                                            ' VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

        data = (case_executed_history_id, testcase_id, testcase_name, testplan, testproject, step_id,
                step_number, '无', 'http', host, port,
                step_action, expected_results, 'Unexecuted', '', '0000-00-00 00:00:00')
        #logger.info('记录测试步骤到测试步骤报告表')
        testdb.execute_insert(sql_insert, data)

        fail_or_error_reason = ''
        protocol_method = caseinfo['flag']
        run_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # 记录运行时间
        action_of_step = ""
        if result == "pass":
            result_of_step = "pass"
        else:
            result_of_step = "fail"
            fail_or_error_reason = result
        sql_update = 'UPDATE ' + case_step_report_tb + ' SET runresult=\"%s\",reason=\"%s\", protocol_method=\"%s\", runtime=\"%s\",' \
                                                       'step_action=\"%s\", expected_results=\"%s\"' \
                                                       ' WHERE executed_history_id = %s AND testcase_id = %s AND step_id = %s' \
                                                       ' AND project=\'%s\' AND testplan=\'%s\'  AND runtime=\'%s\''
        data = ("pass", fail_or_error_reason, protocol_method, run_time, action_of_step, result_of_step,
                str(case_executed_history_id), testcase_id, step_id,
                testproject, testplan, '0000-00-00 00:00:00')
        #logger.info('正在更新步骤执行结果')
        testdb.execute_update(sql_update, data)

        logger.info('测试用例[id=%s, name=%s]执行成功' % (testcase_id, testcase_name))

    #结果处理

        testcase_name = testsuit[i]['name']
        # testcase_steps = 1
        # testcase_isactive = 1
        # testsuite_id = 1
        testsuite_name= "作业许可"
        testplan =  "Plan1"
        project_name = pro()
        testcase_id = testsuit[i]['id']
        #preconditions =''
        tc_external_id = i+1

        try:
            sql_insert = 'INSERT INTO ' + testcase_report_tb + '(executed_history_id, testcase_id, testcase_name, testsuit, testplan, project, runresult, runtime, tc_external_id)' \
                                                               ' VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            data = (executed_history_id, testcase_id, testcase_name, testsuite_name, testplan, project_name, 'Unexecuted',
                    '0000-00-00 00:00:00', tc_external_id)
            logger.info('记录测试用例到测试用例报表')
            testdb.execute_insert(sql_insert, data)

            #logger.info('开始执行测试用例[id=%s，name=%s]' % (testcase_id, testcase_name))
            run_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # 记录运行时间
            case_executed_history_id = time.strftime('%Y%m%d%H%M%S', time.localtime())  # 流水记录编号
            if result == "pass":
                testcase_run_result = "pass"
            else:
                testcase_run_result = "fail"
            #testcase_run_result = testsuit[i]['result']

            logger.info('正在更新用例执行结果')
            sql_update = 'UPDATE ' + testcase_report_tb + ' SET runresult=\"%s\", runtime=\"%s\",' \
                                                 ' case_exec_history_id=\"%s\"' \
                                                 ' WHERE executed_history_id = %s and testcase_id = %s' \
                                                  ' AND project=\'%s\' AND testplan=\'%s\''
            data = (testcase_run_result, run_time, str(case_executed_history_id), executed_history_id, testcase_id, project_name,
            testplan)
            testdb.execute_update(sql_update, data)
        except Exception as e:
            logger.error('运行用例出错 %s' % e)

    logger.info('接口测试已执行完成，正在关闭数据库连接')
    testdb.close()