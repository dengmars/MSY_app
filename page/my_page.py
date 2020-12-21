# -*- coding: utf-8 -*-
# @Time : 2020/12/19 11:23
# @Author : fcj11
# @Email : yangfit@126.com
# @File : my_page.py
# @Project : meishiyuan
from page.base_page import BasePage
from appium.webdriver.common.mobileby import By
from time import sleep


class MyPage(BasePage):
    # 定位登录/注册入口
    login_locator = (By.ID, 'com.meishio.app:id/user_name')
    # 定位用户名输入框
    usename_locator = (By.XPATH, '//android.widget.EditText[@resource-id=\"com.meishio.app:id/user_login_username_email_phone\"]')
    # 定位密码输入框
    password_locator = (By.XPATH, '//android.widget.EditText[@resource-id=\"com.meishio.app:id/user_login_password\"]')
    # 定位登录按钮
    submit_locator = (By.XPATH, '//android.widget.Button[@resource-id=\"com.meishio.app:id/user_login_btn\"]')

    def click_login(self):  # 点击登录/注册
        self.find_element(self.login_locator).click()

    def input_username(self,username):  # 输入用户名
        self.find_element(self.usename_locator).send_keys(username)

    def input_password(self,password):  # 输入密码
        self.find_element(self.password_locator).send_keys(password)

    def click_submit(self):  # 点击登录
        self.find_element(self.submit_locator).click()

    def register(self,username,password):   #登录流程
        self.input_username(username)  # 输入用户名
        self.input_password(password)  # 输入密码
        self.click_submit()  # 点击登录
        sleep(2)
