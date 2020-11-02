import shelve
from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDome1():

    def setup_method(self, method):
        # 复用浏览器
        # 命令行输入 chrome --remote-debugging-port=9222
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()

        # self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self, medhod):
        self.driver.quit()

    # "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

    def test_testdemo1(self):
        # self.driver.get("https://www.google
        # rint(self.driver.window_handles(1))

        # elf.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys("halloween")
        # self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/ul/li[1]/div/div[2]/div[1]/span').click()
        # self.driver.set_window_size(1421,842)
        sleep(5)

    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        # #get_cookies() 可以获取当前打开页面的cookies 信息
        # #add_cookie() 可以吧cookie 添加当页面中去。
        # print(cookies)
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'd-GeqaiA6Dn2xniYLL9-srHH2PpU0LcIOmn7i7MszpNAB5OmWGbaW-sTD11jdVn-VgvIvJUC1Zk42fTCmHNWag838WaVMHjO8ORcn-J-JlGQo4eqPA_5qhEhiktCXSFlHNRNs4cSlIajO_XuUTZ1kcPWEYgmS2my-iJBVzVjypxH0W2PlcKS9IW7tOeMoM8ozmfdp5EOX1UupCpQnecTkzspG8KXxtzDPcXIaPKzERWkWr89BLuE6Eza19eWC1WSk6XP9mDUCXGlJjQrXTO-ww'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'QqBXb4rkH5IJkRDpKmbA6W8iOvAaTiVPD8Su-wqFx8-mLzr3KhafniDRrQFiW77i'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1604155512'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853854918049'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 1604242417, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.2032578262.1604142322'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a9932599'}, {'domain': '.work.weixin.qq.com', 'expiry': 1635691511, 'httpOnly': False,
                                    'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                                    'value': '1604142317'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '3790140536314934'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '51753984'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1604173850, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '6qp84g9'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1606748081, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 1667228017, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1096262099.1531834228'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
             'secure': False, 'value': '825589821'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '6688239776'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325121175509'},
            {'domain': '.qq.com', 'expiry': 1834839110, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '1_825589821'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853854918049'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': 'c7ba253903bb3bb6e8fce19a3b01eff87ad8593d29a5e5532921ae184a7420b6'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1635678314, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 111466884380, 'httpOnly': True, 'name': 'gaduid', 'path': '/',
             'secure': False, 'value': '59a4e7499facc'},
            {'domain': '.qq.com', 'expiry': 1819421512, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'yWEycWTqZi'}]

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cook in cookies:
            self.driver.add_cookie(cook)

        self.driver.refresh()
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(5)

        # db = shelve.open("cookies")
        # db['cookie'] = cookies
        # db.close()

    def test_shelve(self):
        # shelve python 内置模块，专门用来对数据进行持久化存储的，相当于小型数据库
        # 可以通过 key， value 来把数据保存到shelve中
        db = shelve.open("cookies")
        cookies = db['cookie']
        db.close()
        # 利用读取的coolie 完成登录操作
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cook in cookies:
            self.driver.add_cookie(cook)

        self.driver.refresh()
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(5)

        # self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]').click()
        # self.driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[1]/a/input').send_keys("E:/HUANG/Bingo/mydate.xlsx")
        # filename = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[1]/div[2]').text
        # assert 'mydate.xlsx' == filename
        # sleep(3)
