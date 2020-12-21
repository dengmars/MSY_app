from page.base_page import BasePage
from time import sleep
from appium.webdriver.common.mobileby import By
class ClassifyPage(BasePage):
    help_poor_post_locator=(By.XPATH,'//android.widget.TextView[@text="帮贫驿站"]')
    stage_locator=(By.XPATH,'//android.widget.TextView[@text="小圩镇驿站"]')
    commodity_locator = (By.XPATH,'//android.widget.ImageView[@resource-id="com.meishio.app:id/goods_item_image"]')
    add_the_number_locator = (By.XPATH,'//android.widget.ImageView[@resource-id="com.meishio.app:id/product_properties_add"]')
    affirm_locator = (By.XPATH,'//android.widget.TextView[@resource-id="com.meishio.app:id/product_properties_done"]')
    distribution_locator=(By.XPATH,'//android.widget.ImageView[@resource-id="com.meishio.app:id/shipping_item_check"]')
    submit_locator= (By.XPATH, '//android.widget.TextView[@resource-id="com.meishio.app:id/order_confirm_submit"]')

    def click_classify(self):
        sleep(6)
        a = self.driver.get_window_size(windowHandle='current')
        x = a['width']
        y = a['height']
        self.driver.tap([(0.37 * x, 0.96 * y)]) # 点击分类
    def click_help_poor_post(self):
        self.find_element(self.help_poor_post_locator).click()  #点击帮贫驿站
    def click_stage(self):
        self.find_element(self.stage_locator).click()  #点击小圩镇驿站
        sleep(2)
    def click_commodity(self):
        self.find_element(self.commodity_locator).click()  #点击商品

    def click_buy(self):
        sleep(6)
        a = self.driver.get_window_size(windowHandle='current')
        x = a['width']
        y = a['height']
        self.driver.tap([(0.79 * x, 0.96 * y)])
    def click_add_the_number(self):
        self.find_element(self.add_the_number_locator).click()  #添加产品数量

    def click_affirm(self):
        self.find_element(self.affirm_locator).click()  # 点击确认
    def click_delivery(self):
        sleep(3)
        a = self.driver.get_window_size(windowHandle='current')
        x = a['width']
        y = a['height']
        self.driver.tap([(0.92 * x, 0.45 * y)])
    def click_distribution(self):
        self.find_element(self.distribution_locator).click() #选择配送方式
    def click_submit(self):
        # 点击提交订单
        self.find_element(self.submit_locator).click()
    def base(self):
        self.click_classify()
        self.click_help_poor_post()
        self.click_stage()
        self.click_commodity()
        self.click_buy()
        self.click_add_the_number()
        self.click_affirm()
        self.click_delivery()
        self.click_distribution()
        self.click_submit()

