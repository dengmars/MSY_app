from appium import webdriver
from page.base_page import BasePage
def startapp():
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
        'unicodeKeyboard': True,
        'resetKeyboard': True,

    }
    # 启动appium session，url为appium的监听地址
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    driver.implicitly_wait(30)

    return driver