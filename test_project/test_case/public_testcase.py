import time

def get_register_page(self,username,password,password_confirm=''):
    if len(password_confirm)<1:
        password_confirm = password
    driver = self.driver
    driver.implicitly_wait(10)
    driver.get(self.base_url)
    driver.find_element_by_xpath('//*[@id="id_username"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="id_password1"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="id_password2"]').send_keys(password_confirm)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div[4]/button').click()

def get_login_page(self,username,password):
    driver = self.driver
    driver.implicitly_wait(10)
    driver.get(self.base_url)
    driver.find_element_by_xpath('//*[@id="id_username"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="id_password"]').send_keys(password)
    driver.find_element_by_css_selector(".btn").click()

def get_register_feedback_wrongaccout(self,wrong_message,count):
    driver = self.driver
    text = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[1]/div[1]').text
    assert text in wrong_message,'testcase %d fail' % count

def get_register_feedback_wrongpassword(self,wrong_message,count):
    driver = self.driver
    text = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[3]/div[1]').text
    assert wrong_message in text,'testcase %d fail' % count

def get_register_feedback_sucesslogin(self,username,count):
    text = self.driver.find_element_by_xpath('/html/body/nav/div/div[2]/ul[2]/li[1]/a').text
    assert 'Hello, %s.' % username in text, 'testcase %d fail' % count

def get_register_feedback_missinfo(self,info,count):
    text = self.driver.switch_to_active_element().get_attribute('placeholder')
    assert text in info, 'testcase %d fail' % count

def get_login_feedback_cannotlogin(self,wrong_message,count):
    text = self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[1]').text
    assert wrong_message in text, 'testcase %d fail' % count



def get_account_passwd(self,count):
    login = self.dom_root.getElementsByTagName('login%d' % count)
    username = login[0].getAttribute('username')
    password = login[0].getAttribute('passwd')
    wrong_message = login[0].getAttribute('wrong_msg')
    return username,password,wrong_message

