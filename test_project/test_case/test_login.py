import unittest,xml.dom.minidom,time,random
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from public_testcase import *

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox('/home/chenyueming/.mozilla/firefox/mllr6bbp.default')
        self.dom = xml.dom.minidom.parse('login_test')
        self.dom_root = self.dom.documentElement
        url = self.dom_root.getElementsByTagName('base')
        self.base_url = url[0].getAttribute('url')

    @classmethod
    def tearDownClass(self):
        time.sleep(1)
        self.driver.quit()

    def test_register_testcase_1(self):
        '''正常登录帐号'''
        count = 1
        info = get_account_passwd(self,count)
        get_login_page(self,info[0],info[1])
        self.driver.implicitly_wait(10)
        get_register_feedback_sucesslogin(self, info[0], count)

    def test_register_testcase_2(self):
        '''登录不存在的帐号'''
        count = 2
        info = get_account_passwd(self,count)
        username = info[0] + time.strftime('%Y_%m_%d_%H_%M_%S')
        get_login_page(self,username,info[1])
        self.driver.implicitly_wait(10)
        get_login_feedback_cannotlogin(self,info[2],count)

    def test_register_testcase_3(self):
        '''帐号正确，密码错误'''
        count = 3
        info = get_account_passwd(self,count)
        get_login_page(self,info[0],info[1])
        self.driver.implicitly_wait(10)
        get_login_feedback_cannotlogin(self,info[2],count)

    def test_register_testcase_4(self):
        '''只输入帐号'''
        count = 4
        info = get_account_passwd(self,count)
        get_login_page(self,info[0],info[1])
        self.driver.implicitly_wait(10)
        get_register_feedback_missinfo(self,info[2],count)

    def test_register_testcase_5(self):
        '''只输入密码'''
        count = 5
        info = get_account_passwd(self, count)
        get_login_page(self, info[0], info[1])
        self.driver.implicitly_wait(10)
        get_register_feedback_missinfo(self, info[2], count)

    def test_register_testcase_6(self):
        '''不输入帐号和密码'''
        count = 6
        info = get_account_passwd(self, count)
        get_login_page(self, info[0], info[1])
        self.driver.implicitly_wait(10)
        get_register_feedback_missinfo(self,info[2],count)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    file_obj = open('/home/chenyueming/Desktop/test_login.html','wb+')
    for i in range(1,4):
        testname = 'test_register_testcase_'+str(i)
        suite.addTest(TestRegister(testname))
    runner = HTMLTestRunner(
         stream=file_obj,
         title='Test Report',
         description='The details of test'
    )
    runner.run(suite)
    file_obj.close()

