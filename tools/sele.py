import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#暂时关闭登录
'''
#selenium登录测试长庆
driver = webdriver.Firefox()
driver.get("http://192.168.6.27:6030/passports/login?service=http%3A%2F%2F192.168.6.27%3A6030%2Fportals%2Fcas&tenantCode=cqsh&trial=false")

driver.find_element(By.ID, "username").send_keys("test")
driver.find_element(By.ID, "pwd1").send_keys("1")
driver.find_element(By.CSS_SELECTOR, ".justUse").click()

#获取JSESSIONID
c= driver.get_cookies()
#print (c)
#print (c[0])
for a in c:
    #print (a)
    if a['name'] == 'JSESSIONID':
        b=a
        #print (b)
cookies={'JSESSIONID': b['value']}

'''