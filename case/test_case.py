from page.base_page import BasePage
from page.classify_page import ClassifyPage
from model.driver_model import startapp
from page.home_page import HomePage
from page.my_page import MyPage
from page.login_page import LoginPage
import unittest
from model.read_model import ReadExcel
from page.shopping_car_page import ShopingCarPage
class ClassifyTest(unittest.TestCase):
    '''商品分类-切换分类-选择商品-立即购买-提交订单'''
    driver = startapp()
    # def test_classify(self):
    #     HomePage(self.driver).click_skip()
    #     HomePage(self.driver).click_my()
    #     MyPage(self.driver).click_login()
    #     mp = MyPage(self.driver)
    #     username,password=ReadExcel('register')
    #     mp.register(username,password)
    #     cp = ClassifyPage(self.driver)
    #     cp.base()
    # def test_login(self):
    #     '''按邮箱注册'''
    #     HomePage(self.driver).click_skip()
    #     lp=LoginPage(self.driver)
    #     username,password,passwd,email=ReadExcel('login')
    #     lp.login(username,password,passwd,email)
    def test_1(self):
        """选择商品 - 加入购物车 - 登录（未登录情况下）- 加入购物车 - 购物车结算 - 选择配送方式 - 提交订单"""
        #选择商品 - 加入购物车
        hp = HomePage(self.driver)
        hp.join_shopping_car()

        #登录
        username,password = ReadExcel('register')
        MyPage(self.driver).register(username,password)

        #加入购物车
        hp.click_join_shopping_car()
        #点击确定
        hp.click_confirm()

        #购物车 - 选择配送方式 - 提交订单
        ShopingCarPage(self.driver).submit_oder()



    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
