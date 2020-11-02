from time import sleep
import selenium
from selenium import webdriver


class Testhogwarts():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_testdemo1(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("京东").click()
        self.driver.find_element_by_css_selector(".topic-7908 .title > a").click()

        # self.driver.set_window_size(1421,842)
        sleep(10)

# def test_sele():
#     driver = selenium.webdriver.Chrome()
#     driver.get("https://www.baidu.com")
