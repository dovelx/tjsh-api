#pc
#操作hse_work_ticket表，获取workticketid获取
ticket = 'select workticketid from hse_work_ticket order by workticketid desc limit 1'
#ticket = "SELECT workticketid FROM hse_work_ticket WHERE worktype = 'dh' ORDER BY `created_dt` DESC LIMIT 1"
#ticket = "SELECT workticketid FROM hse_work_ticket WHERE worktype = 'dh' ORDER BY `workticketid` DESC LIMIT 1"
#ticket = 'select workticketid from hse_work_ticket where  worktype = "lsyd" ORDER BY created_dt desc limit 1;'
ts = 'select ts from hse_work_ticket order by ts desc limit 1'

worktaskid = 'select worktaskid from hse_work_task ORDER BY created_dt desc limit 1'

worktaskid_in_ticketable = 'select worktaskid from hse_work_ticket ORDER BY created_dt desc limit 1'

sql_query_work_appointid ='SELECT work_appoint_id from hse_work_appoint ORDER BY  created_dt desc LIMIT 1'

sql_query_wf_instance ='SELECT wf_instance from hse_work_appoint ORDER BY  created_dt desc LIMIT 1'
sql_query_measureid = 'select worktaskmeasureid from hse_work_task_measure ORDER BY worktaskmeasureid desc LIMIT 1;'




