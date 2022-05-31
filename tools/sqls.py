#pc
#操作hse_work_ticket表，获取workticketid获取
ticket = 'select workticketid from hse_work_ticket order by workticketid desc limit 1'
ticket = "SELECT workticketid FROM hse_work_ticket WHERE worktype = 'dh' ORDER BY `created_dt` DESC LIMIT 1"
ticket = "SELECT workticketid FROM hse_work_ticket WHERE worktype = 'dh' ORDER BY `workticketid` DESC LIMIT 1"
#ticket = 'select workticketid from hse_work_ticket where  worktype = "lsyd" ORDER BY created_dt desc limit 1;'
ts = 'select ts from hse_work_ticket order by ts desc limit 1'

worktaskid = 'select worktaskid from hse_work_task ORDER BY created_dt desc limit 1'

worktaskid1 = 'select worktaskid from hse_work_ticket ORDER BY created_dt desc limit 1'

appoint_id ='SELECT work_appoint_id from hse_safety_task ORDER BY  work_appoint_id desc LIMIT 1'

#SELECT * FROM `hap_hse_tjsh`.`hse_ticket_mbcd` ORDER BY `workticketmbcdid` DESC LIMIT 0,1000

workticketmbcdid = 'SELECT workticketmbcdid FROM `hap_hse_tjsh`.`hse_ticket_mbcd` ORDER BY `workticketmbcdid` DESC LIMIT 1'

sql_query_work_jsaid='SELECT jsaid from hse_safety_analysis ORDER BY  jsaid desc LIMIT 1'

sql_query_work_safeclarid='SELECT safeclarid from hse_safety_disclosure ORDER BY  safeclarid desc LIMIT 1'

sql_query_work_appointid ='SELECT work_appoint_id from hse_work_appoint ORDER BY  created_dt desc LIMIT 1'

sql_query_wf_instance ='SELECT wf_instance from hse_work_appoint ORDER BY  created_dt desc LIMIT 1'

sql_query_jsa_step_harm_id = 'SELECT jsa_step_harm_id FROM `hap_hse_tjsh`.`hse_safety_analysis_harm` ORDER BY `jsa_step_harm_id` DESC LIMIT 1;'

sql_query_jsastepid = 'SELECT jsastepid FROM `hap_hse_tjsh`.`hse_safety_analysis_harm` ORDER BY `jsa_step_harm_id` DESC LIMIT 1;'

sql_query_jsa_step_measure_id = 'SELECT jsa_step_measure_id FROM `hap_hse_tjsh`.`hse_safety_analysis_measure` ORDER BY `jsa_step_measure_id` DESC LIMIT 1'

#SELECT worknumber FROM `hap_hse_tjsh`.`hse_safety_task` ORDER BY `worktaskid` DESC LIMIT 1

sql_query_jsa_worknumber = 'SELECT worknumber FROM `hap_hse_tjsh`.`hse_safety_task` ORDER BY `worktaskid` DESC LIMIT 1'

sql_query_jsa_workname= 'SELECT workname FROM `hap_hse_tjsh`.`hse_safety_task` ORDER BY `worktaskid` DESC LIMIT 1'


