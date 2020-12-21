
class BasePage():
    def __init__(self,driver):
        self.driver=driver
    def find_element(self,locator):
        return self.driver.find_element(*locator)
    def tap(self, x, y):   #封装tap
        qqq = self.driver.get_window_size()
        xx = qqq['width'] * x / 1080
        yy = qqq['height'] * y / 1920
        return self.driver.tap([(xx, yy)], 100)


