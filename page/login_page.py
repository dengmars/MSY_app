from appium.webdriver.common.mobileby import By
from page.base_page import BasePage
from time import sleep
class LoginPage(BasePage):
    login1_locator=(By.ID,'com.meishio.app:id/user_name')
    quick_registration_locator = (By.ID,'com.meishio.app:id/user_top_view_right')
    registered_email_locator = (By.ID,'com.meishio.app:id/user_register_email_title')
    username_locator = (By.ID,'com.meishio.app:id/user_register_nickname')
    password_locator = (By.ID,'com.meishio.app:id/user_register_password_email')
    passwd_locator = (By.ID,'com.meishio.app:id/user_register_password_confirm_email')
    email_locator = (By.ID,'com.meishio.app:id/user_register_email')
    click_login_locator = (By.ID,'com.meishio.app:id/user_register_confirm_email')
    _locator = (By.ID,)


    def click_my(self):
        sleep(4)
        a = self.driver.get_window_size(windowHandle='current')
        x = a['width']
        y = a['height']
        self.driver.tap([(0.88 * x, 0.97 * y)])  # 点击我的
    def click_login1(self):
        self.find_element(self.login1_locator).click()  #点击登录/注册
    def click_quick_registration(self):
        self.find_element(self.quick_registration_locator).click() #点击快速注册
    def click_registered_email(self):
        self.find_element(self.registered_email_locator).click()  # 点击邮箱注册
    def input_username(self,username):
        self.find_element(self.username_locator ).send_keys(username)  # 输入用户名
    def input_password(self,password):
        self.find_element(self.password_locator).send_keys(password)  #输入密码
    def input_passwd(self,passwd):
        self.find_element(self.passwd_locator).send_keys(passwd)  # 输入确认密码
    def input_email(self,email):
        self.find_element(self.email_locator).send_keys(email)# 输入邮箱
    def click_login(self):
        self.find_element(self.click_login_locator).click()  # 点击注册
    def back(self):
        self.driver.press_keycode(4)  # 返回
    def login(self,username,password,passwd,email):
        self.click_my()
        self.click_login1()
        self.click_quick_registration()
        self.click_registered_email()
        self.input_username(username)
        self.input_password(password)
        self.input_passwd(passwd)
        self.input_email(email)
        self.click_login()
        self.back()



