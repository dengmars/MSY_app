from BeautifulReport import BeautifulReport
import time
import unittest


discover=unittest.defaultTestLoader.discover("../case","test_case.py")
BeautifulReport(discover).report(
    description=u'自动化测试报告',

    filename=time.strftime("%Y-%m-%d %H_%M_%S")
)