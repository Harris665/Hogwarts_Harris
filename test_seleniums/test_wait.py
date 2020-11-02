from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Testwait:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://home.testing-studio.com/")
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        # self.driver.find_element(By.XPATH,'//*[@]')
        self.driver.find_element(By.XPATH, '//*[@title="所有分类"]/a').click()

        # xpath = // li[ @ id = 'ember883'] / a

        sleep(3)

        # 隐式等待的方法
        def wait(x):
            return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) >= 1

        WebDriverWait(self.driver, 10).until(wait)
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
