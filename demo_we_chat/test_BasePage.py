import time
import yaml
from selenium import webdriver


class TestLogin:
    def test_get_cookies(self):
     # 先获取cookies保存至本地
        self.driver = webdriver.Firefox()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        while self.driver.current_url.__contains__("loginpage_wx"):
            time.sleep(1)
        # 获取列表形式的cookies
        cookies = self.driver.get_cookies()
        # 保存到txt文件
        with open('cookies.yaml', 'w') as f:
            yaml.safe_dump(cookies,f)
        self.driver.quit()
        print(cookies)
