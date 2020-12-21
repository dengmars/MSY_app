from appium import webdriver
from appium.webdriver.common.mobileby import By
from time import sleep
# 组装capacity
desired_capabilities = {
    # 测试机平台：Android or ios
    'platformName': 'Android',
    # 测试机名称，通过adb devices获取
    'deviceName': 'emulator-5554',
    # 测试机上的Android版本号，安卓机一般在设置里面查看版本号
    'platformVersion': '7.1.2',
    # 待测包名  cmd命令（aapt dump badging 安装包，需要注意有些cmd不能识别中文 | findstr activity）
    'appPackage': 'com.meishio.app',
    # 待测appium activity
    'appActivity': 'module.home.activity.SplashActivity',
    'unicodeKeyboard':True,
    'resetKeyboard':True,
    'noReset':True
}
# 启动appium session，url为appium的监听地址
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
driver.implicitly_wait(30)
a=driver.get_window_size(windowHandle='current')
x=a['width']
y=a['height']
sleep(3)
driver.tap([(0.37*x,0.96*y)])  #点击分类
sleep(3)
driver.find_element_by_xpath('//android.widget.TextView[@text="帮贫驿站"]').click()  #点击帮贫驿站
sleep(3)
driver.find_element_by_xpath('//android.widget.TextView[@text="小圩镇驿站"]').click()  #点击小圩镇驿站
sleep(3)
driver.find_element_by_xpath('//android.widget.ImageView[@resource-id="com.meishio.app:id/goods_item_image"]').click()  #点击商品
sleep(5)
driver.tap([(0.79*x,0.96*y)]) #点击立即购买
sleep(3)
driver.find_element_by_xpath('//android.widget.ImageView[@resource-id="com.meishio.app:id/product_properties_add"]').click()  #添加产品数量
sleep(3)
driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.meishio.app:id/product_properties_done"]').click()  #点击确认
sleep(3)
#点击配送方式
driver.tap([(0.92*x,0.45*y)])
sleep(3)
#选择中通
driver.find_element_by_xpath('//android.widget.ImageView[@resource-id="com.meishio.app:id/shipping_item_check"]').click()
sleep(3)
#点击提交订单
driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.meishio.app:id/order_confirm_submit"]').click()
sleep(3)



