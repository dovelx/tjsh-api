#m

#from globalpkg.log import logger
#from globalpkg.global_var import testdb_test
from tools.gethost import pro
from globalpkg.mydb import MyDB

projectname = pro()
testdb_test = MyDB('./config/dbconfig.conf', projectname)



def sql_query_jsa_step_harm_id():
    sql_query_jsa_step_harm_id = 'SELECT jsa_step_harm_id FROM `hap_hse_clsh`.`hse_safety_analysis_harm` ORDER BY `jsa_step_harm_id` DESC LIMIT 1;'
    hse_work_task = "hse_work_task"
    #logger.info('正在查询jsa_step_harm_id')


    result = testdb_test.select_one_record(sql_query_jsa_step_harm_id)
    jsa_step_harm_id = result[0][0]
    #logger.info("===关闭数据库=============")
    testdb_test.close()
    return jsa_step_harm_id

if __name__=='__main__':
    sql_query_jsa_step_harm_id()