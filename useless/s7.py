#7,安全分析修改，删除
from backup.case7 import *
from htmlreporter import HtmlReport
import configparser
from runners import runner3
#from runners import runner2
from globalpkg.global_var import *
from runners import pc_login
testsuitex = []
testsuitrul = []

cookies = pc_login.cookies

# 记录测试开始时间
start_time = datetime.datetime.now()

#执行测试
runner3.runcase_old(testsuit7,cookies)
# 记录测试结束时间
end_time = datetime.datetime.now()
# 构造测试报告
report_title = 'ushayden_interface_autotest_report(%s)'%case
html_report = HtmlReport('test report', report_title)
html_report.set_time_took(str(end_time - start_time))  # 计算测试消耗时间

# 读取测试报告路径及文件名
config = configparser.ConfigParser()
config.read('./config/report.conf', encoding='utf-8')
dir_of_report = config['REPORT']['dir_of_report']
report_name = config['REPORT']['report_name']

# 设置报告生成路
html_report.mkdir_of_report(dir_of_report)

# 生成测试报告
html_report.generate_html(report_name)

logger.info('生成测试报告成功')

# mymail = MyMail('./config/mail.conf')
# mymail.connect()
# mymail.login()
# mail_content = 'Hi，附件为接口测试报告，烦请查阅'
# mail_tiltle = '【测试报告】接口测试报告' + str(executed_history_id)
# logger.info(html_report.get_filename())
# attachments = set([html_report.get_filename()])
#
# logger.info('正在发送测试报告邮件...')
# mymail.send_mail(mail_tiltle, mail_content, attachments)
# mymail.quit()
#
# logger.info('发送邮件成功')
# logger.info("-------------------------------------THE_END----------------------------------------------------------------------")