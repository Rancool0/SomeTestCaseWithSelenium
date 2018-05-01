import unittest,xml.dom.minidom,time,random
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from public_testcase import *
class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox('/home/chenyueming/.mozilla/firefox/mllr6bbp.default')
        self.dom = xml.dom.minidom.parse('register_test')
        self.dom_root = self.dom.documentElement
        url = self.dom_root.getElementsByTagName('base')
        self.base_url = url[0].getAttribute('url')

    @classmethod
    def tearDownClass(self):
        time.sleep(1)
        self.driver.quit()

    def test_register_testcase_1(self):
        '''正常注册帐号'''
        count = 1
        info = get_account_passwd(self,count)
        username = info[0] + time.strftime('%Y_%m_%d_%H_%M_%S')
        get_register_page(self,username,info[1])
        self.driver.implicitly_wait(10)
        get_register_feedback_sucesslogin(self, username, count)

    def test_register_testcase_2(self):
        '''注册长度等于帐号长度限制的帐号'''
        count = 2
        info = get_account_passwd(self,count)
        random_num = (random.choice(range(10000, 100000)))
        username = str(random_num) * 30
        get_register_page(self,username,info[1])
        self.driver.implicitly_wait(10)
        get_register_feedback_sucesslogin(self,username,count)

    def test_register_testcase_3(self):
        '''注册长度超过帐号长度限制的帐号'''
        count = 3
        info = get_account_passwd(self,count)
        random_num = (random.choice(range(10000, 100000)))
        username = str(random_num) * 50
        get_register_page(self,username,info[1])
        self.driver.implicitly_wait(10)
        current_name = username[:150]
        get_register_feedback_sucesslogin(self,current_name,count)

    def test_register_testcase_4(self):
        '''注册非法帐号'''
        count = 4
        info = get_account_passwd(self,count)
        get_register_page(self,info[0],info[1])
        self.driver.implicitly_wait(10)
        get_register_feedback_wrongaccout(self,info[2],count)

    def test_register_testcase_5(self):
        '''注册中文帐号'''
        count = 5
        info = get_account_passwd(self, count)
        username = info[0] + time.strftime('%Y_%m_%d_%H_%M_%S')
        get_register_page(self, username, info[1])
        self.driver.implicitly_wait(10)
        get_register_feedback_sucesslogin(self, username, count)

    def test_register_testcase_6(self):
        '''不输入密码进行帐号注册'''
        count = 6
        info = get_account_passwd(self, count)
        get_register_page(self, info[0], info[1])
        self.driver.implicitly_wait(10)
        get_register_feedback_missinfo(self,info[2],count)

    def test_register_testcase_7(self):
        '''不输入帐号进行帐号注册'''
        count = 7
        info = get_account_passwd(self, count)
        get_register_page(self, info[0], info[1])
        self.driver.implicitly_wait(10)
        get_register_feedback_missinfo(self,info[2],count)

    def test_register_testcase_8(self):
        '''注册帐号密码一致的帐号'''
        count = 8
        info = get_account_passwd(self, count)
        get_register_page(self, info[0], info[1])
        self.driver.implicitly_wait(10)
        get_register_feedback_wrongpassword(self, info[2], count)

    def test_register_testcase_9(self):
        '''注册弱密码帐号'''
        count = 9
        info = get_account_passwd(self, count)
        get_register_page(self, info[0], info[1])
        self.driver.implicitly_wait(10)
        get_register_feedback_wrongpassword(self, info[2], count)

    def test_register_testcase_10(self):
        '''两次输入密码不一致'''
        count = 10
        login = self.dom_root.getElementsByTagName('login%d' % count)
        username = login[0].getAttribute('username')
        password = login[0].getAttribute('passwd')
        password_confirm = login[0].getAttribute('passwd_confirm')
        wrong_message = login[0].getAttribute('wrong_msg')
        get_register_page(self, username, password,password_confirm)
        self.driver.implicitly_wait(10)
        get_register_feedback_wrongpassword(self, wrong_message, count)

    def test_register_testcase_11(self):
        '''注册纯数字密码帐号'''
        count = 11
        info = get_account_passwd(self, count)
        get_register_page(self, info[0], info[1])
        self.driver.implicitly_wait(10)
        get_register_feedback_wrongpassword(self, info[2], count)

    def test_register_testcase_12(self):
        '''注册密码长度小于8的帐号'''
        count = 12
        info = get_account_passwd(self, count)
        get_register_page(self, info[0], info[1])
        self.driver.implicitly_wait(10)
        text = self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[3]/div[3]').text
        assert info[2] in text, 'testcase %d fail' % count

    def test_register_testcase_13(self):
        '''注册带空格密码的帐号'''
        count = 13
        info = get_account_passwd(self, count)
        username = info[0] + time.strftime('%Y_%m_%d_%H_%M_%S')
        get_register_page(self, username, info[1])
        self.driver.implicitly_wait(10)
        get_register_feedback_sucesslogin(self, username, count)


    def test_register_testcase_14(self):
        '''注册密码过长的帐号'''
        count = 14
        info = get_account_passwd(self, count)
        username = info[0] + time.strftime('%Y_%m_%d_%H_%M_%S')
        get_register_page(self, username, info[1])
        self.driver.implicitly_wait(10)
        get_register_feedback_sucesslogin(self, username, count)

    def test_register_testcase_15(self):
        '''注册已被注册过了的帐号'''
        count = 15
        info = get_account_passwd(self, count)
        get_register_page(self, info[0], info[1])
        self.driver.implicitly_wait(10)
        get_register_feedback_wrongaccout(self,info[2],count)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    file_obj = open('/home/chenyueming/Desktop/test_register.html','wb+')
    for i in range(1,16):
        if i == 6 or i ==7:
            continue
        testname = 'test_register_testcase_'+str(i)
        suite.addTest(TestRegister(testname))
    runner = HTMLTestRunner(
         stream=file_obj,
         title='Test Report',
         description='The details of test'
    )
    runner.run(suite)
    file_obj.close()
