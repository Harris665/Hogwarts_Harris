from selenium import webdriver
from selenium.webdriver.common.by import By


class TestByid:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")

    def test_id(self):
        self.driver.find_element(By.CSS_SELECTOR, '[id=kw]').send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID, 'su').click()

# http://sahitest.com/demo/clicks.htm
