import unittest
from model.driver_model import startapp
from page.login_page import LoginPage
from model.read_model import ReadExcel
class MyTestCase(unittest.TestCase):
    driver=startapp()
    def test_login(self):
        '''按邮箱注册'''
        lp=LoginPage(self.driver)
        username,password,passwd,email=ReadExcel('login')
        lp.login(username,password,passwd,email)

if __name__ == '__main__':
    unittest.main()
