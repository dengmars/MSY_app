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
print(a)
x=a['width']
y=a['height']
sleep(3)
driver.tap([(0.88*x,0.97*y)])#点击我的
sleep(3)
driver.find_element_by_id('com.meishio.app:id/user_name').click()  #点击登录/注册
sleep(3)
driver.find_element_by_id('com.meishio.app:id/user_top_view_right').click() #点击快速注册
sleep(3)
driver.find_element_by_id('com.meishio.app:id/user_register_email_title').click()  #点击邮箱注册
sleep(1)
driver.find_element_by_id('com.meishio.app:id/user_register_nickname').send_keys('dsad') #输入用户名
sleep(1)
driver.find_element_by_id('com.meishio.app:id/user_register_password_email').send_keys('123456')  #输入密码
sleep(1)
driver.find_element_by_id('com.meishio.app:id/user_register_password_confirm_email').send_keys('123456')  #输入确认密码
sleep(1)
driver.find_element_by_id('com.meishio.app:id/user_register_email').send_keys('2514011735@qq.com')# 输入邮箱
sleep(1)
driver.find_element_by_id('com.meishio.app:id/user_register_confirm_email').click()  #点击注册
sleep(1)
driver.press_keycode(4) #返回
sleep(5)

driver.quit()
