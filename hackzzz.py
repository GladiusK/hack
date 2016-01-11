#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time
import sys,requests,random


s = requests.Session()
r = s.get('xxxxx')
flag = r.json()['result'];
if flag:
    t = random.randint(10,500)
    print 'wait: ',t
    time.sleep(t)
else:
    print 'not the day'
    sys.exit(0)

driver = webdriver.PhantomJS(executable_path='xxx/phantomjs')
driver.get('xxx')
driver.find_element_by_name('username').send_keys('xxx')
driver.find_element_by_name('password').send_keys('xxx')
time.sleep(2)
#driver.get_screenshot_as_file('xxx/aa.png')
driver.find_element_by_xpath('//*[@id="main_wraper"]/div/div[8]/a').click()

try:
    dr=WebDriverWait(driver,5)
    dr.until(lambda the_driver:the_driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/div[2]/div[1]/a').is_displayed())
except:
    print '登录失败'
    sys.exit(0)

# driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/div[2]/div[2]/div/label[3]/a').click()


driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/table/tbody/tr/td[3]/div[2]/div[2]/div/div[1]/div/div/div[2]/button').click()