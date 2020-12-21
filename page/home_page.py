# -*- coding: utf-8 -*-
# @Time : 2020/12/19 11:21
# @Author : fcj11
# @Email : yangfit@126.com
# @File : home_page.py
# @Project : meishiyuan
from time import sleep
from page.base_page import BasePage
from appium.webdriver.common.mobileby import By

class HomePage(BasePage):
    # 定位点击跳过
    skip_locator = (By.ID, 'com.meishio.app:id/lead_skip')
    # 定位【分类】
    classify_locator = (By.XPATH,
                        '//android.widget.LinearLayout[@resource-id=\"com.meishio.app:id/main_tool_bg\"]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]')
    # 定位【购物车】
    shopping_locator = (By.XPATH,
                        '//android.widget.LinearLayout[@resource-id=\"com.meishio.app:id/main_tool_bg\"]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]')
    # 定位【我的】
    my_locator = (By.XPATH,
                  '//android.widget.LinearLayout[@resource-id=\"com.meishio.app:id/main_tool_bg\"]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]')
    # 定位农村土鸡蛋
    egg_locator = (By.XPATH,
                   '//android.widget.GridView[@resource-id=\"com.meishio.app:id/product_recommend_home_gridview\"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]')
    #添加购物车确定
    confirm_locator = (By.ID,'com.meishio.app:id/product_properties_done')


    def click_skip(self):  # 点击跳过
        self.find_element(self.skip_locator).click()

    def click_egg(self):  # 点击【农村草鸡蛋】
        self.find_element(self.egg_locator).click()

    def click_calssify(self):  # 点击【分类】
        self.find_element(self.classify_locator).click()

    def click_shopping_car(self):  # 点击【购物车】
        self.find_element(self.shopping_locator).click()

    def click_my(self):  # 点击【我的】
        self.find_element(self.my_locator).click()

    def click_join_shopping_car(self):  #点击加入购物车
        self.tap(450,1850)

    def click_confirm(self):    #添加购物车点击【确定】
        self.find_element(self.confirm_locator).click()

    def join_shopping_car(self):   #购物流程
        sleep(1)
        self.click_skip()   #进入app时点击跳过
        sleep(2)
        self.driver.swipe(300, 300, 300, 800, 500)  # 刷新
        sleep(1)
        self.click_egg()  #选择农村草鸡蛋
        sleep(1)
        self.click_join_shopping_car()   #点击加入购物车
        sleep(1)



