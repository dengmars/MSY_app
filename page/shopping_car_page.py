# -*- coding: utf-8 -*-
# @Time : 2020/12/19 11:22
# @Author : fcj11
# @Email : yangfit@126.com
# @File : shopping_car_page.py
# @Project : meishiyuan
from time import sleep

from page.base_page import BasePage
from appium.webdriver.common.mobileby import By
from time import sleep


class ShopingCarPage(BasePage):
    # 定位全选商品
    select_locator = (By.ID, 'com.meishio.app:id/shop_cart_item_choice')
    # 定位【结算】
    account_locator = (By.ID, 'com.meishio.app:id/shop_cart_view_balance')
    # 定位选择配送方式
    distribution_locator = (By.XPATH,'//android.widget.TextView[@resource-id=\"com.meishio.app:id/order_confirm_shipping_type\"]')
    # 定位选择中通快递
    expressage_locator = (By.ID, 'com.meishio.app:id/shipping_item_check')
    # 定位提交订单
    # submit_locator = (By.XPATH,'//android.widget.TextView[@resource-id=\"com.meishio.app:id/order_confirm_submit\"]')
    #定位购物车
    shopping_car = (By.XPATH,'//android.widget.ImageView[@resource-id=\"com.meishio.app:id/goods_detail_cart_image\"]')
    def click_select(self):  # 选择全部商品
        self.find_element(self.select_locator).click()

    def click_account(self):  # 点击结算
        self.find_element(self.account_locator).click()

    def click_distribution(self):  # 点击选择配送方式
        self.find_element(self.distribution_locator).click()

    def click_expressage(self):  # 点击中通快递
        self.find_element(self.expressage_locator).click()

    def click_submit(self):  # 点击提交订单
        BasePage(self.driver).tap(870,1855)
        # self.find_element(self.submit_locator).click()

    def click_shopping_car(self):   #点击购物车
        self.find_element(self.shopping_car).click()

    def submit_oder(self):  #提交订单流程
        self.click_shopping_car()  #点击购物车
        sleep(2)
        self.click_select()   #点击选择全部商品
        sleep(1)
        self.click_account()   #点击结算
        sleep(1)
        self.click_distribution()   #点击选择配送方式
        sleep(1)
        self.click_expressage()   #点击选择中途快递
        sleep(2)
        self.click_submit()   #点击提交订单
        sleep(1)


